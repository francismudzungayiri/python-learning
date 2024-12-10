### Roller coster example 

print('WELCOME TO THE ROLLER COSTER')

height = int(input('What is your height in cm ? \n'))
bill = 0

if height > 120:
    print('You can ride the roller coster')
    age = int(input('Enter your age \n'))
    if age < 12:
        bill = 5
        print('kids charge is $5')
        
    elif age <= 18:
        bill = 7
        print('Youth charge is $7')
        
    else:
        bill = 12
        print('Adult charge is $12')
        
    wants_photo = input('Do you want some photos yes = y or no= n  \n')
    if wants_photo == 'y':
        bill = bill + 3
        print(f'YOUR TOTAL CHARGE IS ${bill}')
else:
    print('Sorry, you have to be greater than 120cm ')