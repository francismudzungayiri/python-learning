#### Range function 

# range(start, stop, step)
#find the sum between 0 to 100

sum = 0
for number in range(0, 101):  # why 101 because it excludes 101 so it end at 100
    sum += number

print(sum)