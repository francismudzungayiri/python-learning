### program that picks a random person from a list

import random 

names = input('Enter namesof people and seperate them with a comma(,) \n')
people = names.split(',')

print(people)

random_person = random.randint(0, len(people)-1)
print (f'{people[random_person]}, is going to pay bill today')