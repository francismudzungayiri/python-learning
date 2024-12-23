from turtle import Turtle, Screen
import random

colors = [
    'gray', 'black','royal blue','midnight blue','sea green','saddle brown','dark slate blue','orange red'
]


# #drawing a  triangle
# triangle = Turtle()
# triangle.color(random.choice(colors))
# for _ in range(3):    
#     triangle.forward(50)
#     triangle.right(360 / 3)

# #drawing a square
# square = Turtle()
# square.color(random.choice(colors))
# for _ in range(4):
#     square.fd(50)
#     square.right(360 / 4)
    
# #drawing a pentagon
# pentagon = Turtle()
# pentagon.color(random.choice(colors))
# for _ in range(5):
#     pentagon.fd(50)
#     pentagon.right(360 / 5)

# #drawing a hexaagon
# hexa = Turtle()
# hexa.color(random.choice(colors))
# for _ in range(6):
#     hexa.fd(50)
#     hexa.right(360 / 6)
    
# #drawing a heptagon
# hep = Turtle()
# hep.color(random.choice(colors))
# for _ in range(7):
#     hep.fd(50)
#     hep.right(360 / 7)

# #drawing a octagon
# octagon = Turtle()
# octagon.color(random.choice(colors))
# for _ in range(8):
#     octagon.fd(50)
#     octagon.right(360 / 8)

# #drawing an nanogon
# nano = Turtle()
# nano.color(random.choice(colors))
# for _ in range(9):
#     nano.fd(50)
#     nano.right(360 / 9)


# #drawing an decagon
# deca = Turtle()
# deca.color(random.choice(colors))
# for _ in range(10):
#     deca.fd(50)
#     deca.right(360 / 10)
    
canvas = Turtle()

def draw_shape(number_of_sides):
    angle = 360 / number_of_sides
    for _shape in range(number_of_sides):
        canvas.fd(50)
        canvas.right(angle)
        

for _num in range(3, 11):
    canvas.color(random.choice(colors))
    draw_shape(_num)
    



screen = Screen()
screen.exitonclick()

