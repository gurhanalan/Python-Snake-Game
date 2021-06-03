from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.num_of_segments = 3
        self.segments = []
        for i in range(self.num_of_segments):
            new_turtle = Turtle(shape="square")
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.goto(-20 * i, 0)
            self.segments.append(new_turtle)
        self.head = self.segments[0]

    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(15)

    def extend(self):

        # add a new segment to the snake
        new_turtle = Turtle(shape="square")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.goto(self.segments[-1].position())
        self.segments.append(new_turtle)

    # def is_collision(self):
    #     for segment in self.segments:
    #         if self.head == segment:
    #             pass
    #         elif self.head.distance(segment) < 10:
    #             return True
    #         else:
    #             return False

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
