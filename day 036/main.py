
# word counter app 
sentence = input('Write your tweet \n')
max_char = 140


#number_of_words =  sentence.split()
#print(len(number_of_words))

num_char =[char for char in sentence]
if len(num_char) > max_char:
    exceed_num = abs(max_char - len(num_char))
    print(f'You exceed with {exceed_num}')
    
else:
    char_left = max_char - len(num_char)
    print(f'{char_left} characters left')
    


