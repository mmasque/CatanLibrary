class Board:
    def __init__(self, numbers, resources, edge_length=3):
        """ Make tiles with a default size of board
        - edge_length: number of tiles at an edge of the board
        1. Initialise all the tiles
        2. Initialise every node, and figure out the tiles it belongs to and add
        it to those tiles
        I decided to get rid of edges, and perhaps a simpler solution than keeping the houses
        and edges on the tile and edge class is to keep them in dicts of nodes and node pairs in board. 
        
        """
        self.edge_length = edge_length
        self.tiles = {}
        self.roads = {}
        self.buildings = {}
        # tile initialisation, https://en.wikipedia.org/wiki/Centered_hexagonal_number
        num_tiles = 3 * edge_length * (edge_length - 1) + 1
        for tile in range(num_tiles):
            self.tiles[tile] = Tile(numbers[tile], resources[tile], {})

            row_num,row_pos = self._findTileRow(tile)
            for row in [row_num, row_num + 1]:
                for j in range(3):
                    self.tiles[tile]._add_node(row, 2*row_pos + j, Node())

            print(self.tiles[tile].nodes.keys())

    def _findTileRow(self, tile_num):
        # tile count starts at 0
        # tile row starts at 0
        # how many row sizes can I fit in there? 
        if tile_num >= 3 * self.edge_length * (self.edge_length - 1) + 1:
            raise ValueError("tile number incorrect")
        curr_num = tile_num
        row_size = self.edge_length
        row_num = 0
        
        max_row_size = self.edge_length + 2
        reachedMax = False

        while curr_num >= row_size and row_size >= self.edge_length:
            row_num = row_num + 1
            curr_num = curr_num - row_size #?
            if row_size == max_row_size or reachedMax:
                row_size = row_size - 1
                reachedMax = True
            else:
                row_size = row_size + 1

        return (row_num, curr_num)   #row number, position in row

        
        

class Tile:
    def __init__(self, dice_number, resource, nodes, robber=False):
        self.dice_number = dice_number
        self.resource = resource
        self.nodes = nodes
        self.robber = robber

    def _add_node(self, row_num, row_pos, node):
        self.nodes[(row_num,row_pos)] = node

class Node:
    def __init__(self, inhabitant=None):
        self.inhabitant = inhabitant

if __name__ == '__main__':
    testboard = Board([1,2,3,4,5,6,6,5,4,3,2,1,1,2,3,4,5,6,6],
                      [1,2,3,4,5,6,6,5,4,3,2,1,1,2,3,4,5,6,6])
    
    
