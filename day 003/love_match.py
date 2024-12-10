# LOVE MATCHING PROGRAM


name1 = input(" BOYFRIEND'S NAME \n")
name2 = input(" GIRLFRIEND'S NAME  \n")

combined_name = name1 + name2

lower_case = combined_name.lower()

t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")

true_word = str(t + r + u + e)

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")

love_word = str( l + o + v + e)

love_score = true_word + love_word

love_score = int(love_score)

if love_score <= 10 or love_score >= 90:
    print(f'Your score is {love_score},you go togetner like coke and mentos')
    
elif love_score >= 40 and love_score <=50:
    print(f'Your score is {love_score}, you are alright together')

else:
    print(f'Your score is {love_score}')