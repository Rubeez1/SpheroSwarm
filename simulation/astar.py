import math
import heapq
import itertools

class Node():
    """A node in 2D array

    Attributes:
      coords: a tuple, coordinate of this node
      gcost: cost from starting node to this node
      hcost: estimated cost from current node to destination node
      fcost: gcost + hcost
      parent: node immediately preceding this node on the lowest cost path to this node
    """
    def __init__(self, coords):
        self.coords = tuple(coords)
        self.gcost = 0 # Cost from starting node to current node
        self.hcost = 0 # Estimated cost from current node to destination node
        self.fcost = self.gcost + self.hcost 
        self.parent = None
    def __eq__(self, other):
        return self.fcost == other
    def __gt__(self, other):
        return self.fcost > other
    def __lt__(self, other):
        return self.fcost < other
    def set_fcost(self):
        self.fcost = self.gcost + self.hcost 

def a_star(start, goal, map):
    """Performs A* algorithm from start to goal node

    Args:
      start: a Node, start position
      goal: a Node, destination
      map: 2-D list map with obstacle information, True means obstacle exists, False means obstacle does not exist

    Returns:
        path: a list, containing coordinates in tuple from start to goal
    """
    assert type(start) == Node and type(goal) == Node

    # List of discovered nodes that may need to expaneded
    # Initially start node is added to open nodes list
    open_nodes = []
    counter = itertools.count() # counter for tie breaker when there are more than 1 equal fcost nodes
    
    # Add start to the open node list
    count = next(counter)
    heapq.heappush(open_nodes, (start.fcost, count, start))

    # Map containing gcost of each node found so far
    # Each coordinate is initialized to infinite
    gcost_map = [[math.inf for col in map[0]] for row in map]

    # Set start node gcost to 0
    gcost_map[start.coords[0]][start.coords[1]] = 0

    while len(open_nodes) != 0:
        # Pop the node from open_nodes priority queue to get node with lowest fcost
        # current_node = open_nodes.pop(0)
        fcost, count, current_node = heapq.heappop(open_nodes)

        # Check if current node is the destination node, if true, return path
        if current_node.coords == goal.coords:
            return get_path(current_node)
        
        next_nodes = get_next_nodes(current_node, map) # Get next possible nodes

        for next_node in next_nodes:
            # Next node's gscore is current node gcost + weight of edge, which in this project is uniform 1
            next_node.gcost = current_node.gcost + 1
            
            # If next node gcost is less than gcost of previously calculated node with same coordinate, this path is better than previous path
            if next_node.gcost < gcost_map[next_node.coords[0]][next_node.coords[1]]:
                gcost_map[next_node.coords[0]][next_node.coords[1]] = next_node.gcost

                next_node.hcost = get_hcost(next_node, goal)
                next_node.set_fcost()
                next_node.parent = current_node

                # If next_node does not exist in open node, add to open node
                if not does_node_exist(open_nodes, next_node):
                    count = next(counter)
                    heapq.heappush(open_nodes, (next_node.fcost, count, next_node))

    return [] # Return empty path list for failure

def get_path(goal):
    """Contructs path with goal node

    Args:
      goal: a Node, containing linked parent nodes to the start node 

    Returns:
        path: a list, containing coordinates in tuple from start to goal
    """
    path = []
    while goal != None:
        path.insert(0, goal.coords)
        goal = goal.parent

    return path

def get_next_nodes(node, map):
    """Checks next possible nodes of input node and return list of next possible nodes

    Args:
      node: a Node, that needs next possible nodes
      map:  2-D list map with obstacle information

    Returns:
        next_nodes: a list, containing next possible nodes that agent can travel to from current node
    """
    next_nodes = []
    for next_step in [(0, -1), (0, 1), (-1, 0), (1, 0), (0, 0)]:
        new_pos = [node.coords[0] + next_step[0], node.coords[1] + next_step[1]]
        # Check if new pos is within the grid
        # TODO - Check if there is conflict
        if is_within_map(new_pos, map) and map[new_pos[0]][new_pos[1]] == False:
            next_nodes.append(Node(new_pos))

    return next_nodes

def is_within_map(new_pos, map):
    return new_pos[0] >= 0 and new_pos[0] <= len(map[0]) - 1 and new_pos[1] >= 0 and new_pos[1] <= len(map[0]) - 1

def get_hcost(node, goal):
    return math.sqrt((goal.coords[0] - node.coords[0]) ** 2 + (goal.coords[1] - node.coords[1]) ** 2) #Euclidean distance

def does_node_exist(array, node):
    for fcost, count, open_node in array:
        if open_node.coords == node.coords and open_node.gcost == node.gcost:
            return True
    return False

if __name__ == "__main__":

    # Test A* algorithm
    map = [[False for i in range(13)] for j in range(13)]
    start = Node((0,0))
    goal = Node((7,10))
    path = a_star(start, goal, map)
    print(path)

    start = Node((0,0))
    goal = Node((12,12))
    path = a_star(start, goal, map)
    print(path)

    start = Node((0,0))
    goal = Node((13,13))
    path = a_star(start, goal, map)
    print(path)

    for i in range(12):
        map[6][i] = True
    start = Node((0,0))
    goal = Node((12,0))
    path = a_star(start, goal, map)
    print(path)