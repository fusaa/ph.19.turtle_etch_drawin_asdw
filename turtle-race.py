from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(500,500)

turtles = []
turtle_colors = ('red', 'green', 'blue', 'pink', 'black')

bet_invalid = True
while bet_invalid:
    user_bet = screen.textinput("Make bet:", "Turtle:")
    for a in range(len(turtle_colors)):
        if user_bet.lower() == turtle_colors[a]:
            bet_invalid = False


y_pos = -50
for x in range(5):
   turtles.append(Turtle(shape='turtle'))
   turtles[x].penup()
   turtles[x].color(turtle_colors[x])
   y_pos += 30
   turtles[x].goto(-200,y_pos)

race_is_on = True
while race_is_on:
    for x in range(len(turtles)):
        turtles[x].forward(random.randint(1,10))
        if turtles[x].xcor() > 200:
            print(f"winner is {turtle_colors[x]}")
            winner = turtle_colors[x]
            if user_bet.lower() == winner:
                print("YOU WON!")
            else:
                print("Sorry, you lost. You can always try again.")
            race_is_on = False

screen.exitonclick()
