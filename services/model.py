from flask_sqlalchemy import SQLAlchemy
from database import db
import random, string


def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String, unique=True, nullable=False)
    token = db.Column(db.String, nullable=False)

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    role = db.relationship('Role', backref=db.backref('users', lazy=True))

    def insert(self):
        if self.role is None:
            self.role = get_role("user")
        self.token = randomword(25)
        db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()


service_tag=db.Table('service_tag',
                    db.Column('service_id', db.Integer,db.ForeignKey('services.id'), nullable=False),
                    db.Column('tag_id',db.Integer,db.ForeignKey('tags.id'),nullable=False),
                    db.PrimaryKeyConstraint('service_id', 'tag_id') )


class Service(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    region = db.Column(db.String)
    size = db.Column(db.String)
    image = db.Column(db.String)
    ssh_keys = db.Column(db.String)
    backups = db.Column(db.Boolean)
    ipv6 = db.Column(db.Boolean)
    user_data = db.Column(db.String)
    private_networking = db.Column(db.String)
    volumes = db.Column(db.String)

    #user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    #user = db.relationship('User', backref=db.backref('services', lazy=True))

    tags=db.relationship('Tag', secondary=service_tag, backref='services' )

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()

class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String, unique=True, nullable=False)

def get_user(login_name, role_name=None, auth_token=None):
    if auth_token is None:
        auth_token = "hard_"+login_name
    if role_name is None:
        role_name = "user"
    u = User.query.filter_by(login=login_name).first()
    if u is None:
        u = User(login=login_name, token=auth_token)
    r = Role.query.filter_by(name=role_name).first()
    if r is None:
        u.role(Role(name=role_name))
    else:
        u.role = r
    return u

def get_role(role_name):
    r = Role.query.filter_by(name=role_name).first()
    if r is None:
        r = Role(name=role_name)
    return r

def get_tag(tag_name):
    t = Tag.query.filter_by(label=tag_name).first()
    if t is None:
        t = Tag(label=tag_name)
    return t

def init_db():
    db.create_all()
    roles = []
    roles.append(get_role("admin"))
    roles.append(get_role("automation"))
    roles.append(get_role("user"))
    db.session.add_all(roles)
    db.session.commit()
    users = []
    users.append(get_user("admin@123.com", "admin"))
    users.append(get_user("bot@123.com", "automation"))
    db.session.add_all(users)
    db.session.commit()
