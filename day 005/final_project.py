import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','j','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 

numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','&','*','+','(',')']

num_letters = int(input('How many letters do want in your Password'))
num_numbers = int(input('How many numbers do you want'))
num_symbols = int(input('How many sysmbols do you want'))

password = []

for letter in range(0, num_letters):
    rand_letter = random.randint(0, len(letters)-1)
    password.append(letters[rand_letter])


final_password = ' '.join(password)
print(final_password)


import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','j','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 

numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','&','*','+','(',')']

num_letters = int(input('How many letters do want in your Password'))
num_numbers = int(input('How many numbers do you want'))
num_symbols = int(input('How many sysmbols do you want'))

password = []

for letter in range(0, num_letters):
    rand_letter = random.randint(0, len(letters)-1)
    password.append(letters[rand_letter])

for number in range(0, num_numbers):
    rand_number = random.randint(0, len(numbers)-1)
    password.append(letters[rand_number])

for symbol in range(0, num_symbols):
    rand_sysmbol = random.randint(0, len(symbols)-1)
    password.append(letters[rand_sysmbol])

print(password)
shuffled_password = random.shuffle(password)
final_password = ''.join(shuffled_password)

print(final_password)
    