from turtle import Turtle

MOVE_DISTANCE=10
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(270)
        self.fd(280)
        self.setheading(90)

    def go_up(self):
        self.fd(MOVE_DISTANCE)

    def starting_position(self):
        self.goto(0,-280)