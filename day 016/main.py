class User:
    
    def __init__(self, username, id_num):
        self.name = username
        self.id = id_num
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User('francis', 4012)
user2 = User('Natasha', 7896)

user1.follow(user2)


print(f'{user1.name} = {user1.following}')
print(f'{user2.name} = {user2.following}')