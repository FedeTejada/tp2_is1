from datetime import UTC, datetime

from tp2_is1.extensions import db


class Answer(db.Model):
    __tablename__ = 'answer'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(UTC))
    is_accepted = db.Column(db.Boolean, nullable=False, default=False)

    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    # Autoría polimórfica: apunta a Author (User o AgentAI) sin acoplar Answer a ninguno
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    question = db.relationship('Question', back_populates='answers')
    author = db.relationship('Author')

    def accept(self):
        """Marca esta respuesta como aceptada (solo una por pregunta)."""
        for other in self.question.answers:
            other.is_accepted = False
        self.is_accepted = True

    def __repr__(self):
        return f"<Answer {self.id} q={self.question_id}>"
