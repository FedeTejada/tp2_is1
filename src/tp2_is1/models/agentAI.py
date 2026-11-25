from tp2_is1.extensions import db
from tp2_is1.models.author import Author


class AgentAI(Author):
    __tablename__ = 'agent'
    id = db.Column(db.Integer,db.ForeignKey('author.id'),primary_key=True)
    model = db.Column(db.String,nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'agent'
    }
