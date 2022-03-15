# Turtle Race Program

import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=700, height=500)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? "
                                   "\nEnter a colour (violet/indigo/blue/green/yellow/orange/red): ").lower()
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_positions = [-90, -60, -30, 0, 30, 60, 90]
all_turtles = []

# Create 7 turtles
for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-330, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    # Check for the winning turtle
    for turtle in all_turtles:
        if turtle.xcor() > 330:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # Make each turtle move a random amount.
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
