from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level=1
        self.goto(-240,240)
        self.update()
        self.hideturtle()
    def update(self):

        self.write(f"level: {self.level}",False,"center",("Times New Roman",20,"normal"))

    def LevelUp(self):
        self.level+=1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",False,"center",("Times New Roman",20,"normal"))


