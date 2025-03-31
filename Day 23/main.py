import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

score = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.tracer(0)

c = CarManager()
p = Player()
s = Scoreboard(score)

screen.listen()
screen.onkey(p.go_up, 'w')


#What ever you put inside this while loop will be repeated,updated/refresh every (0.1s)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    c.create_car()
    c.move()

    if p.ycor() > 280:
        score += 1
        s.level_refresher(score)
        p.reset_position()
        c.next_level()
    for car in c.all_cars:
        if p.distance(car) < 28:
            game_is_on = False
            s.game_over(score)


screen.exitonclick()