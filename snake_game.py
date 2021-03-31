import time
from turtle import Turtle, Screen

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("MY SNAKE GAME")
my_screen.tracer(0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]
segment = []

for position in starting_position:
    new_position = Turtle("square")
    new_position.color("white")
    new_position.penup()
    new_position.goto(position)
    segment.append(new_position)

game_is_on = True
while game_is_on:
    my_screen.update()
    for seg in segment:
        seg.forward(20)
        time.sleep(0.05)

my_screen.exitonclick()
