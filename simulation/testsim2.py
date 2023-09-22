import random
import time

grid_size = 30
num_objects = 50
mol_des = "bezenine"
bez_array = [(15,10),(15,20),(10,12),(10,18),(20,12),(20,18)]
# Initialize the grid with empty nodes
grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

# Initialize the objects with random positions. Random Y coordinate but x coordinate is either left or right 
objects = [{'x': random.choice([0,grid_size - 1]), 'y': random.randint(0, grid_size - 1)} for _ in range(num_objects)]

# objects = [{'x': 0, 'y': 0} for _ in range(num_objects)]

#for _ in range(num_objects):
#    {'x': random.choice([0,grid_size]), 'y': random.randint(0, grid_size - 1)
t = 0
for i in objects:
    i["destination"] =  (objects[t]["x"],objects[t]["y"])
    t = t + 1
t = 0

for i in bez_array:
    objects[t]["destination"] = i
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

    # Move and update the objects
    for obj in objects:
        # Randomly choose a direction
        dir_vector = (obj["destination"][0] - obj["x"],obj["destination"][1]-obj["y"])
        print(dir_vector)
        
        # Update the object's position based on the chosen direction
        if dir_vector[1] > 0 and obj['y'] != :
            obj['y'] += 1
        if dir_vector[1] < 0:
            obj['y'] -= 1
        if dir_vector[0] < 0:
            obj['x'] += 1
        if dir_vector[0] > 0:
            obj['x'] -= 1
            
        #check if object is out of bounds, if so, set it to the edge
        if obj['x'] < 0:
            obj['x'] = 0
        if obj['x'] > grid_size - 1:
            obj['x'] = grid_size - 1
        if obj['y'] < 0:
            obj['y'] = 0
        if obj['y'] > grid_size - 1:
            obj['y'] = grid_size - 1

    # Place objects on the grid
    # print(objects)
    for obj in objects:
        #print(obj['y'])
        #print(obj['x'])    
        grid[obj['y']][obj['x']] = 'O'

    # Print the grid
    print_grid()

    # Add a delay to control the simulation speed
    time.sleep(0.5)  # Adjust the sleep time as needed
