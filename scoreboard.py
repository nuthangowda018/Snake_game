from turtle import Turtle
i=0

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,268)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"score:{self.score}", align="center", font=("arial", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game over", align="center", font=("arial", 24, "normal"))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()
