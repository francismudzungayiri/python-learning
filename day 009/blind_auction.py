import os


print('WELCOME TO BLIND AUCTION  \n\n')

bids = []

def add_bidder(name, bid_amount):
    new_bid = {}
    new_bid['name'] = name
    new_bid['amount']= bid_amount
    bids.append(new_bid)
 
 
#a function that calculates the winner from all bidders    
def calc_winner(bid_list):
    highest= {
        'person': 'name',
        'amount': 0
    }
    
    for pos in range(len(bid_list)):
        x = bid_list[pos]['amount']
        
        if highest['amount'] < x:
            highest['amount'] = x
            highest['person']= bid_list[pos]['name']
        
    print(f'The winner is {highest["person"]} , with a bid of ${highest["amount"]}')
            
    
    
next_bidder = True

while next_bidder:
    
    name = input('Enter your name: \n')
    amount = int(input('ENTER YOUR BIDDING AMOUNT \n'))
    
    add_bidder(name, amount)
    
    next_person = input('Is there anyone left to bid yes or no \n').lower()
    
    if next_person =='no':
        next_bidder = False
        calc_winner(bids)
    
    else:
        # Clearing the Screen
        os.system('cls')