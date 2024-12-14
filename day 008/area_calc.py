
import math

def paint_calc(height, width, coverage):
    result = (height * width) / coverage
    result = math.ceil(result)   #math.ceil() is used to round up the number to the nearest whole number
    print(f"You will need {result} cans of paint")
    
    
    
test_h = int(input('Height of wall: \n'))
test_w = int(input('Width of wall: \n'))
coverage = 5


paint_calc(height=test_h, width=test_w, coverage=coverage)