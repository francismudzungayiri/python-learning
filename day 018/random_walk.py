from turtle import Turtle, Screen
import random

canvas = Turtle()  
canvas.width(4)


#move forward
def move_fd(timmy):
    return timmy.fd(20)

#move backwards
def move_bd(timmy):
    return timmy.bk(20)

#left movement
def move_right(timmy):
    return timmy.right(90)


#right movement
def move_left(timmy):
    return timmy.left(90)

functions = [
    move_bd, move_fd, move_right, move_left
]

colors = [
    'gray', 'black','royal blue','midnight blue','sea green','saddle brown','dark slate blue','orange red'
]

for _ in range(500):
    canvas.color(random.choice(colors))
    random.choice(functions)(canvas)
    
    












screen = Screen()
screen.exitonclick()