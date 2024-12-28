from turtle import Turtle
from scoreboard import ScoreBoard
from car_manager import CarManager



PACE = 10
FINISHING_Y = 280


score_board = ScoreBoard()
car_manager = CarManager()

class Player(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('sienna')
        self.start_pos()
        self.cars_speed = 5
        

    def start_pos(self):
        self.goto(0, -280)
        self.setheading(90)
                
        
    def up_movement(self):
        new_y = self.ycor() + PACE
        self.goto(self.xcor() ,new_y)
        
        
    def crossed_successful(self):
        if self.ycor() > FINISHING_Y:
            score_board.level_up()
            car_manager.level_up()
            self.start_pos()
            