import pandas as pd


data = pd.read_csv('day 025/Squirrel-Data.csv')

print(data.columns) # returns data columns heading

gray_squirrel_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrel_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrel_count = len(data[data['Primary Fur Color'] == 'Black'])

print(gray_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)


#creating a dataframe 
data_dict = {
    'Fur color':['Gray', 'Cinnamon', 'Black'],
    'Count ':[gray_squirrel_count, red_squirrel_count, black_squirrel_count]    
}
df = pd.DataFrame(data_dict)

print(df)
