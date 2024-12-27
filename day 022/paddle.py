from turtle import Turtle

MOVE_DISTANCE = 20



class Paddle(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_len=1.0, stretch_wid=5.0)
        
        
        
    def right_paddle(self):
        self.goto(350, 0)
    
    def left_paddle(self):
        self.goto(-350, 0)    
    
    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor() ,new_y)
        
        
    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor() ,new_y)
        