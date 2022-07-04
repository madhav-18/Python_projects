# from turtle import Turtle,Screen
#
# bud = Turtle()
#
# bud.shape("triangle")
# bud.color("dark slate gray")
#
# for i in range(4):
#     bud.left(90)
#     bud.forward(100)
#
#
# screen = Screen()
# screen.exitonclick()


# import turtle
#
# tim = turtle.Turtle()
#
# """OR"""
#
#
# from turtle import Turtle
#
# tim = Turtle()
# tom = Turtle()
# import turtle as t

# def draw_shape(number_of_sides):
#     angle = 360 / number_of_sides
#     for i in range(number_of_sides):
#         tim.fd(100)
#         tim.right(angle)
#
#
# for shape_side in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side)

# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

""" Random Walk"""
import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)
# colors = ["royal blue", "Black", "red", "orange", "dark magenta", "hot pink", "lime green", "dark green",
#         "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
tim.pensize(5)
tim.speed(0)
for i in range(200):
    tim.forward(30)
    tim.setheading(random.choice(directions))
    tim.color(random_color())

screen = Screen()
screen.exitonclick()
