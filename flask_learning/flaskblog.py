from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '4d92f5816bda1d4bafa57beb34036069'

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

@app.route("/login")
def login():
    form =LoginForm()
    return render_template('login.html',title='Login',form=form)

@app.route("/register",methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created For {form.username.data}! ',category='success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)