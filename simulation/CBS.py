import astar

class CBS_Node():
    """A CBS node in binary tree

    Attributes:
      constraints: a list, contraints of agents at certain time step
      longest_cost: longest cost of an agent cost
      total_cost: sum of all costs of agents
      solution: Solution path of this CBS node
    """
    def __init__(self):
        self.constraints = []
        self.longest_cost = 0
        self.total_cost = 0
        self.solution = None
    
    def __eq__(self, other):
        return self.longest_cost == other
    def __gt__(self, other):
        return self.longest_cost > other
    def __lt__(self, other):
        return self.longest_cost < other

def CBS(agents):
    """Performs CBS algorithm

    Args:
      agents: a 2-D list, each list in agents contain an agent which contains start and goal node

    Returns:
        path: a 2-D list, containing list of coordinates in tuple from start to goal for each agent
    """
    # Create start CBS_Node with no contraints and find solution
    start = CBS_Node()

    
    # Insert start CBS_Node to the Open heap

    # While Open is not empty
        # Pop 'P' the CBS_Node with the least cost

        # Validate path and check if conflict exists

        # If CBS_Node has no conflict, return P

        # Else, for each agent in conflict
            # Create a new CBS_Node

            # Add a new constraint with this agent

            # Set the solution by invoking low level algorithm

            # Set the cost

            # Insert into Open heap
    
    return None # Return none if no solution exists

# Get input constraint
def get_agents_path(agents):
    path = []
    for agent in agents:
        # Calculate map that accounts constraint
        map = get_constraint_map()
        path.append(astar.astar(agent[0], agent[1], map))
    return

# TODO - apply constraint to the map
# Is this neccessary?
def get_constraint_map(constraint):

    map = [[False for i in range(13)] for j in range(13)]

    return map