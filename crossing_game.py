from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from score import ScoreBoard
screen=Screen()
screen.setup(600,600)
screen.tracer(0)

player=Player()
car=CarManager()
score_board=ScoreBoard()

screen.listen()
screen.onkey(player.go_up,"Up")

is_game_on=True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move()

    for cars in car.all_cars:
        if cars.distance(player)<20:
            is_game_on=False
            score_board.game_over()
    if player.ycor()>290:
        player.starting_position()
        car.level_up()
        score_board.LevelUp()



screen.exitonclick()