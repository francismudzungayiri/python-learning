## ADDING EVEN NUMBERS BETWEEN 0 TO 100 

even_sum = 0 

for  number in range(0, 101):
    if number % 2 == 0:
        even_sum += number
        
print(even_sum)
