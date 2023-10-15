import time
import copy
import math
import sphere

grid_size = 30
num_objects = 50
mol_des = "bezenine"
mol_array = [(15,10),(15,20),(10,12),(10,18),(20,12),(20,18)]

# Initialize the grid with empty nodes
grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

class AStarNode:
    def __init__(self, parent=None, pos=None):
        self.pos = pos
        self.parent = parent
        self.g = 0 #step cost
        self.h = 0 #heuristic cost (cost to move to destination)
        self.f = 0 #total cost

        
# plan: given a sphere object, use astar to find the best path to destination, and give that path as an array.
def astar(sphere, occupancies):
    openList = [] #possible locations
    closedList = [] #not possible locations to go to
    startNode = AStarNode(None, [sphere.pos['x'], sphere.pos['y']])
    startNode.g = startNode.h = startNode.f = 0
    endNode = AStarNode(None, [sphere.dest['x'], sphere.dest['y']])
    endNode.g = endNode.h = endNode.f = 0
    openList.append(startNode)
    
    while(len(openList) > 0):
        currNode = openList[0]
        currInd = 0
        # Find the node with smalleset f cost
        for i, node in enumerate(openList): #basically just a i=1;i<len(openList);i++ for loop to keep trakc of the index and item
            if node.f < currNode.f:
                currNode = node
                currInd = i
        
        # pop the smallest f cost node
        openList.pop(currInd)
        closedList.append(currNode)
        
        # If the node is destination, return the path
        if currNode == endNode:
            path = []
            curr = currNode
            while curr is not None:
                path.append(curr.pos)
                curr = curr.parent #basically recursivesly moves back to start from end
            return path[::-1] #reverses path
    
        #generates neighbor nodes
        children = []
        for nextStep in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            newPos = currNode.pos[0] + nextStep[0], currNode.pos[1] + nextStep[1]
            if newPos[0] > (len(grid) - 1) or newPos[0] < 0 or newPos[1] > (len(grid[len(grid)-1]) -1) or newPos[1] < 0: #checks to make sure not out of bounds
                continue
            if str(newPos) in occupancies: #checks to make sure not occupied
                continue
            newNode = AStarNode(currNode, newPos)
            children.append(newNode)
        
        for child in children:
            for closedChild in closedList:
                if child == closedChild:
                    continue
                #ignore child, since already in closed list (visited
            child.g = currNode.g + 1
            child.h = endNode.pos[0] - child.pos[0] + endNode.pos[1] - child.pos[1] #manhattan distance
            child.f = child.g + child.h
            
            for openNode in openList:
                if child == openNode and child.g > openNode.g: #looking for lowest cost node
                    continue
            
            openList.append(child)
            
        

# Calculate the distance between a starting point and ending point 
def calculate_distance(start_pos, end_pos):
        add = pow((end_pos[0] - start_pos[0]),2) + pow((end_pos[1] - start_pos[1]),2)
        return pow(add, 0.5)

# Initialize the objects.
start_x = 0
start_y = 0
objects = []
for n in range(num_objects):
    if n > (num_objects / 2 - 1) and start_x == 0:
        start_x = grid_size - 1
        start_y = 0
    objects.append(sphere.Sphere(n, {'x': start_x, 'y': start_y}, False))
    start_y += 1

# objects = [Sphere(_, {'x': random.choice([0,grid_size - 1]), 'y': random.randint(0, grid_size - 1)}, False) for _ in range(num_objects)]

# allocate molecules to move; set destination to benzine
# for i in range(len(mol_array)):
#     objects[i].dest['x'] = mol_array[i][0]
#     objects[i].dest['y'] = mol_array[i][1]
#     objects[i].active = True
objects[37].dest = {'x': mol_array[2][0], 'y': mol_array[2][1]}
objects[37].active = True
objects[12].dest = {'x': mol_array[4][0], 'y': mol_array[4][1]}
objects[12].active = True
objects[43].dest = {'x': mol_array[3][0], 'y': mol_array[3][1]}
objects[43].active = True
objects[18].dest = {'x': mol_array[5][0], 'y': mol_array[5][1]}
objects[18].active = True
objects[0].dest = {'x': mol_array[0][0], 'y': mol_array[0][1]}
objects[0].active = True
objects[1].dest = {'x': mol_array[1][0], 'y': mol_array[1][1]}
objects[1].active = True

# occupancies: dictionary. Holds all occupied spaces
#   key: string form of destination
#   value: id of object occupying that area
occupancies = {}
for obj in objects: 
    occupancies[str(obj.pos)] = obj.id

# Calculate path for each spheros
for obj in objects:
    if (obj.active):
        obj.path = astar(obj, occupancies)

# Function to print the grid
def print_grid():
    for row in grid:
        print(' '.join(row))
    print('=' * 30 + "\n")  # Add some spacing between frames        

# Main simulation loop
while True:
    # Clear the grid
    for i in range(grid_size):
        for j in range(grid_size):
            grid[i][j] = ' '
    
    # occupancies: dictionary. Holds all occupied spaces
    #   key: string form of destination
    #   value: id of object occupying that area
    occupancies = {}
    for obj in objects: 
        occupancies[str(obj.pos)] = obj.id
    
    # Move and update the objects
    for obj in objects:
        if not obj.active: continue     # skip if inactive object

        # plot out future path
        obj.update_step()

        # change path if intended destination is taken
        if str(obj.step) in occupancies:
            obj.remap_step(occupancies, grid_size)

        # remove object from current location
        del occupancies[str(obj.pos)]
        
        # change object position
        obj.pos = copy.deepcopy(obj.step)
        if obj.pos == obj.dest: 
            obj.active = False

        # add object to new location
        occupancies[str(obj.pos)] = obj.id
                
    # Break from loop if all objects in position
    fin_count = 0
    for obj in objects:
        if not obj.active:
            fin_count += 1
    if fin_count == num_objects:
        break

    # Place objects on the grid
    for obj in objects:
        grid[obj.pos['y']][obj.pos['x']] = str(obj.id)
        
    # Print the grid
    print_grid()

    # Add a delay to control the simulation speed
    time.sleep(0.5)  # Adjust the sleep time as needed
