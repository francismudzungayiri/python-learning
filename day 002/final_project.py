# TIP CALCULATOR 

print('WELCOME TO A TIP CALCUATOR.')

bill = float(input('What is the total bill ?\n'))
percentage = int(input('What percentag tip would you like to give? 10, 12 or 15')) 
num_people = int(input('How many peoplewould you like to split the bill with?'))

tip = (bill * percentage) / 100

total_amount =  tip + bill

splits_amount = total_amount / num_people


print(f'Each person should pay ${round(splits_amount, 2)}.')
