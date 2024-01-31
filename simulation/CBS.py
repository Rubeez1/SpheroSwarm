import astar
import heapq
import itertools

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
    
    def calculate_longest_cost(self):
        longest_cost = 0
        for path in self.solution:
            if longest_cost > len(path):
                longest_cost = len(path)
        self.longest_cost = longest_cost
    
    def calculate_total_cost(self):
        total_cost = 0
        for path in self.solution:
            total_cost += len(path)
        self.total_cost = total_cost

def CBS(agents):
    """Performs CBS algorithm

    Args:
      agents: a 2-D list, each list in agents contain an agent which contains start and goal node

    Returns:
        path: a 2-D list, containing list of coordinates in tuple from start to goal for each agent
    """
    # Create start CBS_Node with no contraints and find initial paths
    start = CBS_Node()
    start.solution = get_agents_path(agents)
    start.calculate_longest_cost()
    start.calculate_total_cost()
    
    # Initialzie heap
    open = []
    counter = itertools.count() # counter for tie breaker when there are more than 1 equal longest or total_cost nodes

    # Insert start CBS_Node to the Open heap
    count = next(counter)
    heapq.heappush(open, (start.longest_cost, start.total_cost, count, start))

    # While Open is not empty
    while len(open) != 0:
        # Pop 'P' the CBS_Node with the least cost
        _ , _ , _ , current_node = heapq.heappop(open)

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
    agent_path = []
    for agent in agents:
        # Calculate map that accounts constraint
        agent_path.append(astar.astar(agent[0], agent[1], map))
    return agent_path

# Detect if conflict exist
def detect_conflict(agent_paths):
    # Detect if two agents occupy same space at same time

    # Detect if two agents switch position

    # Return first found conflict
    return