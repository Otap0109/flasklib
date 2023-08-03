from lib import app
from flask import render_template,redirect,url_for, flash,get_flashed_messages
from lib.models import Item, User
from lib.forms import RegisterForm, LoginForm
from lib import db
from flask_login import login_user

@app.route('/')
@app.route('/home')
def homePage():
    return render_template('home.html')

@app.route('/catalogue')
def cataloguePage():
    items = Item.query.all()
    return render_template('catalogue.html', items = items )

@app.route('/register', methods=['GET','POST'])
def registerPage():
    form = RegisterForm()
    
    if form.validate_on_submit():
        user_to_create= User(username= form.username.data,
                            email= form.email.data,
                            password= form.password1.data)
        
        
    
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('cataloguePage'))
     
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(err_msg, category= 'danger')
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET','POST'])
def loginPage():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username= form.username.data).first()
        
        if attempted_user and attempted_user.check_password(
            attempted_password = form.password.data
        ):
  

            login_user(attempted_user)
            flash(f'You are now logged in as: {attempted_user.username} ',category= 'succes')
            return redirect(url_for('cataloguePage'))   

    else: 
        flash('Username or password is incorrect', category= 'danger')

    return render_template('login.html', form=form)

