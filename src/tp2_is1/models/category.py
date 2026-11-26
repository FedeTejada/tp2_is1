from tp2_is1.extensions import db


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    questions = db.relationship('Question', back_populates='category')

    def __repr__(self):
        return f"<Category {self.name}>"
