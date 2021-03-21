from player import *
from board import *
from random import randint
class RuleBook:
    def resources_dict(wood, brick, wheat, cattle, stone):
        cost = {}
        cost["WOOD"] = wood
        cost["BRICK"] = brick
        cost["WHEAT"] = wheat
        cost["CATTLE"] = cattle
        cost["STONE"] = stone
        return cost

    def road_cost():
        return resources_dict(1,1,0,0,0)
    
    def house_cost():
        return resources_dict(1,1,1,1,0)
    
    def upgrade_cost():
        return resources_dict(0,0,2,0,3)
    
    def development_cost():
        return resources_dict(0,0,1,1,1)

class Engine:
    def __init__(self, player_names):
        self.players = []
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
    
    
    def run_game(self):
        board = Board(self.rn_pairs(3), 3)
        
        # initial placement of houses and roads
        # ...
        for players in [self.players, reversed(self.players)]: #[i for i in range(len(self.players))] + [len(selfi for i in range(len(self.players))]
            for player in players:
                win = self.place_starting_house(player)
                self.place_starting_road(player)
                if win:
                    self.end_game()
        
        # general turn of each player loop      
        n = len(self.players)
        id_player = 0          
        while True:
            player = self.players[id_player]
            done = False
            while not done: 
                action, arguments, done = player.take_action()
                self.action_enum[action](**arguments)

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
            player.place_house(node.inhabitant)
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
    
    def add_house(self, player, node):
        # check resources
        if all([for tp in types])
        # check they can build at node
        # build a house

    def end_game(self):
        pass

