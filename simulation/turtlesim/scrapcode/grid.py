import turtle

# Set up the Turtle screen
screen = turtle.Screen()
screen.setup(width=400, height=400)

# Create a Turtle object
grid_turtle = turtle.Turtle()

# Function to draw a square at a given position
def draw_square(x, y, size):
    grid_turtle.penup()
    grid_turtle.goto(x, y)
    grid_turtle.pendown()
    grid_turtle.speed(0)
    for _ in range(4):
        grid_turtle.forward(size)
        grid_turtle.right(90)



# Grid parameters
grid_size = 100
num_rows = 4
num_cols = 4

# Draw the grid of squares
for row in range(num_rows):
    for col in range(num_cols):
        x = col * grid_size
        y = row * grid_size
        draw_square(x, y, grid_size)

# Close the window on click
screen.exitonclick()
