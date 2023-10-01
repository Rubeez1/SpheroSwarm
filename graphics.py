import pygame
import random

# speed of simulation
speed = 5
grid_size = 30
num_objects = 50
mol_des = "bezenine"
bez_array = [
    (15, 10, "carbon"),
    (15, 20, "carbon"),
    (10, 12, "carbon"),
    (10, 18, "carbon"),
    (20, 12, "carbon"),
    (20, 18, "carbon"),
    (15, 5, "hydrogen"),
    (5, 10, "hydrogen"),
    (5, 20, "hydrogen"),
    (15, 25, "hydrogen"),
    (25, 20, "hydrogen"),
    (25, 10, "hydrogen"),
]

glu_array = [
    (3,14,"oxygen"),
    (1,16,"hydrogen"),
    (6,16,"carbon"),
    (7,14, "hydrogen"),
    (7,18,"hydrogen"),      
    (9,14,"carbon"),
    (10,16,"hydrogen"),
    (12,16,"carbon"),
    (15,14,"carbon"),
    (18,16,"carbon"),
    (21,14,"carbon"),
    (24,16,"oxygen"),
    (9,10,"oxygen"),
    (8,8,"hydrogen"),
    (12,20,"oxygen"),
    (15,10,"oxygen"),
    (18,20,"oxygen"),
    (11,14,"hydrogen"),
    (14,17,"hydrogen"),
    (17,14,"hydrogen"),
    (22,13,"hydrogen"),
    (16,8,"hydrogen"),
    (11,22,"hydrogen"),
    (17,22,"hydrogen"),

]

acetone_array = [
    (15, 11, "oxygen"),
    (15, 15, "carbon"),
    (11, 17, "carbon"),
    (19, 17, "carbon"),

    (11, 19, 'hydrogen'),
    (10, 18, "hydrogen"),
    (10, 16, "hydrogen"),

    (19, 19, "hydrogen"),
    (20, 18, "hydrogen"),
    (20, 16, "hydrogen"),

]
mol = acetone_array
# Initialize the grid with empty nodes
grid = [[" " for _ in range(grid_size)] for _ in range(grid_size)]

# Initialize the objects with random positions. Random Y coordinate but x coordinate is either left or right
objects = [
    {
        "x": random.choice([0, grid_size - 1]),
        "y": random.randint(0, grid_size - 1),
        "atom": "",
    }
    for _ in range(num_objects)
]
print(objects)
# objects = [{'x': 0, 'y': 0} for _ in range(num_objects)]

# for _ in range(num_objects):
#    {'x': random.choice([0,grid_size]), 'y': random.randint(0, grid_size - 1)
t = 0
for i in objects:
    i["destination"] = (objects[t]["x"], objects[t]["y"])
    t = t + 1
t = 0

for i in mol:
    objects[t]["atom"] = i[2]
    objects[t]["destination"] = i
    t = t + 1

# pygame setup
pygame.init()
screen = pygame.display.set_mode((900, 900))
clock = pygame.time.Clock()
running = True


# resizes the coordinates to pixels for plotting in pygame
def resizecoord(x, y, gridx=30, gridy=30, screenx=900, screeny=900):
    xFactor = 900 / 30
    yFactor = 900 / 30
    return (x * xFactor, y * yFactor)


# carbon atom draw function
def carbon(x, y, screen):
    pygame.draw.circle(screen, (0, 0, 0), (x, y), 15)


# hydrogen atom draw function
def hydrogen(x, y, screen):
    pygame.draw.circle(screen, (255, 255, 255), (x, y), 15, 1)

def oxygen(x, y, screen):
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 15, 0)


# move function by step of 1
def move(obj):
    x = 0
    y = 0
    dir_vector = (obj["destination"][0] - obj["x"], obj["destination"][1] - obj["y"])
    if dir_vector[0] > 0:
        x = 1
    elif dir_vector[0] < 0:
        x = -1
    if dir_vector[1] > 0:
        y = 1
    elif dir_vector[1] < 0:
        y = -1
    return x, y


# moves any atoms that are out of the grid to the closest border
def inbound(obj):
    x = obj["x"]
    y = obj["y"]
    if obj["x"] < 0:
        x = 0
    elif obj["x"] > grid_size - 1:
        x = grid_size - 1
    if obj["y"] < 0:
        y = 0
    elif obj["y"] > grid_size - 1:
        y = grid_size - 1
    return x, y


# game loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((100, 100, 100))  # RENDER YOUR GAME HERE

    for obj in objects:
        print(obj)
        print("new set")
        if obj["atom"] == "carbon":
            carbon(
                resizecoord(obj["x"], obj["y"])[0],
                resizecoord(obj["x"], obj["y"])[1],
                screen,
            )
        elif obj["atom"] == "hydrogen":
            hydrogen(
                resizecoord(obj["x"], obj["y"])[0],
                resizecoord(obj["x"], obj["y"])[1],
                screen,
            )
        elif obj["atom"] == "oxygen":
            oxygen(
                resizecoord(obj["x"], obj["y"])[0],
                resizecoord(obj["x"], obj["y"])[1],
                screen,
            )
        obj["x"] += move(obj)[0]
        obj["y"] += move(obj)[1]
        obj["x"], obj["y"] = inbound(obj)
        print(obj)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(5)  # limits FPS to 60

pygame.quit()
