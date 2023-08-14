from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("PONG")
screen.tracer(0)

paddle1 = Paddle(350, 0)
paddle2 = Paddle(-350, 0)
ball = Ball()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(paddle1.go_up, 'Up')
screen.onkey(paddle1.go_down, 'Down')
screen.onkey(paddle2.go_up, 'w')
screen.onkey(paddle2.go_down, 's')

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # Detect collision with top and bottom walls
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect collision with the paddle
    if ball.xcor()>= 320 and ball.distance(paddle1)< 50 or ball.xcor() <= -320 and ball.distance(paddle2)< 50:
        ball.bounce_x()


    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_point()



screen.exitonclick()
