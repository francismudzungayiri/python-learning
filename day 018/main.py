from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('triangle')
timmy_the_turtle.color('slate blue')

#drawing a square 
for left_sqre in range(0, 4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)
    


for right_sqr in range(0,4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)
    
    

























screen = Screen()
screen.exitonclick()