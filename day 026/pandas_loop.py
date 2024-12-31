import pandas 


student_dict = {
    'students': ['Francis', 'Natasha', 'Tinashe'],
    'scores':[89, 65, 76]
}

student_df = pandas.DataFrame(student_dict)
print(student_df)