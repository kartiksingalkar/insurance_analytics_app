from app.models.users_model import User
from app import db

def create_user(email, password, role, mobile):
    new_user = User(email=email, password=password, role=role, mobile=mobile)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def get_all_users():
    return User.query.all()

def check_password(user, password):
    return user.password == password
