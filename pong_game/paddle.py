from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    # def create_line(self):
    #     self.color("White")
    #     self.left(90)
    #     self.goto(x=0, y=240)
    #     self.goto(x=0, y=-290)

    def go_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)

    def go_up_left(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def go_down_left(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)
