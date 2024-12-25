from turtle import Turtle


#CONSTANTS
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:
    
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        
    
    def create_snake(self):
        x_pos = 0
        y_pos = 0


        for pos in range(3):
            canvas = Turtle(shape='square')
            canvas.color('white')
            canvas.penup()
            canvas.goto(x= x_pos, y= y_pos)
            self.snake.append(canvas)
            x_pos +=-20
            
            
            
    def move(self):
        for seg in range(len(self.snake)-1, 0, -1):
            x_cord = self.snake[seg - 1].xcor()
            y_cord = self.snake[seg - 1].ycor()
            self.snake[seg].goto(x = x_cord, y= y_cord)
        
        self.head.fd(MOVE_DISTANCE)
     
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
     
     
     
     
        
    def game_over(self):
        
        if self.head.xcor()== 280 or self.head.xcor() == -280 or self.head.ycor() == 280 or self.head.ycor() == -280:
            return True