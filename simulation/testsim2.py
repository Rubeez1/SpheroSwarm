import random
import time

grid_size = 30
num_objects = 50
mol_des = "bezenine"
bez_array = [(15,10),(15,20),(10,12),(10,18),(20,12),(20,18)]
# Initialize the grid with empty nodes
grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

# Initialize the objects with random positions. Random Y coordinate but x coordinate is either left or right 
objects = [{'x': random.choice([0,grid_size - 1]), 'y': random.randint(0, grid_size - 1), 'active': 0} for _ in range(num_objects)]

# Set initial destinations to current position
t = 0
for i in objects:
    i["destination"] =  (objects[t]["x"], objects[t]["y"])
    t = t + 1

# allocate molecules to move; set destination to benzine
t = 0
for i in bez_array:
    objects[t]["destination"] = i
    objects[t]["active"] = 1
    t = t + 1

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

    fin_count = 0    # Count the number of inactive objects
    # note: occupancies doesn't do anythign yet 
    occupancies = [[False]*grid_size] * 2    # log occupancies

    # Move and update the objects
    for obj in objects:
        # skip if inactive object
        if (obj["active"] == 0):
            fin_count += 1
            continue

        # Move in direction of destination
        dir_vector = (obj["destination"][0] - obj["x"], obj["destination"][1] - obj["y"])
        if (dir_vector[0] + dir_vector[1] == 0):
            obj["active"] = 0
            fin_count += 1
            continue
        
        # Update the object's position based on the chosen direction
        if dir_vector[0] > 0:
            obj['x'] += 1
        if dir_vector[0] < 0:
            obj['x'] -= 1
        if dir_vector[1] > 0:
            obj['y'] += 1
        if dir_vector[1] < 0:
            obj['y'] -= 1
            
        #check if object is out of bounds, if so, set it to the edge
        if obj['x'] < 0:
            obj['x'] = 0
        if obj['x'] > grid_size - 1:
            obj['x'] = grid_size - 1
        if obj['y'] < 0:
            obj['y'] = 0
        if obj['y'] > grid_size - 1:
            obj['y'] = grid_size - 1

        occupancies[0][obj['x']] = True
        occupancies[1][obj['y']] = True
    
    # Break from loop if all objects in position
    if (fin_count == num_objects):
        break

    # Place objects on the grid
    # print(objects)
    for obj in objects:
        grid[obj['y']][obj['x']] = 'O'

    # Print the grid
    print_grid()

    # Add a delay to control the simulation speed
    time.sleep(0.5)  # Adjust the sleep time as needed
