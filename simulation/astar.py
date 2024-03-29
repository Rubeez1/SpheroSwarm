import math
import heapq
import itertools

class Node():
    """A node in 2D array

    Attributes:
      coords: a tuple, coordinate of this node: 
        (x coordinate, y coordinate, timestep)
        eg: (5,7,1): (5,7) at time step 1
      gcost: cost from starting node to this node
      hcost: estimated cost from current node to destination node
      fcost: gcost + hcost
      parent: node immediately preceding this node on the lowest cost path to this node

    TODO - Algorithm can infinitely loop if there is no solution. This is because timestep is considered. Need to find way to detect whether solution exist.
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

def astar(start, goal, map, constraints):
    """Performs A* algorithm from start to goal node

    Args:
      start: a Node, start position
      goal: a Node, destination
      map: list containing size of map [size of x, size of y]
      constraints: dictionary of coordinates that agent can not go to

    Returns:
        path: a list, containing coordinates in tuple from start to goal
    """
    assert type(start) == Node and type(goal) == Node             # start and goal must be Node type
    assert map[0] >= goal.coords[0] and map [1] >= goal.coords[1] # Map must be large and contain goal node

    # Set start node coords to contain timestep if it does not already contain timestep
    if len(start.coords) == 2:
        start.coords = (start.coords[0], start.coords[1], 0)

    # List of discovered nodes that may need to expaneded
    # Initially start node is added to open nodes list
    open_nodes = []
    counter = itertools.count() # counter for tie breaker when there are more than 1 equal fcost nodes
    
    # Add start to the open node list
    count = next(counter)
    heapq.heappush(open_nodes, (start.fcost, count, start))

    # Dictionary containing nodes that are already visited
    closed_nodes = {}

    # Add the start node to the closed_nodes
    closed_nodes[start.coords] = start

    while len(open_nodes) != 0:
        # Pop the node from open_nodes priority queue to get node with lowest fcost
        # current_node = open_nodes.pop(0)
        _fcost, _count, current_node = heapq.heappop(open_nodes)

        # Check if current node is the destination node, if true, return path
        if current_node.coords[0] == goal.coords[0] and current_node.coords[1] == goal.coords[1]:
            return get_path(current_node)
        
        next_nodes = get_next_nodes_with_constraints(current_node, map, constraints)

        for next_node in next_nodes:
            # Next node's gcost is current node gcost + weight of edge, which in this project is uniform 1
            next_node.gcost = current_node.gcost + 1
            
            # If next node gcost is less than gcost of previously calculated node with same coordinate, this path is better than previous path
            if next_node.coords not in closed_nodes or next_node.gcost < closed_nodes[next_node.coords].gcost:
                # Update closed nodes dictionary
                closed_nodes[next_node.coords] = next_node

                # Set cost and parent
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

def get_next_nodes_with_constraints(node, map, constraints):
    """Checks next possible nodes of input node and return list of next possible nodes

    Args:
      node: a Node, that needs next possible nodes
      map:  3-D list map with obstacle information
      contraints: dictionary of coordinates that agent can not go to

    Returns:
        next_nodes: a list, containing next possible nodes that agent can travel to from current node
    """
    next_nodes = []
    for next_step in [(0, -1, 1), (0, 1, 1), (-1, 0, 1), (1, 0, 1), (0, 0, 1)]:
        new_pos = (node.coords[0] + next_step[0], node.coords[1] + next_step[1], node.coords[2] + next_step[2])
        # Check if new pos is within the grid and Check if there is conflict
        if is_within_map(new_pos, map) and new_pos not in constraints:
            next_nodes.append(Node(new_pos))
    return next_nodes

def is_within_map(new_pos, map):
    return new_pos[0] >= 0 and new_pos[0] <= map[0] and new_pos[1] >= 0 and new_pos[1] <= map[1]

def get_hcost(node, goal):
    return math.sqrt((goal.coords[0] - node.coords[0]) ** 2 + (goal.coords[1] - node.coords[1]) ** 2) #Euclidean distance

def does_node_exist(array, node):
    for fcost, count, open_node in array:
        if open_node.coords == node.coords and open_node.gcost == node.gcost:
            return True
    return False

def test_astar():
    # Test A* algorithm with constraints
    map = [13, 13] # Initialize the map
    start = Node((0,0))
    goal = Node((7,10))
    constraints = {}
    path = astar(start, goal, map, constraints)
    print(path)

    constraints = {(0,1,1), (6,10,16)}
    path = astar(start, goal, map, constraints)
    print(path)
    


if __name__ == "__main__":
    test_astar()
