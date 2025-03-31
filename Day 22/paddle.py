from turtle import Turtle

VELOCITY = 20

class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.color('white')
        self.penup()
        self.shapesize(5, 1)
        self.goto(x,y)

    def go_up(self):
        new_y = self.ycor() + VELOCITY
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - VELOCITY
        self.goto(self.xcor(), new_y)
