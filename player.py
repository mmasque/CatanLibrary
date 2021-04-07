from board import *
from engine import RuleBook


class Player():
    def __init__(self, p_id, display_name):
        self.id = p_id
        self.display_name = display_name
        self.points = 0
        self.nodes = [] 
        self.houses = []
        self.roads = []
        self.resources = {key: 0 for key in RuleBook.types}
        
    # example : self.houses[choice].upgrade()

    def __eq__(self, player):
        return self.id == player.id

    def add(self, resource):
        self.resources[resource] += 1

    def increase_point(self):
        self.points += 1
        return self.points >= 10
    
    def decrease_point(self):
        self.points -= 1

    def road_options(self):
        opts = []
        for node in self.nodes:
            opts += node.potential_outgoing_roads(self)
        return list(set(opts))

    def house_options(self):
        opts = []
        for node in self.nodes:
            if node.can_build and node not in opts:
                opts.append(node)
        return opts

    def upgrade_options(self):
        return [house for house in self.houses if not house.upgraded]

    def place_road(self, edge):
        # update its representation of available nodes
        self.add_node(edge.start)
        self.add_node(edge.end)
        self.roads.append(edge)
    
    def place_house(self, house):
        self.houses.append(house)

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
    
    def choose_house(self, board):
        pass

    def choose_road(self, board):
        pass

