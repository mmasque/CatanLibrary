class Board:
    def __init__(self, edge_length=3):
        """ Make tiles with a default size of board
        - edge_length: number of tiles at an edge of the board
        """
        for row_length in range(edge_length, 2 * edge_length):
            current_row = []
            for tile in range(row_length):
                #create a new tile
                #add it to the current_row
                pass

class Tile:
    def __init__(self, dice_number, resource, nodes, robber=False):
        self.dice_number = dice_number
        self.resource = resource
        self.nodes = nodes
        self.robber = robber

    #def _add_node(self, )

    #def get_node(self, )
class Node:
    def __init__(self, edges, inhabitant=None):
        self.edges = edges
        self.inhabitant = inhabitant

class Edge:
    def __init__(self, starting_node, ending_node, inhabitant_road):
        self.starting_node = starting_node
        self.ending_node = ending_node
        self.inhabitant_road = inhabitant_road
