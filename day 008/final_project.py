alphabet = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

    
def cesar(text, shift, direction):
    plan_message = ''
    new_pos = 0
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            if direction == "encode":
                new_pos = position + shift
            else:
                new_pos = position - shift
            new_letter =  alphabet[new_pos]
            plan_message += new_letter       
        else:
            plan_message +=char    
    
    print(plan_message)
    




should_continue = True

while should_continue:
    
    direction = input('Type encode to encrypt, type decode to decoode the message. \n')
    text = input('Type your message. \n').lower()
    shift = int(input('Type the shift number: \n'))    
    
    shift = shift % 26 
    cesar(text, shift, direction)
    prog_continue = input('DO YOU WANT TO CONTINUE TYPE YES OR NO \n')
    if prog_continue == 'no':
        should_continue = False
        print('GOODBYE')