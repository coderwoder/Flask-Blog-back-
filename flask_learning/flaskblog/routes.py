from flask import render_template,url_for,flash,redirect,request
from flaskblog import app,bcrypt,db,login_manager
from flask_login import login_user,logout_user,current_user,login_required
from flaskblog.models import User,Post
from flaskblog.forms import RegistrationForm, LoginForm

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form =LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            next_page= request.args.get('next') #args-> dict, hence better to accessed with get() then [k,v]; Will return None or a key 
            print(next_page) 
            flash(f'Login Successful! Welcome {user.username }',category='success') 
            # if the user accesses the account page through URL it will redirect it to the 'account' 
            # and if through normal login it will redirect it to the home page.
            return redirect(next_page) if next_page else redirect(url_for('home')) 
        else:
            flash(f'Login Unsuccessful, please check your Email and Password',category='danger')
    return render_template('login.html',title='Login',form=form)

@app.route("/register",methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_pw=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,password=hashed_pw,email=form.email.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account Created For {form.username.data}! You can now Log in',category='success')
        return redirect(url_for('login'))
    return render_template('register.html',title='Register',form=form)

@app.route("/logout")
def logout():
   logout_user()
   return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html',title='Account')