from turtle import Turtle

class ScoreBoard(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.color('dodger blue')
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_level()
        
        
        
    def update_level(self):
        self.clear()
        self.goto(-390, 250)
        self.write('Level:', align='center', font=('Courier', 10, 'normal'))
        self.goto(-360, 250)
        self.write(self.level,align='center', font=('Courier', 10, 'normal'))
        
        
    def level_up(self):
        self.level += 1
        self.update_level()