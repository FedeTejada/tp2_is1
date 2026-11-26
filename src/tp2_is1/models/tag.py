from tp2_is1.extensions import db

# Tabla de asociación Question 0..* <-> 0..* Tag
question_tags = db.Table(
    'question_tags',
    db.Column('question_id', db.Integer, db.ForeignKey('question.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
)


class Tag(db.Model):
    __tablename__ = 'tag'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)

    questions = db.relationship('Question', secondary=question_tags, back_populates='tags')

    def __repr__(self):
        return f"<Tag {self.name}>"
