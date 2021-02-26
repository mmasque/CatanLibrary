from board import *

types = ["WHEAT", "BRICK", "STONE", "WOOD", "CATTLE"]

class Player():
    def __init__(self, p_id, display_name):
        self.id = p_id
        self.display_name = display_name
        self.points = 0
        self.nodes = {}
        self.houses = {}
        self.resources = {key: 0 for key in resources}
        
    # example : self.houses[choice].upgrade()

    def __eq__(self, player):
        return self.id == player.id

    def add(self, resource):
        pass
