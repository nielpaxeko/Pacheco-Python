from turtle import Turtle

FONT = ("Courier", 10, "normal")

class Marker(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(0, 0)
      
    def write_state(self, state, coordinates):
        self.goto(coordinates)
        self.write(f"{state}", align="center", font=FONT)