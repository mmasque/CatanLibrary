class ResourceNumberPair:
    def __init__(self, resource, dice_number):
        self.resource = resource
        self.dice_number = dice_number

class Board:
    def __init__(self, resource_number_pairs, edge_length=3):
        """ Make tiles with a default size of board
        - edge_length: number of tiles at an edge of the board
        """
        assert(len(resource_number_pairs) > 0)
        self.tiles = []
        rows = []
        node_count = 0
        for row_length in range(edge_length, 2 * edge_length):
            current_row = []
            for tile in range(row_length):
                new_tile_nodes = [0] * 6
                if tile > 0:
                    Board.update_shared_left_nodes(new_tile_nodes, tile, current_row)
                if len(rows) > 0:
                    if tile > 0:
                        Board.update_shared_top_left_nodes(new_tile_nodes, tile, rows, False)
                    if tile < (row_length - 1):
                        Board.update_shared_top_right_nodes(new_tile_nodes, tile, rows, False)

                for i in range(len(new_tile_nodes)):
                    if new_tile_nodes[i] == 0:
                        new_tile_nodes[i] = Node([], node_count)
                        node_count += 1
                resource_number_pair = resource_number_pairs[node_count%len(resource_number_pairs)]
                new_tile = Tile(resource_number_pair.dice_number, resource_number_pair.resource, new_tile_nodes)
                current_row.append(new_tile)

            rows.append(current_row)
            self.tiles += current_row

        for row_length in range(2 * edge_length - 2, edge_length - 1, -1):
            current_row = []
            for tile in range(row_length):
                new_tile_nodes = [0] * 6
                if tile > 0:
                    Board.update_shared_left_nodes(new_tile_nodes, tile, current_row)
                
                Board.update_shared_top_left_nodes(new_tile_nodes, tile, rows, False)
                Board.update_shared_top_right_nodes(new_tile_nodes, tile, rows, False)
                for i in range(len(new_tile_nodes)):
                    if new_tile_nodes[i] == 0:
                        new_tile_nodes[i] = Node([], node_count)
                        node_count += 1
                resource_number_pair = resource_number_pairs[len(self.tiles%len(resource_number_pairs)]
                new_tile = Tile(resource_number_pair.dice_number, resource_number_pair.resource, new_tile_nodes)
                current_row.append(new_tile)

            rows.append(current_row)
            self.tiles += current_row

    def update_shared_left_nodes(tile_nodes, tile, row):
        tile_nodes[5] = row[-1].nodes[1]
        tile_nodes[4] = row[-1].nodes[2]
    
    def update_shared_top_left_nodes(tile_nodes, tile, rows, narrower_row):
        tile_nodes[0] = rows[-1][tile-1 + narrower_row].nodes[2]
        tile_nodes[5] = rows[-1][tile-1 + narrower_row].nodes[3]
    
    def update_shared_top_right_nodes(tile_nodes, tile, rows, narrower_row):
        tile_nodes[0] = rows[-1][tile + narrower_row].nodes[4]
        tile_nodes[1] = rows[-1][tile + narrower_row].nodes[3]

class Tile:
    def __init__(self, dice_number, resource, nodes, robber=False):
        self.dice_number = dice_number
        self.resource = resource
        self.nodes = nodes
        self.robber = robber
    
    def __str__(self):
        return str([self.resource, self.dice_number] + [str(node) for node in self.nodes])

    #def _add_node(self, )

    #def get_node(self, )
class Node:
    def __init__(self, edges, id=0, inhabitant=None):
        self.edges = edges
        self.id = id
        self.inhabitant = inhabitant
    
    def __str__(self):
        return str(self.id)

class Edge:
    def __init__(self, starting_node, ending_node, inhabitant_road):
        self.starting_node = starting_node
        self.ending_node = ending_node
        self.inhabitant_road = inhabitant_road

board = Board([ResourceNumberPair("wheat", 6), ResourceNumberPair("brick", 8), ResourceNumberPair("wood", 5)])
print([str(i) for i in board.tiles])