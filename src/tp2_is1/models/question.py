from datetime import UTC, datetime

from tp2_is1.extensions import db
from tp2_is1.models.tag import question_tags


class Question(db.Model):
    __tablename__ = 'question'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text, nullable=False)  # texto enriquecido
    date = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(UTC))

    # Un usuario (humano) realiza 0..* preguntas
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # Cada pregunta pertenece obligatoriamente a UNA categoría
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    user = db.relationship('User', foreign_keys=[user_id])
    category = db.relationship('Category', back_populates='questions')
    tags = db.relationship('Tag', secondary=question_tags, back_populates='questions')
    answers = db.relationship(
        'Answer',
        back_populates='question',
        cascade='all, delete-orphan',
        order_by='Answer.date',
    )

    @property
    def tag_names(self):
        return {t.name for t in self.tags}

    @property
    def accepted_answer(self):
        return next((a for a in self.answers if a.is_accepted), None)

    def __repr__(self):
        return f"<Question {self.id} {self.title!r}>"
