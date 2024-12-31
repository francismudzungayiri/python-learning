import pandas


data = pandas.read_csv('day 026/nato_phonetic_alphabet.csv')

code_dict = {
    row.letter: row.code for (index,row) in data.iterrows()
}
print(code_dict)

your_name = input('What is your name?')
your_name_list = [
    code_dict[letter.upper()] for letter in your_name
]
print(your_name_list)