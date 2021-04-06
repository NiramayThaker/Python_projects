import time
from turtle import Turtle, Screen
from paddel import Paddle
from ball import Ball

my_screen = Screen()
my_screen.bgcolor('Black')
my_screen.setup(800, 600)
my_screen.title("Pong")
my_screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

my_screen.listen()
my_screen.onkey(r_paddle.go_up, "Up")
my_screen.onkey(r_paddle.go_down, "Down")
my_screen.onkey(l_paddle.go_up_left, "w")
my_screen.onkey(l_paddle.go_down_left, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    my_screen.update()
    ball.move()

my_screen.exitonclick()
