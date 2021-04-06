from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):

        new_x = self.xcor() + 5
        new_y = self.ycor() + 5
        self.goto(x=new_x, y=new_y)
        if new_x >= 350 <= new_y:
            print("Game over")
