from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time




screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PONG GAME')
screen.tracer(0)



paddle_1 = Paddle()
paddle_2 = Paddle()

paddle_1.right_paddle()
paddle_2.left_paddle()

ball = Ball()

score_board = ScoreBoard()

screen.listen()
#right paddle user
screen.onkey(paddle_1.move_up,'Up')
screen.onkey(paddle_1.move_down, 'Down')


#left paddle user
screen.onkey(paddle_2.move_up,'w')
screen.onkey(paddle_2.move_down, 's')



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()   #when is 0 the turtle doesnt showup so you need this for it update screen
    ball.move_ball()
    
    #detect collision with the top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #bounce  
        ball.bounce_y()
        
    #detect collision with the right paddle
    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    #right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.l_point()
        
    #left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()
    
    











screen.exitonclick()



