from turtle import Turtle
MOVE_DISTANCE = 20
STARTING_POSITION = (0, 0)

class Ball(Turtle):
    def __init__(self, position=()):
        super().__init__()
        position = STARTING_POSITION
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(STARTING_POSITION)
        self.bounce_x()
        self.move_speed = 0.1
