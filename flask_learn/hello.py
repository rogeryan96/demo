from flask import Flask
from flask import request,abort
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return "Hello World"

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        print request.get_json(force=True)
        print request.blueprint
        print request.endpoint
        print request.max_content_length
        return ""
    else:
        return 'show the login form'

if __name__ == '__main__':
    app.run(debug=True)