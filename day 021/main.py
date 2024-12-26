from turtle import Screen
import time
from snake import Snake
from food import Food



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)


#instance of classes
snake = Snake()
food = Food()



screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')



game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    #detect food collision
    if snake.head.distance(food) < 13:
        food.refresh()
    
    
    
    game_over = snake.game_over()




screen.exitonclick()
