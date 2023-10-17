import time
import copy
import sphere

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
    objects.append(sphere.Sphere(n, {'x': start_x, 'y': start_y}, False))
    start_y += 1
# objects = [Sphere(_, {'x': random.choice([0,grid_size - 1]), 'y': random.randint(0, grid_size - 1)}, False) for _ in range(num_objects)]

init_dist = {}
taken_objs = ()
for atom in mol_array: init_dist[str(atom)] = 0
for atom in mol_array:
    atom_pos = {'x': atom[0], 'y': atom[1]}
    for obj in objects:
        prev_obj = objects[init_dist[str(atom)]]
        old_dist = calculate_distance(prev_obj.pos, atom_pos)
        new_dist = calculate_distance(obj.pos, atom_pos)

        better_obj = prev_obj
        if new_dist < old_dist: better_obj = obj

        if not better_obj.id in taken_objs:
            init_dist[str(atom)] = better_obj.id
    taken_objs += (init_dist[str(atom)],)
for atom in mol_array: 
    atom_pos = {'x': atom[0], 'y': atom[1]}
    objects[init_dist[str(atom)]].dest = atom_pos
    objects[init_dist[str(atom)]].active = True

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
        if obj.pos == obj.dest:
            obj.active = False
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
        grid[obj.pos['y']][obj.pos['x']] = '0'
        
    # Print the grid
    print_grid()

    # Add a delay to control the simulation speed
    time.sleep(0.5)  # Adjust the sleep time as needed
