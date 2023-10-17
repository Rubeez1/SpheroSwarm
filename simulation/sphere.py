import copy

# Calculate the distance between a starting point and ending point 
def calculate_distance(start_pos, end_pos):
        add = pow((end_pos['x'] - start_pos['x']),2) + pow((end_pos['y'] - start_pos['y']),2)
        return pow(add, 0.5)

# SPHERE CLASS
class Sphere:
    def __init__(self, id, pos, active, path = None, path_idx = 0):
        # object ID: int    
        #   assigned by order of initialization
        self.id = id
        # object's current position: dictionary of {'x': x, 'y': y}
        self.pos = copy.deepcopy(pos)
        # if the object has finished moving: boolean 
        self.active = active
        # object's end destination: dictionary of {'x': x, 'y': y}
        self.dest = copy.deepcopy(pos)
        # object's next immediate movement: dictionary of {'x': x, 'y': y}
        self.step = copy.deepcopy(pos)
        # object's path calculated using Astar and index to track the step
        self.path = path
        self.path_idx = path_idx
    
    def __str__(self):
        return f"{self.id} {self.pos} {self.dest} {self.active}"
    
            
    # CREATE AN INITIAL NEXT STEP
    # This is the most direct path towards the objet's destination.
    # It disregards all objects around it, aka whether its path
    # is currently occupied. 
    def update_step(self):
        # sets the step to the current position 
        self.step = copy.deepcopy(self.pos)
        
        # increments x value towards the destination 
        if self.dest['x'] > self.pos['x']:
            self.step['x'] += 1
        elif self.dest['x'] < self.pos['x']: 
            self.step['x'] -= 1

        # increments y value towards the destination 
        if self.dest['y'] > self.pos['y']:
            self.step['y'] += 1
        elif self.dest['y'] < self.pos['y']:
            self.step['y'] -= 1 


    # REMAPS THE NEXT STEP 
    # This function is intended to be called if the most direct step
    # is occupied and the step needs to be remapped. It takes into 
    # consideration the objects around it. 
    def remap_step(self, occupancies, grid_size):
        # possible_steps: all of the viable locations the robot can move to,
        # mapped to keys that record the distance of each step to the destination.
        # dictionary of {'distance to object': {corresponding step information}}
        possible_steps = {}

        # generate possible locations around the robot.
        # the change in x can range between -1 and 1, and  
        # the change in y can range between -1 and 1. 
        for delta_x in range(-1, 2):
                for delta_y in range(-1, 2):

                    # apply the change in y and change in x
                    possible_step = {'x': self.pos['x'] + delta_x, 
                                     'y': self.pos['y'] + delta_y}

                    # CONDITIONALS MAKING THIS LOCATION INVALID
                    # there is no change in x or y
                    if delta_x == 0 and delta_y == 0:
                        continue
                    # the location is out of bounds 
                    if (possible_step['x'] >= grid_size or
                        possible_step['x'] < 0 or
                        possible_step['y'] >= grid_size or
                        possible_step['y'] < 0):
                        continue
                    # the location is occupied 
                    if str(possible_step) in occupancies.keys(): 
                        continue
                    # eliminate x directions opposite to the destination
                    if self.step['x'] > 0 and delta_x < 0: continue 
                    if self.step['x'] < 0 and delta_x > 0: continue
                    # eliminate y directions opposite to the destination
                    if self.step['y'] > 0 and delta_y < 0: continue 
                    if self.step['y'] < 0 and delta_y > 0: continue

                    # add new location to the possible_steps dictionary, mapped
                    # to a key representing its distance from the destination
                    distance = calculate_distance(possible_step, self.dest)
                    possible_steps[str(distance)] = possible_step
        
        # there are no available positions 
        if len(possible_steps) == 0:
            # the step is set equal to the current position so
            # the object does not move
            self.step = copy.deepcopy(self.pos)
            return
        
        # set the object's step to the location that has the least 
        # distance from its final destination
        self.step = possible_steps[str(min(possible_steps.keys()))]
