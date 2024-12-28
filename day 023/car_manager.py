from turtle import Turtle
import random


COLORS = ['black', 'slate gray', 'steel blue', 'orange red', 'slate blue', 'orange','green']
MOVEDISTANCE = 5

class CarManager:
    
    
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVEDISTANCE
        
    
    def create_car(self):
        random_chance = random.randint(1, 10)
        if random_chance == 1:
            new_car = Turtle('square') 
            new_car.penup()
            new_car.shapesize(stretch_wid=1.0, stretch_len=2.0)
            new_car.color(self.car_color())
            random_y = random.randint(-150, 150)
            new_car.goto(450, random_y)
            self.all_cars.append(new_car)
        
        
        
        
    def car_color(self):
        color = random.choice(COLORS)
        return color
    
    
    def car_movement(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            
            
    def level_up(self):
        self.car_speed += MOVEDISTANCE 