from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    
    def __init__(self):
        super().__init__()
        self.cars = []
        self.create_cars()
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def create_cars(self):
        for i in range (30):
            new_car = Turtle()
            rand_color = random.choice(COLORS)
            new_car.shape("square")
            new_car.penup()
            new_car.setheading(180)
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(rand_color)
            new_car.goto(self.random_position())
            self.cars.append(new_car)
        
    def speed_increase(self):
        self.car_speed += MOVE_INCREMENT
        
    def move_cars(self):
        for car in self.cars:
            new_x = car.xcor() - self.car_speed
            car.goto(new_x, car.ycor())
            
    def reset_car(self):
        for car in self.cars:
            if car.xcor() <= -320:
                car.goto(self.random_position())
                
    def random_position(self):
        y_values = list(range(-260, 260, 25))
        x_values = list(range(280, 800, 20))
        return (random.choice(x_values), random.choice(y_values))
    
    
        