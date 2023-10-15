# A* pathfinding algorithm

class Node:
    # Node class stores its position, g cost, and its parent
    def __init__(self, x, y, parent, g_cost):
        self.x = x
        self.y = y
        self.parent = parent
        self.g_cost = g_cost

    def set_f_cost(self, f_cost):
        self.f_cost = f_cost

def get_next_nodes(map, curr_node):
    next_node_coordinates = getAdjacent(map, curr_node.x, curr_node.y)
    next_nodes = []

    for node in next_node_coordinates:
        if(map[node[0]][node[1]] == True):
            # g_cost is curr_node.g_cost + 1 because distance between the nodes is equal
            next_nodes.append(Node(node[0], node[1], curr_node, curr_node.g_cost + 1))
    return next_nodes


# Function that returns all the adjacent elements from https://www.geeksforgeeks.org/find-all-adjacent-elements-of-given-element-in-a-2d-array-or-matrix/
def getAdjacent(arr, i, j):
   
    # Size of given 2d array
    n = len(arr)
    m = len(arr[0])
 
    # Initialising a vector array where
    # adjacent elements will be stored
    v = []
 
    # Checking for adjacent elements
    # and adding them to array
 
    # Deviation of row that gets adjusted
    # according to the provided position
    for dx in range (-1 if (i > 0) else 0 , 2 if (i < n) else 1):
 
        # Deviation of the column that
        # gets adjusted according to
        # the provided position
        for dy in range( -1 if (j > 0) else 0,2 if (j < m) else 1):
            if (dx is not 0 or dy is not 0):
                v.append([i + dx, j + dy])
 
 
    #Returning the vector array
    return v

# grid is map information (array of nodes for now). Each element in grid contains informtion whether sphero ball exist, thus acting as obstacle
# array containing true means a sphero ball can move to location, array containing false means sphero ball cannot move to the location
# starting position and destination will be list contain x and y for now: [x, y]
def find_path(grid, starting_position, destination):
    # 1. Initialize open list
    # Add starting position to the open list
    open = []
    h_cost = abs((starting_position.x - destination.x) ** 2 + (starting_position.y + destination.y) ** 2)
    open.append(Node(starting_position.x, starting_position.y, 0, 0))
    open[0].set_f_cost(h_cost)

    # 2. Initialize closed list
    close = []

    # 3. while open list is not empty
    while(len(open) != 0):
        # find node with least f on open list
        least_f_node = open[0]
        for node in open:
            if(least_f_node.f_cost > node.f_cost):
                least_f_node = node

        # pop the node q
        open.remove(least_f_node)

        # Generate possible next positions to nodes and set their parent to node
        next_nodes = get_next_nodes()

        # for each successor
        for node in next_nodes:
            # if node is destination stop search
            if(node.x == destination[0] and node.y == destination[1]):
                
                open.clear

            else:
                # Compute f of the node
                # h_cost calculate heuristic for moving to destination
                # h_cost is calculated with diagonal distance
                h_cost = abs((node.x - destination.x) ** 2 + (node.y + destination.y) ** 2)

                # f = g_cost (cost to move to the next_node) + h_cost (heuristic to estimate moving cost to the destination)
                f = node.g_cost + h_cost
                node.set_f_cost(f)

                # If the node with same position with larger g is in the open list, update to this node
                for open_node in open:
                    if(open_node.x == node.x and open_node.y == node.y and open_node.g_cost > node.g_cost):
                        open[index(open_node)]

                # If the node with same posiiton is in closed list with has lower f, skip

                # add the node to open list

        # Push least_f_node to closed list
        close.append(least_f_node)

        # Return updated map information and path for the sphero ball
        
    return grid, path

sample = Node(1,2)

print(sample.isEmpty)