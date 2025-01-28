from flask import Flask, render_template
import datetime
import requests


app = Flask(__name__)



@app.route('/')
def index():
    
    date = datetime.datetime.now()
    year = date.year
    
    return render_template('index.html', this_year = year)


@app.route('/guess/<name>')
def guess(name):
    
    age_response = requests.get(f'https://api.agify.io?name={name}')
    gender_response = requests.get(f'https://api.genderize.io?name={name}')
        
    age_data = age_response.json()
    get_age = age_data["age"]
        
    geander_data =gender_response.json()
    get_gender =geander_data["gender"]
        
    print(get_age, get_gender)

    return render_template('profile.html', age = get_age, gender = get_gender)


@app.route('/blogs')
def blog():
    url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(url)
    all_posts = response.json()
    
    return render_template('blog.html', all_posts = all_posts)




@app.route('/blogs/<int:num>')
def read_blog(num):
    
    url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(url)
    all_posts = response.json()
    
    post = all_posts[num-1]

    return render_template('read_blog.html', blogpost = post)







if __name__ == 'main':
    app.run(debug=True)