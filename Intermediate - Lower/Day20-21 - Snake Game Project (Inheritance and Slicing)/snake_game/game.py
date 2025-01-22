from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setup game
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
game_over = False
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Allow player to control snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
      
# Start game
while not game_over:
    screen.update()
    time.sleep(.1)
    snake.move()
    # Check if snake ate food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increse_score()
    # Check of snake hit wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_over = True
        scoreboard.game_over()
    # Chech if snake ate it's own tail
    for segement in snake.snake_body[1:]:
        if snake.head.distance(segement) < 10:
            game_over = True
            scoreboard.game_over()
        
        





screen.exitonclick()