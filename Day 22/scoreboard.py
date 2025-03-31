from turtle import Turtle

ALIGN = "center"
FONT = ("gameplay",40,"normal")


class Scoreboard(Turtle):
    def __init__(self,score_l,score_r):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.goto(-100, 240)
        self.write(f"{score_l}",False,ALIGN,FONT)
        self.goto(100, 240)
        self.write(f"{score_r}", False, ALIGN, FONT)

    def refreher(self,score_l,score_r):
        self.clear()
        self.goto(-100, 250)
        self.write(f"{score_l} ", False, ALIGN, FONT)
        self.goto(100, 250)
        self.write(f"{score_r}", False, ALIGN, FONT)