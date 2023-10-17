from turtle import *
import random
class InitializeEnv:

    def __init__(self,number, canvas):
        self.ballList = []
        for i in range(number):
            self.ball = Turtle()
            self.ball.shape("circle")
            self.ball.penup()
            x = random.randint(-400,400);
            y = random.randint(-400,400);
            # self.ball.setx(random.randint(-300,300))
            # self.ball.sety(random.randint(-300,300))
            self.ball.goto(x,y)
            self.ballList.append(self.ball)
        self.create_grid()



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


    def create_grid(self, cols = 10, rows = 10, size = 40):
        grid_turtle = Turtle()
        for i in range(rows):
            for j in range(cols):
                y = i * size
                x = j * size
                self.draw_square(size,x,y,grid_turtle)







