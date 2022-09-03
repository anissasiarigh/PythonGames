from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()

    def create_paddle(self, position ,color):
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color(color)
        self.penup()
        self.goto(position)
        self.speed("fastest")

    def move_up(self):
        y_cor = self.ycor() + 25
        self.goto(self.xcor(), y_cor)

    def move_down(self):
        y_cor = self.ycor() - 25
        self.goto(self.xcor(), y_cor)