### LEAP YEAR PROGRAM 


print('WECOME TO MY LEAP YEAR PROGRAM')

year = int(input('ENTER YEAR \n'))

if year % 4 == 0 or year % 400 == 0 :
    print(f'{year} is a LEAP YEAR')
    
else:
    print(f'{year}, is not a leap year')