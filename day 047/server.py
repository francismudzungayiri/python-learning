from flask import Flask, render_template, request


app = Flask(__name__)


posts = []

@app.route('/')
def home():
    return render_template('blog.html', all_posts = posts)


@app.route('/add', methods=['GET', 'POST'])
def add_post():
    
    if request.method == 'POST':
        title = request.form.get('title')
        subtitle = request.form.get('subtitle')
        body = request.form.get('post_body')
        
        my_post = {
            'title': title,
            'subtitle': subtitle,
            'body': body
        }
        
        posts.append(my_post)
        print(posts)
    return render_template('add.html')
    






if __name__ == 'main':
    app.run(debug=True)
    
    