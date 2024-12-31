with open('day 026/file1.txt') as file1:
    file1_data = file1.readlines()
    
with open('day 026/file2.txt') as file2:
    file2_data = file2.readlines()
    

result = [int(number) for number in file1_data if number in file2_data]
print(result) 