from turtle import Turtle, Screen
import random



screen = Screen()
screen.setup(width=700, height=500)

colors = ['red','orange','yellow','green','blue','purple']
all_turtles = []
is_race_on = False

x_pos = -330
y_pos = 210
for turtle_creation in range(6):
    canvas = Turtle(shape='turtle')
    canvas.color(colors[turtle_creation])
    canvas.penup()
    canvas.goto(x= x_pos, y= y_pos)
    all_turtles.append(canvas)
    y_pos -= 70
    
user_bet = screen.textinput(title='Make a bet', prompt='Which Turtle will win the race? Enter color!')
winner_list = []

if user_bet:
    is_race_on = True
    
while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        
        if turtle.xcor() == 300:
            is_race_on = False
            winner = turtle.fillcolor()
            if  winner == user_bet:
                print('YOU WON $500, GREAT GUESs')
                
            else:
                print(f'YOU LOST,[ {winner} is the winner ], TRY AGAIN ')


    



screen.exitonclick()