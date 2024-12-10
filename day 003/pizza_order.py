### THIS IS A PIZZA ORDER PROGRAM

print ('WELCOME TO PYTHON PIZZA DELIVERIES') 
bill = 0

size = input('What size of a pizza do you want? S, M, L \n')
add_pepperoni = input('Do you pepperoni? y or n \n')
add_extra_cheese = input('Do you want extra cheese? y or n \n')

if size =='s':
    bill = 15
    
elif size == 'm':
    bill = 20
    
elif size == 'l':
    bill = 25
    
else:
    print(' next customer please ')
    
if add_extra_cheese == 'y':
    bill = bill + 1
    
if add_pepperoni == 'y':
    if size == 's':
        bill = bill + 2
    else:
        bill = bill + 3

print(f' YOUR FINAL BILL IS ${bill}')
