# Rock , scissors and paper Game
import random

states = ['rock','scissors','paper' ]

user1_input = int(input('Type: 1 for rock, 2  for scissors, 3 for paper \n'))

computer_choice = random.randint(1, 3)
print(f' user = {states[user1_input-1]} \n computer = {states[computer_choice-1] }')


if states[user1_input-1] == 'rock' and states[computer_choice-1] == 'scissors':
    print('YOU WIN')
    
elif states[user1_input-1] == 'scissors' and states[computer_choice-1] == 'paper':
    print('YOU WIN')

elif states[user1_input-1] == 'paper' and states[computer_choice-1] == 'rock':
    print('YOU WIN')
    
elif states[user1_input-1] == 'scissors' and states[computer_choice-1] == 'rock':
    print('YOU LOSE')
    
elif states[user1_input-1] == 'paper' and states[computer_choice-1] == 'scissors':
    print('YOU LOSE')

elif states[user1_input-1] == 'rock' and states[computer_choice-1] == 'paper':
    print('YOU LOSE')

elif states[user1_input-1] == states[computer_choice-1]:
    print('YOU DRAW')