import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.setup(height=600, width=600)
my_screen.tracer(0)
player = Player()
cars = CarManager()

my_screen.listen()
my_screen.onkey(fun=player.up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    my_screen.update()
    cars.move_car()

my_screen.exitonclick()
