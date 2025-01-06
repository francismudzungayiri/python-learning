facebook_posts =[
    {'likes': 21, 'Comments':2},
    {'likes': 13, 'Comments':2, 'shares':1},
    {'likes': 33, 'Comments':8, 'shares': 3},
    {'Comments': 4, 'shares':2},
    {'Comments': 1, 'shares':1},
    {'likes': 19, 'Comments':3},
]

total_likes = 0
for post in facebook_posts:
    try:
        total_likes = total_likes + post['likes']
        
    except KeyError:
        total_likes += 0
    
        
        
print(total_likes)    
        