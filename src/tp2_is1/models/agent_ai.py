from typing import ClassVar

from tp2_is1.extensions import db
from tp2_is1.models.author import Author


class Agent_AI(Author):
    __tablename__ = 'agent'
    id = db.Column(db.Integer,db.ForeignKey('author.id'),primary_key=True)
    model = db.Column(db.String,nullable=False)

    __mapper_args__: ClassVar[dict] = {
        'polymorphic_identity': 'agent'
    }
