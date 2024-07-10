from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(0, 0)
        self.x_dir = 10
        self.y_dir = 10
        self.move_speed = .1
        
    def move(self):
        new_x = self.xcor() + self.x_dir
        new_y = self.ycor() + self.y_dir
        self.goto(new_x, new_y)
    
    def bounce(self):
        self.y_dir *= -1
    
    def paddle_bounce(self):
        self.x_dir *= -1
        self.move_speed *= .75
        
    def refresh(self):
        self.goto(0, 0)
        self.move_speed = .1
        self.paddle_bounce()