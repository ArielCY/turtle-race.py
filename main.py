from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color.") # same as input
# print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle") #tim.shape("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index]) # each turtle has different y position, create a list of y position
    all_turtles.append(new_turtle) # list of multiple turtle instances, each instance has different state.

if user_bet: # user_bet exist
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230: # 250-40/2=230
            is_race_on = False # to stop all the other turtles from moving
            # print(turtle.pencolor) # default is two color: pencolor and fillcolor
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You have won!! The {winning_color} turtle is the winner!!")
            else:
                print("You have lost!! The {winning_color} turtle is the winner!!")

        else:
            random_distance = random.randint(0, 10) # 0 & 10 are included
            turtle.forward(random_distance)

screen.exitonclick()