import turtle
from turtle import *
from simulation.turtlesim import InitializeEnv

#ball = Turtle()
# ball.shape("circle")
# turtle.setworldcoordinates(0,0,400,400)
screen = turtle.Screen()

screen.screensize(400,400)
screen.bgcolor("blue")
l = InitializeEnv.InitializeEnv(10, screen, 60)
ballList = l.get_ball_list()
screen.mainloop()

# screen.
# while True:
#     turtle.mainloop()

