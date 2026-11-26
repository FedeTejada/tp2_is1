from tp2_is1.extensions import db
from tp2_is1.models.author import Author


class User(Author):
    __tablename__ = 'user'
    id = db.Column(db.Integer, db.ForeignKey('author.id'), primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    lastname = db.Column(db.String(40), nullable=False)

    def __init__(self,email,password,name,username,lastname):
        self.email = email
        self.password = password
        self.name = name
        self.username = username
        self.lastname = lastname


    __mapper_args__ = {
        'polymorphic_identity': 'user'
    }