from turtle import *
import random
class Ball:

    def __init__(self,number, canvas):
        self.ballList = []
        for i in range(number):
            self.ball = RawTurtle(canvas)
            self.ball.shape("circle")
            self.ball.penup()
            self.ball.setx(random.randint(-300,300))
            self.ball.sety(random.randint(-300,300))
            self.ballList.append(self.ball)


    def getBallList(self):
        return self.ballList




