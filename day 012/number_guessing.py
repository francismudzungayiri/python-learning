import random

print('WELCOME TO THE NUMBER GUESSING GAME')
print('I AM THINKING OF A NUMBER BETWEEN 1 TO 100')

game_level = input('Choose difficulty type easy or hard \n').lower() # getting user inputs

# a function that generates a random number between 1 to 100
def get_number():
    return random.randint(1,100)


    
    
def play_game(computer_guess, game_attempts):
    
    for attempt in range(game_attempts):
        print(f'You have {game_attempts} attempts remaining to guess the number.')
        guess = int(input('Make 1 guess:  '))
        
        if game_attempts > 0:
            if guess > computer_guess:
                print('Too high')
                game_attempts-=1
        
            elif guess == computer_guess:
                print('Congrats you guessed correctly....... You win')
                break
        
            else:
                print('Too low')
                game_attempts -=1
        else:
            print('YOU HAVE RAN OUT CHANCES ....OOPS YOU LOSE')


choosen_number = get_number()
if game_level == 'easy':
    easy_attempts = 10
    play_game(choosen_number, easy_attempts)
    
elif game_level == 'hard':
    hard_attempts = 5
    play_game(choosen_number, hard_attempts)
    
else:
    print('oops check your spellings')
    

    