
def prime_checker(number):
    is_prime = True
    for x in range(2,number):
        if number % x == 0:
            is_prime= False
            
    if is_prime:
        print('Its a prime number')
    
    else:
        print('Its not a prime number')
            
            

n = int(input('Enter an integer \n'))
prime_checker(number = n)