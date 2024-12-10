# CALCULATE NUMBER OF DAYS, WEEKS & MONTHS LEFT IF YOU ARE TO LIVE UP TO 90 YEARS OLD

age = int(input('What is your curret age? \n'))

years_left = 90 - age

days = years_left * 365

months = years_left * 12

weeks = years_left *  52

print(f'{days} days left, {weeks} weeks left, {months} months left, {years_left} years left.') 
