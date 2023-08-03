from lib import db, login_manager
from lib import bcrypt
from flask_login import UserMixin
# python
# from lib import app
# from lib.models import Item,db
# app.app_context().push()
# db.session.add(item1) 
# db.session.commit()
# Item.query.all()




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable= False, unique= True)
    email = db.Column(db.String(length=50),nullable= False, unique= True)
    password_hash= db.Column(db.String(60),nullable= False)

    @property
    def password(self):
        return self.password


    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
        
        
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable= False, unique= True)
    writer = db.Column(db.String(length=30), nullable= False)
    volumes = db.Column(db.Integer(), nullable= False)

    def __repr__(self):
        return f'item {self.name}'