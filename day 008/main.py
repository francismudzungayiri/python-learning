#function without parameters or inouts
def greet():
    print('Hello')
    print('How do you do?')
    print("Isn't the weather too hot today")
        
greet()


#function with one input parameter
def greet_with_name(name):
    print(f'Hello, {name}')
    print(f'How do you do {name}?')
    print(f"{name}, isn't the weather too hot today")
        
greet_with_name('Francis')


#function with more than one parameter
def greet_with_name_and_location(name, location):
    print(f'Hello, {name}')
    print(f'How do you do {name}?')
    print(f"{name}, isn't the weather too hot today in {location}")
        
greet_with_name_and_location('Francis','Harare')