fruits =  ['Apple', 'Peach','Orange','Guava','Pineapple']

for fruit in fruits:
    print(fruit)
    
#### exercise of calculating student heights

student_heights = input('Input a list of student heights \n').split()

for height in range(0, len(student_heights)):
    student_heights[height] = int(student_heights[height])
    
print(student_heights)

total = 0 
for x in range(0, len(student_heights)):
    total = total + student_heights[x]

average = round( total / len(student_heights))
print(f'average = {average}')



## program that calculates the highest score from our student list

print('WECOME TO OUR HIGHEST SCORE PROGRAM')

print(student_heights)
highest_score = 0
for score in range(0, len(student_heights)):
    if student_heights[score] > highest_score:
        highest_score = student_heights[score]

print(f'Highest score is {highest_score}')  
