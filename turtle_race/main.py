""" You hev to guess which colour of turtle will win the forward race """

from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enetr a color:")
colors = ["blue", "purple", "orange", "red"]
y_position = [-75, 0, 75, 150]
all_turtles = []

for turtle_index in range(0, 4):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} turtle is the winner")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
