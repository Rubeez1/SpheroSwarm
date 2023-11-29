from turtle import *
import random
class InitializeEnv:

    def __init__(self,number, canvas, grid_size):
        self.ballList = []
        self.grid_size = grid_size
        self.factor = 1.25
        self.canvas = canvas

        for i in range(number):
            self.ball = Turtle()
            self.ball.shape("circle")
            self.ball.penup()
            x = random.randint(0,12)
            y = random.randint(0,12)

            self.ball.goto(x * self.grid_size - self.canvas.screensize()[0]//self.factor,
                           y*self.grid_size - self.canvas.screensize()[0]//self.factor)
            self.ballList.append(self.ball)
        print(type(self.canvas.screensize()))
        self.create_grid()

    def painter_ball_cors(self, turtle):
        print(self.canvas.screensize())
        turtle.setpos(self.canvas.screensize()[0]//self.factor, self.canvas.screensize[1]//self.factor)



    def get_ball_list(self):
        return self.ballList

    def draw_square(self,size,x,y,grid_turtle):              # This is only making the first
                                                             # quadrant.
        grid_turtle.penup()
        grid_turtle.speed(0)
        grid_turtle.goto(x,y)
        grid_turtle.pendown()
        for i in range(4):
            grid_turtle.forward(size)
            grid_turtle.left(90)


    def create_grid(self, cols = 12, rows = 12):
        grid_turtle = Turtle()
        for i in range(rows):
            for j in range(cols):
                y = i * self.grid_size - self.canvas.screensize()[0]//self.factor
                x = j * self.grid_size - self.canvas.screensize()[1]//self.factor
                self.draw_square(self.grid_size,x,y,grid_turtle)

    def up(self, id, squares=1):
        self.ballList[id].up(self.grid_size * squares)

    def down(self, id, squares=1):
        self.ballList[id].down(self.grid_size * squares)

    def left(self, id, squares=1):
        self.ballList[id].left(self.grid_size * squares)

    def right(self, id, squares=1):
        self.ballList[id].right(self.grid_size * squares)












