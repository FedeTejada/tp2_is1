from tp2_is1.extensions import db
from tp2_is1.models.author import Author


class User(Author):
    __tablename__ = 'user'
    id = db.Column(db.Integer, db.ForeignKey('author.id'), primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    lastname = db.Column(db.String(120), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'user'
    }