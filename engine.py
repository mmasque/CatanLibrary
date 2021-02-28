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
        
    def roll_dice(self):
        return randint(1,6) + randint(1,6)
    
    
    def run_game(self):
        board = Board(self.rn_pairs(3), 3)
        
        
        # initial placement of houses
        # ...

        # general turn of each player loop                


    def place_starting_houses(self, player):
        available_nodes = board.available_nodes()
        chosen_node = player.choose_house(board)
        
        if chosen_node in available_nodes:            
            # valid, place a house
            node.inhabitant = House(player)
            player.houses.append(node.inhabitant)
        else:
            # crash, player failed
            raise ValueError("Invalid house selection by player: " +  player.display_name)
        