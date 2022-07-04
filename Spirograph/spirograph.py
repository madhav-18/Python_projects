import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)


def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


tim.speed(0)


# def draw_graph(size_of_gap):
#     for i in range(int(360 / size_of_gap)):
#         tim.color(color())
#         tim.circle(100)
#         current_heading = tim.heading()
#         tim.setheading(current_heading + size_of_gap)
#
#
# draw_graph(5)

for i in range(72):
    tim.color(color())
    tim.circle(100)
    current_heading = tim.heading()
    tim.setheading(current_heading + 5)

screen = Screen()
screen.exitonclick()
