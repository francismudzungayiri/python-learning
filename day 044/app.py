#Advanced python decorator function
    
class User:
    
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False
        
    
def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper    
    
    
@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is user.name's new blog post.")
        
        
new_user = User("Francis")
new_user.is_logged_in = True
create_blog_post(new_user)



from flask import Flask
import random




app = Flask(__name__)


def make_bold(func):
    def bold():
        return f'<b> {func()} </b'
    return bold

def make_em(func):
    def em():
        return f'<em> {func()} </em>'
    return em

def big_text(func):
    def biggie():
        return f'<h1 style="font-size: 30px;"> {func()} </h1>'
    return biggie



@app.route('/')
@make_bold
@make_em
@big_text
def index():
    return 'DAY 044 STARTED'

@app.route('/username/<name>')
def greetings(name):
    return f'HELLO, {name}'



@app.route('/<int:number>')
def higher_game(number):
    random_number = random.randint(1,9)
    if number == random_number:
        return 'YOU GUESSED CORRECTLY'
    
    elif number > random_number:
        return 'YOUR GUESS IS TOO HIGH'
    
    else:
        return ' YOUR GUESS IS TOO LOW'


    

if __name__ == 'main':
    app.run(debug=True)
    
    


        
