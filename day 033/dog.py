

class Dog:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
    def sit(self):
        print(f"{self.name.title()} is now sitting.")
        
        
    def roll_over(self):
        print(f" {self.name.title()} rolled over.")