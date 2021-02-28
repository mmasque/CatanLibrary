from board import *

types = ["WHEAT", "BRICK", "STONE", "WOOD", "CATTLE"]

class Player():
    def __init__(self, p_id, display_name):
        self.id = p_id
        self.display_name = display_name
        self.points = 0
        self.nodes = {}#[] 
        self.houses = []
        self.resources = {key: 0 for key in types}
        
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
        for node in self.nodes.values():
            opts += node.potential_outgoing_roads(self)
        return list(set(opts))

    def house_options(self):
        opts = []
        for node in self.nodes.values():
            if node.can_build and node not in opts:
                opts.append(node)
        return opts

    def upgrade_options(self):
        return [house for house in self.houses if not house.upgraded]




    