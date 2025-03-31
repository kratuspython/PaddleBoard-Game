from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

l_score = 0
r_score = 0



screen = Screen()
screen.setup(800,600)
screen.bgcolor('black')
screen.title("Ping Pong Game")
screen.tracer(0)

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()
score= Scoreboard(l_score,r_score)


screen.listen()
screen.onkey(r_paddle.go_up,'Up')
screen.onkey(r_paddle.go_down,'Down')
screen.onkey(l_paddle.go_up,'w')
screen.onkey(l_paddle.go_down,'s')

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.1)
    #Detect collition between ball and wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()
    #Detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()
    #Detect out of bounds
    if ball.xcor() > 380:
        l_score+=1
        score.refreher(l_score,r_score)
        ball.reset_position()
    elif ball.xcor() < -380:
        r_score += 1
        score.refreher(l_score,r_score)
        ball.reset_position()



screen.exitonclick()