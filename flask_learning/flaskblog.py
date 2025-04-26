from flask import Flask,render_template,url_for
app = Flask(__name__)

posts = [
    {
        'author':'Dummy1',
        'title':'What can i do with this?',
        'content':'First content',
        'date':'April, 2025'
    },
    {
        'author':'Dummy2',
        'title':'What cant i do with this?',
        'content':'second content',
        'date':'April, 2026'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts,title='Home')
@app.route("/about")
def about():
    return render_template('about.html',title='About')