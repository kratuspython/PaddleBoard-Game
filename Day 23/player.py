from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.move_speed = MOVE_DISTANCE

    def go_up(self):
        new_y = self.ycor() + self.move_speed
        self.goto(0,new_y)

    def reset_position(self):
        self.goto(0,-280)
