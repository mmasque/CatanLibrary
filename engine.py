from player import Player
from board import *
from random import randint
#next time the game has to be played
# so ordered, marcel and amit, 5.4.21
class RuleBook:
    types = ["WHEAT", "BRICK", "STONE", "WOOD", "CATTLE"]

    @staticmethod
    def resources_dict(wood, brick, wheat, cattle, stone):
        cost = {}
        cost["WOOD"] = wood
        cost["BRICK"] = brick
        cost["WHEAT"] = wheat
        cost["CATTLE"] = cattle
        cost["STONE"] = stone
        return cost

    @staticmethod
    def road_cost():
        return RuleBook.resources_dict(1,1,0,0,0)
    
    @staticmethod
    def house_cost():
        return RuleBook.resources_dict(1,1,1,1,0)
    @staticmethod
    def upgrade_cost():
        return RuleBook.resources_dict(0,0,2,0,3)
    @staticmethod
    def development_cost():
        return RuleBook.resources_dict(0,0,1,1,1)
    @staticmethod
    def can_buy(available, required):
        return all([available[tp] >= required[tp] for tp in RuleBook.types])

class Engine:
    def __init__(self, player_names):
        self.players = []
        self.board = None
        pid = 0
        for player_name in player_names:
            self.players.append(Player(pid, player_name))
            pid += 1
        
        self.action_enum = {
            "HOUSE"     :   self.add_house,
            "ROAD"      :   self.add_road,
            "UPGRADE"   :   self.upgrade_house
        }
        
    def roll_dice(self):
        return randint(1,6) + randint(1,6)
    
    def rn_pairs(self,n):
        return [ResourceNumberPair("WHEAT", 5), ResourceNumberPair("WOOD", 12), ResourceNumberPair("BRICK", 5)]
    
    def distribute_wealth(self,dice_roll):
        # TODO: clean this up, communism should be neat
        for tile in self.board.tiles:
            if tile.dice_number == dice_roll:
                for node in tile.nodes:
                    if node.inhabitant is not None:
                        player = self.players[node.id]
                        player.add_resource(tile.resource)
                        if node.inhabitant.upgraded:
                            player.add_resource(tile.resource)

    def run_game(self):
        self.board = Board(self.rn_pairs(3), 3)
        
        # initial placement of houses and roads
        # ...
        for players in [self.players, reversed(self.players)]: #[i for i in range(len(self.players))] + [len(selfi for i in range(len(self.players))]
            for player in players:
                win = self.place_starting_house(player)
                self.place_starting_road(player)
                if win:
                    self.end_game()
                    return
        
        # general turn of each player loop      
        n = len(self.players)
        id_player = 0
        
        while True:
            #roll dice and give out stuff
            dice_roll = self.roll_dice()
            self.distribute_wealth(dice_roll)

            #player turn
            player = self.players[id_player]
            done = False
            action, arguments, done = player.take_action()
            
            while not done:
                win = self.action_enum[action](**arguments)
                if win:
                    self.end_game()
                    return
                action, arguments, done = player.take_action()
            id_player = (id_player + 1)%n

    #YOU LEFT THE ZOOM CALL 
    #I KNOW I KNOW, GIMME A SEC
    #HAHA OKAY LETS LEAVE THIs here as a comment
    def place_starting_house(self, player):
        available_nodes = board.available_nodes()
        chosen_node = player.choose_house(board)
        
        if chosen_node in available_nodes:            
            # valid, place a house
            # need to update available nodes in the board
            chosen_node.build(House(player))
            # need to update the player's repr of the board.
            player.place_house(chosen_node.inhabitant) # remember to increase score
        else:
            # crash, player failed
            raise ValueError("Invalid house selection by player: " +  player.display_name)

        return player.increase_point()

    
    def place_starting_road(self, player):
        available_roads = player.road_options()
        chosen_road = player.choose_road()
        
        if chosen_road in available_roads:            
            # valid, place the road
            chosen_road.add_inhabitant(player.id)
            player.place_road(chosen_road)
            
            # This is annoying, because we have to update the nodes that the player now owns. 
            # this should happen automatically when we call add road to player. 

        
        else:
            # crash, player failed
            raise ValueError("Invalid road selection by player: " +  player.display_name)
    
    # TODO: Abstract sanity checks 
    def add_house(self, player, node):
        # check resources
        if not RuleBook.can_buy(player.resources, RuleBook.house_cost()):
            raise ValueError("Player " + str(player.id) + " cannot buy the house")
        if not node in player.house_options():
            raise ValueError("Player's (" + str(player.id) + ") choice of node is not in their options")
        if not (node in self.board.available_nodes()):
            raise ValueError("player house_options function is broken")
        
        # build a house
        player.place_house(node)
        return player.increase_point()
        
    def add_road(self, player, road):
        if not RuleBook.can_buy(player.resources, RuleBook.road_cost()):   
            raise ValueError("Player " + str(player.id) + " cannot buy the road")
        if not road in player.road_options():
            raise ValueError("Player's (" + str(player.id) + ") choice of road is not in their options")

        road.add_inhabitant(player.id)
        return False

    def upgrade_house(self, player, house):
        if not RuleBook.can_buy(player.resources, RuleBook.upgrade_cost()):   
            raise ValueError("Player " + str(player.id) + " cannot upgrade the house")
        if not house.player == player:
            raise ValueError("This house is not owned by Player with id " + str(player.id))
        if house.upgraded:
            raise ValueError("This house has already been upgraded")

        house.upgrade()
        return player.increase_point()
        
        
    def end_game(self):
        # get the scores of each player, rank them, declare winner
        players = [(player.points, player.pid) for player in self.players]
        players.sort()
        place = 1
        for p in players:
            print(str(place) + ". player " + p[1] + " with a score of " + str(p[0]) + " points")
            place += 1

