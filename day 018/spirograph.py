import turtle as t
import random as r



canvas = t.Turtle()
colors = [
    'gray', 'black','royal blue','midnight blue','sea green','saddle brown','dark slate blue','orange red'
]

canvas.speed(10)

def draw_spiralgraph(gap_size):
    for x in range(int(360 / gap_size)):
        canvas.color(r.choice(colors))
        canvas.circle(100)
        canvas.setheading(canvas.heading() + gap_size)


draw_spiralgraph(10)



screen = t.Screen()
screen.exitonclick()