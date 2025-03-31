from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self,score):
        super().__init__()
        self.hideturtle()
        self.color('black')
        self.penup()
        self.goto(-200,260)
        self.write(f"Level: {score}", False, 'center', FONT)

    def level_refresher(self,score):
        self.clear()
        self.write(f"Level: {score}", False, 'center', FONT)

    def game_over(self,score):
        self.goto(0,0)
        self.write(f"Game Over", False, 'center', FONT)