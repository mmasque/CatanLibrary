
class Board:
    def __init__(self, resource_number_pairs, edge_length=3):
        """ Make tiles with a default size of board
        - edge_length: number of tiles at an edge of the board
        """
        assert(len(resource_number_pairs) > 0)
        self.tiles = []
        self.nodes = []
        rows = []
        node_count = 0 #for node id's. They are convenient for checking equality for nodes and edges.
        for row_length in list(range(edge_length, 2 * edge_length)) + list(range(2 * edge_length - 2, edge_length - 1, -1)): # a list of the row lengths (3,4,5,4,3)
            #creates the next row 
            current_row = []
            row_narrowing = len(rows) >= edge_length
            for tile in range(row_length):
                new_tile_nodes = [0] * 6 #default value is 0. Inherits nodes from neighbours according to inhertiance rules where possible.
                if tile > 0:
                    Board.update_shared_left_nodes(new_tile_nodes, tile, current_row)
                if len(rows) > 0:
                    if tile > 0 or row_narrowing:
                        Board.update_shared_top_left_nodes(new_tile_nodes, tile, rows, row_narrowing)
                    if tile < (row_length - 1) or row_narrowing:
                        Board.update_shared_top_right_nodes(new_tile_nodes, tile, rows, row_narrowing)

                for i in range(len(new_tile_nodes)):
                    if new_tile_nodes[i] == 0: #new node is created because this node could not be inherited from existing tiles
                        new_node = Node([], node_count)
                        new_tile_nodes[i] = new_node
                        self.nodes.append(new_node)
                        node_count += 1
                

                #tile creation
                resource_number_pair = resource_number_pairs[len(self.tiles)%len(resource_number_pairs)]
                new_tile = Tile(resource_number_pair.dice_number, resource_number_pair.resource, new_tile_nodes)
                current_row.append(new_tile)
                self.tiles.append(new_tile)

                #Add edges in a cycle for each tile starting by connecting node 0 to node 1 then 1 to 2 and so on until 5 to 0
                #Note that each edge on the board is part of a tile loop. Doesn't add an edge if it already exists.
                print("----")
                for i in range(len(new_tile_nodes)):
                    start = new_tile_nodes[i]
                    end = new_tile_nodes[(i+1)%6]
                    edge = Edge(start, end)
                    if edge not in start.edges:
                        start.edges.append(edge)
                        end.edges.append(edge)

            rows.append(current_row)

    def update_shared_left_nodes(tile_nodes, tile, row):
        #left node rule. can be explained by diagram.
        tile_nodes[5] = row[-1].nodes[1]
        tile_nodes[4] = row[-1].nodes[2]
    
    def update_shared_top_left_nodes(tile_nodes, tile, rows, narrower_row):
        tile_nodes[0] = rows[-1][tile-1 + narrower_row].nodes[2]
        tile_nodes[5] = rows[-1][tile-1 + narrower_row].nodes[3]
    
    def update_shared_top_right_nodes(tile_nodes, tile, rows, narrower_row):
        tile_nodes[0] = rows[-1][tile + narrower_row].nodes[4]
        tile_nodes[1] = rows[-1][tile + narrower_row].nodes[3]

    def available_nodes(self):
        return [node for node in self.nodes if node.can_build]

class ResourceNumberPair:
    #not 100% necessary but a convenient data structure for tiles
    def __init__(self, resource, dice_number):
        self.resource = resource
        self.dice_number = dice_number

class Tile:
    def __init__(self, dice_number, resource, nodes, robber=False):
        self.dice_number = dice_number
        self.resource = resource
        self.nodes = nodes
        self.robber = robber
    
    def __str__(self):
        return str([self.resource, self.dice_number] + [str(node) for node in self.nodes])

class Node:
    def __init__(self, edges, pid=0, can_build=True, inhabitant=None):
        self.edges = edges
        self.id = pid
        self.can_build = can_build
        self.inhabitant = inhabitant
        self.edges_unlocked = True
    
    def __eq__(self, other):
        return isinstance(other, Node) and self.id == other.id

    def __str__(self):
        return str(self.id) + ":" + str([edge.end.id if edge.start == self else edge.start.id for edge in self.edges])
    
    def build(self, house):
        for edge in edges:
            edge.start.can_build = False
            edge.end.can_build = False
        self.inhabitant = house

    def potential_outgoing_roads(self, player):
        if self.can_build or self.inhabitant.isPlayer(player):
            return [edge for edge in self.edges if not edge.inhabitant_road]
        return []

    def __hash__(self):
        return self.id

class Edge:
    def __init__(self, start, end, inhabitant_road=None):
        if start.id <= end.id: #add in numerical order by id. Makes edge comparison easier
            self.start = start
            self.end = end
        else:
            self.start = end
            self.end = start
        self.inhabitant_road = inhabitant_road
    
    def __eq__(self, other):
        return self.start == other.start and self.end == other.end
    
    def __str__(self):
        return str(self.start.id) + "=>" + str(self.end.id)
    
    def __hash__(self):
        return self.__str__()


class House: 
    def __init__(self, player):
        self.player = player
        self.upgraded = False
    
    def upgrade(self):
        self.upgraded = True
    
    def isPlayer(self, player):
        return self.player == player # remember to implement __eq__ for player
    
    def get_resources(self, resource):
        self.player.add(resource)
        if self.upgraded:
            self.player.add(resource)


if __name__ == "main":
    board = Board([ResourceNumberPair("wheat", 6), ResourceNumberPair("brick", 8), ResourceNumberPair("wood", 5)])
    print([str(i) for i in board.tiles])