import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
soup = BeautifulSoup(response.text, 'html.parser')


movies_list = []
movies = soup.select('h2 strong')
movies_list = [movie.getText() for movie in movies]

#reversing a list 
movies_list.reverse()
print(movies_list)

with open('day 039/movies.txt', 'w') as file:
    for line in movies_list:
        file.write(f'{line} \n')
        
        
print('process finished ...... \ncheck the movies text file there is your list of top 100 movies of all time.')