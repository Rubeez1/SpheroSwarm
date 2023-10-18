import time
import copy
import sphere_2

"""
We have a grid. Plot all potential movements, then move the ball in the 
HIGHEST needed area (to the LOWEST needed area) to a lower concentration around it. 
    Needed:
        - dictionary (like occupancies) storing the future population of each node 
        - function to get adjacent nodes 
        - cant go to any path it has just been unless enabled. 

If both spaces are permanently occupied to in the direction of the components, 
then move backwards or something . 

"""

grid_size = 30
num_objects = 50
mol_des = "bezenine"
mol_array = [(15,10),(15,20),(10,12),(10,18),(20,12),(20,18)]

# Initialize the grid with empty nodes
grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

# Calculate the distance between a starting point and ending point 
def calculate_distance(start_pos, end_pos):
        add = pow((end_pos['x'] - start_pos['x']),2) + pow((end_pos['y'] - start_pos['y']),2)
        return pow(add, 0.5)

# Initialize the objects.
start_x = 0
start_y = 0
objects = []
for n in range(num_objects):
    if n > (num_objects / 2 - 1) and start_x == 0:
        start_x = grid_size - 1
        start_y = 0
    objects.append(sphere_2.Sphere(n, {'x': start_x, 'y': start_y}, False))
    start_y += 1
# objects = [Sphere(_, {'x': random.choice([0,grid_size - 1]), 'y': random.randint(0, grid_size - 1)}, False) for _ in range(num_objects)]

z = 0
for atom in mol_array:
    objects[z].dest = {'x': atom[0], 'y': atom[1]}
    objects[z].active = True
    z += 1

# init_dist = {}
# taken_objs = ()
# for atom in mol_array: init_dist[str(atom)] = 0
# for atom in mol_array:
#     atom_pos = {'x': atom[0], 'y': atom[1]}
#     for obj in objects:
#         prev_obj = objects[init_dist[str(atom)]]
#         old_dist = calculate_distance(prev_obj.pos, atom_pos)
#         new_dist = calculate_distance(obj.pos, atom_pos)

#         better_obj = prev_obj
#         if new_dist < old_dist: better_obj = obj

#         if not better_obj.id in taken_objs:
#             init_dist[str(atom)] = better_obj.id
#     taken_objs += (init_dist[str(atom)],)
# for atom in mol_array: 
#     atom_pos = {'x': atom[0], 'y': atom[1]}
#     objects[init_dist[str(atom)]].dest = atom_pos
#     objects[init_dist[str(atom)]].active = True

# Function to print the grid
def print_grid():
    for row in grid:
        print(' '.join(row))
    print('=' * 30 + "\n")  # Add some spacing between frames      

def clear_grid():
    for i in range(grid_size):
        for j in range(grid_size):
            grid[i][j] = ' '

def init_populations():
    populations = {}
    for i in range(grid_size):
        for j in range(grid_size):
            node = {'x': j, 'y': i}
            populations[str(node)] = 0
    return populations

def init_occupancies():
    occupancies = {}
    for obj in objects: 
        if obj.active == False:
            occupancies[str(obj.pos)] = obj.id
    return occupancies

# Main simulation loop
while True:
    # Clear the grid
    clear_grid()
    
    # populations: dictionary. Holds the possible population of each node. 
    #   key: string form of destination
    #   value: int of possible population.
    populations = init_populations()
    occupancies = init_occupancies()
    
    # plot steps and map populations 
    for obj in objects:
        if not obj.active: continue
        obj.plot_steps()
        for step in obj.steps:
            populations[str(step)] += 1

    for obj in objects:
        obj.population = populations[str(obj.pos)]
        obj.sort_steps(populations)

    # order objects by population of their location; objects in
    # higher population areas get more priority to move first
    # so that they get out of the way. 
    objects.sort(key=lambda obj: obj.population, reverse=True)
    
    for obj in objects:
        if obj.pos == obj.dest:
            obj.active = False
        if not obj.active: continue 

        this_step = None
        for step in obj.steps:
            if not str(step) in occupancies:
                final_step = step
                break
        
        if not final_step == None:
            obj.pos = copy.deepcopy(final_step)
        
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
        grid[obj.pos['y']][obj.pos['x']] = '0'
        
    # Print the grid
    print_grid()

    # Add a delay to control the simulation speed
    time.sleep(0.5)  # Adjust the sleep time as needed
