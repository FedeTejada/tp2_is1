from datetime import UTC, datetime, timedelta

from tp2_is1.extensions import db
from tp2_is1.models.answer import Answer
from tp2_is1.models.question import Question
from tp2_is1.services.author_factory import AuthorFactory
from tp2_is1.services.llm.strategy import Strategy

AI_TAG = 'ia-help'


class AIResponseService:
    """Contexto del patrón Strategy: delega la generación al proveedor configurado."""

    def __init__(self, strategy: Strategy, unanswered_after: timedelta = timedelta(hours=24)):
        self._strategy = strategy
        self.unanswered_after = unanswered_after

    def set_strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def should_answer(self, question: Question, now: datetime | None = None) -> bool:
        """Etiqueta #ia-help, o sin respuestas pasado el tiempo configurado."""
        if question.answers:
            return False
        if AI_TAG in question.tag_names:
            return True
        now = now or datetime.now(UTC)
        date = question.date
        if date.tzinfo is None:
            date = date.replace(tzinfo=UTC)
        return now - date >= self.unanswered_after

    def generate_answer(self, question: Question) -> Answer:
        text = self._strategy.generate_response(question)
        author = AuthorFactory.get_or_create_agent(self._strategy.model)
        answer = Answer()
        answer.body = text
        setattr(answer, 'question', question)
        setattr(answer, 'author', author)
        db.session.add(answer)
        db.session.commit()
        return answer

    def answer_pending(self) -> list[Answer]:
        """Recorre preguntas sin respuesta y genera las que correspondan (para un job/cron)."""
        pending = db.session.scalars(db.select(Question)).all()
        return [self.generate_answer(q) for q in pending if self.should_answer(q)]
