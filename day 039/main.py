from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/newest')
soup = BeautifulSoup(response.text, 'html.parser')


articles = []
links = []
votes = []


articles_text = soup.select(selector='.titleline a')
for article in articles_text:
    text = article.get_text() 
    link = article['href'] #  OR      article_text.get('href')
    
    articles.append(text)
    links.append(link)
    
    
votes = [int(vote.get_text().split()[0]) for vote in soup.find_all(name='span', class_ = 'score')]

# print(articles)
# print(links)
# print(votes)

# highest = 0
# index = 0
# x = 0
# while x < len(votes):
#     if votes[x] > highest:
#         highest = votes[x]
#         index = x
#     x += 1
        
highest_vote = max(votes)
highest_vote_index = votes.index(highest_vote)



print(articles[highest_vote_index])
print(links[highest_vote_index])
print(f'VOTES: {highest_vote}')
        

 
