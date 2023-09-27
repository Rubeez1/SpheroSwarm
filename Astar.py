# A* pathfinding algorithm

class Node:
    def __init__(self, x, y, isEmpty):
        self.x = x
        self.y = y
        self.isEmpty = isEmpty

    def set_cost(self, g_cost):
        self.g_cost = g_cost
    
    def set_parent(self, parent):
        self.parent = parent


def get_next_nodes(map, curr_node):
    next_nodes = getAdjacent(map, curr_node.x, curr_node.y)
    for node in next_nodes:
        if(node.isEmpty == False):
            next_nodes.remove(node)
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
                v.append(arr[i + dx][j + dy])
 
 
    #Returning the vector array
    return v

# grid is map information (array of nodes for now), spheros contain the ball's initial position and destination
def find_path(grid, starting_position, destination):
    # 1. Initialize open list
    # Add starting position to the open list
    open = []
    open.append(starting_position)
    starting_position.isEmpty = False

    # 2. Initialize closed list
    close = []

    # 3. while open list is not empty
    while(len(open) != 0):
        # find node with least f on open list called q
        least_f_node = open[0]
        for node in open:
            if(least_f_node.g_cost > node.g_cost):
                least_f_node = node

        # pop the node q
        open.remove(least_f_node)

        # Generate possible next positions to nodes and set their parent to node
        get_next_nodes()

        # for each successor
            # if node is goal stop search

            # Compute f of the node

            # If the node with same position with less f is in the open list, skip

            # If the node with same posiiton is in closed list with has lower f, skip

            # add the node to open list

        # Push q to closed list
    pass

sample = Node(1,2,True)

sample.isEmpty = False

print(sample.isEmpty)