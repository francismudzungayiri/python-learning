import random

print('WELCOME TO BLACKJACK GAME. \n\n')

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
bank = 1000
computer = []
my_cards = []



def getCard():
    dealer_first_card = random.randint(0, len(cards)-1)
    return cards[dealer_first_card]

#GETTING COMPUTER CARDS
computer.append(getCard())

# GETTING USER CARDS
for x in range(0, 2):
    my_cards.append(getCard())
    
def score_sum(card_score):
    total = 0
    for value in card_score:
            total += value
    
    return total

def get_deal():
    computer.append(getCard())
    my_cards.append(getCard())
    
    comp_total = score_sum(computer)
    user_total = score_sum(my_cards)
    
    return comp_total, user_total
    


def hit_deal():
    computer.append(getCard())
    comp_total = score_sum(computer)
    user_total = score_sum(my_cards)
    
    return comp_total, user_total        


def find_winner(user_total, comp_total):
    if user_total > 21 or comp_total > 21:
        if comp_total > 21:
            print('YOU WIN')
        else:
            print('YOU LOSE')
    
    elif user_total > comp_total:
        print('YOU WIN')

    elif user_total == comp_total:
        print('THATS A DRAW ')
        
    else:
        print('YOU LOSE')
    
    print(f'DEALER CARDS ARE  {computer}')
    print(user_total, comp_total)
    
       
plays = input('DO YOU WANT TO PLAY THE: type \n yes or no : ')
if plays =='no':
    print('GOODBYE')
    
else:
    print(f'YOU HAVE {bank}')
    #dealer_amount = input('How much do you want to bet 1, 5, 10, 20, 50, 100')
    print(f'YOUR CARDS ARE: {my_cards}')
    print(f'DEALER CARDS ARE: {computer}')
    
    #hit or deal 
    stop_game = input('tpye hit to stop or deal to continue \n')
    if stop_game == 'hit':
        comp, human = hit_deal()
        find_winner(human, comp)
    else:
        comp, human = get_deal()
        find_winner(human, comp)