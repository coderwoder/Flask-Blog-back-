from datetime import datetime,timezone
from flask import Flask,render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '4d92f5816bda1d4bafa57beb34036069'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db= SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True,)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(150),unique=True,nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    password=db.Column(db.String(60),nullable=False)
    post=db.relationship('Post',backref='author',lazy=True)

    def __repr__(self):
        return f"User({self.username},{self.email},{self.image_file})"

class Post(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(150),nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.now(timezone.utc)) # Not the () since we don't want the (executed) time right now
    content=db.Column(db.Text,nullable=False)
    # The 'User' model will have atomatically set the table name as 'user' same for 'Post'->'post, tb_name can be changed. 
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)  

    def __repr__(self):
        return f"Post({self.title},{self.date_posted})"
    

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

@app.route("/login",methods=['POST','GET'])
def login():
    form =LoginForm()
    if form.validate_on_submit():
        if form.email.data=='admin@123.com' and form.password.data=='admin':
            flash(f'Login Successful! Welcome',category='success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful, please check your Email and Password',category='danger')
    return render_template('login.html',title='Login',form=form)

@app.route("/register",methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created For {form.username.data}! ',category='success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)