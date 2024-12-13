import random 

word_list = ['ardvark','baboon','camel']

#randomly choose a word and assign to a variable called chosen_word
chosen_word = random.choice(word_list)    #word_list[random.randint(1, 3)-1]
print(chosen_word)


display = []
for letter in chosen_word:
    display.append('_')
    
print(display)

lives  = 6
while '_' in display:
    if lives > 0:
        guess = input('Guess a letter \n').lower()
        for pos in range(len(display)): 
            letter = chosen_word[pos]
            if guess == letter:
                display[pos] = guess

        if guess not in display:
            lives -=1
        
        if '_' not in display:
            print('YOU WIN')   
            
    
        print(display)   
        print(f'{lives} lives left')
        
        
    else:
        print('HANGED: GAME OVER') 
        break
            
        


