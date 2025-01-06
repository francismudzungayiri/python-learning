fruits = ['Apple', 'Pear', 'Grape']

def make_juice(index):
    fruit = fruits[index]
    print(fruit +' juice')
    

try:
    make_juice(4)
    
except IndexError:
    print(f'Max fruits we have are {len(fruits)} fruits')