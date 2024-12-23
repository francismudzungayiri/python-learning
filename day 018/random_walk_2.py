import turtle as t
import random



canvas = t.Turtle()
t.colormode(255)
#colors r, g, b
def get_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    return (r,g,b)
    
    
    
directions = [0, 90, 180, 270]

canvas.width(5)
for _ in range(200):
    canvas.color(get_color())
    canvas.forward(20)
    canvas.setheading(random.choice(directions))







screen = t.Screen()
screen.exitonclick()