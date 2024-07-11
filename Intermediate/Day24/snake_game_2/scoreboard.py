from turtle import Turtle
ALIGNMENT = "center"

    
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/Users/nielpaxeko/Desktop/Programming/Python/Pacheco-Python/Intermediate/Day24/snake_game_2/data.txt") as data:
            self.high_score = data.read()
            if self.high_score == '':
                self.high_score = 0
            else:
                self.high_score = int(self.high_score)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | Highscore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode = "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
