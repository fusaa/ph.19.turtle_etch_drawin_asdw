from turtle import Turtle,Screen

turtle = Turtle()
screen = Screen()

def forward():
    turtle.forward(10)

def right():
    turtle.right(10)

def left():
    turtle.left(10)

def backward():
    turtle.backward(10)

def clear():
    turtle.clear()

screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=clear)
screen.listen()





screen.exitonclick()