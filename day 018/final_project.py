import turtle as t
import random



def get_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    return (r,g,b)

t.colormode(255)
canvas = t.Turtle()



canvas.setheading(255)
canvas.forward(100)
canvas.setheading(0)

number_of_dots = 100


for dots in range(1, number_of_dots):
    canvas.dot(20, get_color())
    canvas.fd(50)
    
    if dots % 10 == 0:
        canvas.setheading(90) 
        canvas.forward(50)
        canvas.setheading(180)
        canvas.forward(500)







screen = t.Screen()
screen.exitonclick()