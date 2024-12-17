print('WELCOME TO OUR PYTHON CALCULATOR \n\n')



#addition
def add(n1, n2):
    return n1 + n2

#subtraction
def subtract(n1, n2):
    return n1 - n2

#multiplication
def multiply(n1, n2):
    return n1 * n2


#division
def division(n1, n2):
    return n1 / n2


operations = {
    '+':  add,
    '-':  subtract,
    '*':  multiply,
    '/':  division,
}

def calculator():
    num1 = float(input('ENTER NUM1 \n'))
    for symbol in operations:
        print(symbol)

    next_calculation = True
    while next_calculation:    
        operation_symbol = input('Pick an operation from the line above. \n')
        num2 = float(input('ENTER NUM2 \n'))
        operational_function = operations[operation_symbol]    
        answer = operational_function(num1, num2)
        print(f'{num1} {operation_symbol} {num2} = {answer}')
        
        #next calculation
        next_calc = input(f'Type yes to continue calculating with {answer} or no to exit \n')
        if next_calc == 'no':
            next_calculation = False
            calculator()
            
        num1 = answer
        
        
        
calculator()
    