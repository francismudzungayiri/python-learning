sentence = 'What is the airspeed velocity of an unladen swallow'

words = sentence.split()

num_letters = {
    word : len(word) for word in words
}
print(num_letters)