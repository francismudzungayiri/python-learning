# import csv

# with open('day 025/weather-data.csv') as data:
#     reading_lines = csv.reader(data)
#     temperature = []
#     heading = next(data) # skips the headings 
#     for row in reading_lines:
#         temp = row[1]
#         temperature.append(int(temp))
        
#     print(temperature)



#USING PANDAS TO WORK WITH CSV FILES
import pandas



data = pandas.read_csv('day 025/weather-data.csv')
# print(data['temp'])
temp = data['temp'].to_list()
print(temp)
print(data['temp'].mean())
print(data['temp'].max())



#get data in a row
print(data[data.day == 'Monday'])

#pull data that has the maximum temp
max_temp = data[data.temp == data['temp'].max()]

#covert temp to foreheight
degree = int(max_temp.temp)
forenheight = (degree * (9/5)) + 32
print(forenheight)


