from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win th race? Enter a color: ")
colors = ["red", "orange", "green", "yellow", "blue", "purple"]
y_position = [-60, -30, 0, 30, 60]
all_turtles = []

for turtle_index in range(0, 5):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_position[turtle_index])
    new_turtle.pendown()
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Win!. The {winning_color} is the winner!.")
            else:
                print(f"You lost!. The winner was {winning_color}")

        distance = random.randint(0, 10)
        turtle.penup()
        turtle.forward(distance)
        turtle.pendown()


screen.exitonclick()