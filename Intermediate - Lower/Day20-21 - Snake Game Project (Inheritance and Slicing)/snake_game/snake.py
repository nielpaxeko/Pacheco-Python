from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# Directions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            
    # Extend snake
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_body.append(new_segment)
        
    def extend(self):
        self.add_segment(self.snake_body[-1].position())
            
    
    # Move snake continously
    def move(self):
        for segment in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[segment-1].xcor()
            new_y = self.snake_body[segment-1].ycor()
            self.snake_body[segment].goto(new_x, new_y)
        self.head.forward(20)
    
    # Functions for turning snake
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
        
        