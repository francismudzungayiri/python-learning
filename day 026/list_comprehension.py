numbers = [1,2,3,4,5,6]
#increase each number by 3 inside that list
new_numbers = [n+3 for n in numbers]
print(new_numbers)


#seperate from a name
my_name =  'Francis'
name_letters = [letter for letter in my_name]
print(name_letters)

#multiply each number by 2 inthe specifyed range

doub_numbers = [num*2 for num in range(1,5)]
print(doub_numbers)

#conditional comprehension
names = ['Alex','Beth','Francis','Natasha','Dave','Eleanor','Fraddie']
cap_names = [name.upper() for name in names if len(name) > 5]
print(cap_names)