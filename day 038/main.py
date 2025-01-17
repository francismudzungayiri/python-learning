class Car:
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
        
    def display_info(self):
        print(f'This is {self.brand} {self.model}')
        
        
tesla = Car('Tesla', 'model S')
tesla.display_info()

mazda = Car('Mazda', 'Atenza')
mazda.display_info()



class Dog:
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
        
    def bark(self):
        print(f'{self.name} is barking.')
        
        
        
rex = Dog('Rex', 'Mongroo') 
rex.bark()

boky = Dog('Boky', 'German Shepard')
boky.bark()
       