from turtle import Screen
from player import Player
import time
from car_manager import CarManager






screen = Screen()
screen.bgcolor('white')
screen.title('Turtle Crossing Game')
screen.setup(width=900, height=600)
screen.tracer(0)



player = Player()


screen.listen()
screen.onkey(player.up_movement, 'Up')


cars = CarManager()


game_over =False
while not game_over:
    screen.update()
    time.sleep(0.1)
    cars.create_car()
    cars.car_movement()
    player.crossed_successful()
    
    
    # detect collision with a car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_over = True
    










screen.exitonclick()