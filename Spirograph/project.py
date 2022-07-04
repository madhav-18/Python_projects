# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 45)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     colour = (r, g, b)
#     rgb_colors.append(colour)
#
# print(rgb_colors)

import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202),
              (112, 139, 141), (254, 194, 0)]
tim.hideturtle()
tim.setheading(225)
tim.penup()
tim.forward(350)
tim.pendown()
tim.setheading(0)
tim.showturtle()
tim.speed(0)

for _ in range(10):
    for i in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.fd(50)
        tim.pendown()

    tim.hideturtle()
    tim.setheading(90)
    tim.penup()
    tim.fd(50)
    tim.pendown()
    tim.setheading(180)
    tim.penup()
    tim.fd(500)
    tim.pendown()
    tim.right(180)
    tim.showturtle()


screen = Screen()
screen.exitonclick()
