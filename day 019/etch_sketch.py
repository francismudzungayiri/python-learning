from turtle import Turtle, Screen


canvas = Turtle()
screen = Screen()

#move forward the turtle
def move_forward():
    canvas.fd(10)
    
#move backwards
def move_backwards():
    canvas.bk(10)
    

#turn left by 10 degrees
def turn_left():
    canvas.left(10)

#turn right by 10 degrees
def turn_right():
    canvas.right(10)


#clear the drawings 
def clear_drawings():
    canvas.clear()
    canvas.penup()
    canvas.home()
    canvas.pendown()




screen.listen()
screen.onkey(move_forward, 'w')
screen.onkey(move_backwards, 's')
screen.onkey(turn_left, 'a')
screen.onkey(turn_right, 'd')
screen.onkey(clear_drawings, 'c')



screen.exitonclick()