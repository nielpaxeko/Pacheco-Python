from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        
    def left_scored(self):
        self.l_score+=1
        self.update_score()
        
    def right_scored(self):
        self.r_score+=1
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"Score = {self.l_score} | {self.r_score}", align="center", font=("Courier", 40, "normal"))
