import turtle
import pandas as pd 

screen = turtle.Screen()
screen.title('US States Game')
img_path = "day 025/blank_states_img.gif"

screen.addshape(img_path)
turtle.shape(img_path)


# def get_mouseclick_cor(x,y):
#     print(x, y)
    

# turtle.onscreenclick(get_mouseclick_cor)



guesed_states = []
data = pd.read_csv('day 025/50_states.csv')
states = data.state.to_list()


while len(guesed_states) < 50:
    answer = screen.textinput(title='Gues the state', prompt="What's another states name")


    if answer == 'exit':
        break
    
    
    if answer.title() in states:
        guesed_states.append(answer.title())
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        
        get_state = data[data.state  == answer.title()]
        x_cor = int(get_state['x'])
        y_cor = int(get_state['y'])
        
        t.goto(x_cor, y_cor)
        t.write(answer.title())




 