number = int(input('Which number do you want to check\n'))

if number % 2 == 0:
    print(f'{number} is an even digit')
else:
    print(f'{number} is an odd number')
    
    
### The code produce an syntax error because it wasn't doing a comparison check but 
# doing  an assignment by = instead of equal to (==) 