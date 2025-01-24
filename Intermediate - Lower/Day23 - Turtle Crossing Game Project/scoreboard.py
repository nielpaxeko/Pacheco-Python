from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(0, 250)
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Level : {self.level}", align="center", font=FONT)
        
    def increase_score(self):
        self.level+=1
        self.update_score()
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
