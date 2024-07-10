from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Ping Pong Game")
screen.tracer(0)

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()
score = Scoreboard()
game_over = False
screen.update()

# Right paddle commands
screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

while not game_over:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()
    
    # Check if ball hit ceiling or floow
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()
    # Check if ball hit either side
    if ball.xcor() >= 380: # right
        time.sleep(2)
        score.left_scored()
        ball.refresh()
    elif ball.xcor() <= -380: # left
        time.sleep(2)
        score.right_scored()
        ball.refresh()
    # Check if ball hit paddle
    if (ball.distance(right_paddle) <= 50 and ball.xcor() == 320) or (ball.distance(left_paddle) <= 50 and ball.xcor() == -320):
        ball.paddle_bounce()
        
        

screen.exitonclick()