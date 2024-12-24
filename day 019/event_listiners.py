from turtle import Turtle, Screen

canvas = Turtle()
screen = Screen()

def move_forward():
    return canvas.forward(20)

screen.listen()
screen.onkey(key = 'space', fun = move_forward)

screen.exitonclick()
