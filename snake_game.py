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
    time.sleep(0.1)
    for seg_num in range(len(segment)-1, 0, -1):
        new_x = segment[seg_num - 1].xcor()
        new_y = segment[seg_num - 1].ycor()
        segment[seg_num].goto(new_x, new_y)
    segment[0].forward(20)

my_screen.exitonclick()
