import random
from game_data import data

print('HIGHER OR LOWER GAME \n\n')


def get_data():
    number = random.randint(0, len(data) -1)
    return data[number]

def print_question(a, b):
    comparison_a = f"Compare A: {a['name']}, {a['description']}, {a['country']}"
    comparison_b = f"Compare B: {b['name']}, {b['description']}, {b['country']}"
    print(f'{comparison_a} \n vs \n {comparison_b}')
    
score = 0
def comparison(a, b, user):
    a_followers = a['follower_count']
    b_followers = b['follower_count']
    
    global score
    global comp_a
    global comp_b
    global play_game
    
    if user == 'a':
        if a_followers > b_followers:
            score +=1 
            comp_a = comp_b
            comp_b = get_data()
            
        else:
            play_game = False
    
    elif user == 'b':
        if b_followers > a_followers:
            score +=1
            comp_a = comp_b
            comp_b = get_data()
        else:
            play_game = False
            
    else:
        print('Invalid input')
    


comp_a = get_data()
comp_b = get_data()
play_game = True

while play_game:
    #if account a = account while is true so it continues to check until they are no longer equal
    while  comp_a == comp_b:
        comp_b = get_data()
        
    print_question(comp_a, comp_b)    
    user_input = input('Whi has more followers? Type A or B').lower()
    comparison(comp_a, comp_b, user_input)
    
    
print(f'Your score is {score}')

