import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()
screen.update()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
    # Check if turtle reach top of screen
    if player.check_finish():
        time.sleep(2)
        player.refresh()
        car_manager.speed_increase()
        score.increase_score()
        
    # Check if player hit car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            score.game_over()
            
    car_manager.reset_car()
    
screen.exitonclick()