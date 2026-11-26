from tp2_is1.extensions import db
from tp2_is1.models.answer import Answer
from tp2_is1.models.category import Category
from tp2_is1.models.question import Question
from tp2_is1.models.tag import Tag


def list_questions():
    return db.session.scalars(db.select(Question).order_by(Question.date.desc())).all()


def get_question(question_id: int):
    return db.session.get(Question, question_id)


def list_categories():
    return db.session.scalars(db.select(Category).order_by(Category.name)).all()


def _get_or_create_tag(name: str) -> Tag:
    tag = db.session.scalar(db.select(Tag).where(Tag.name == name))
    if tag is None:
        tag = Tag(name=name)
        db.session.add(tag)
    return tag


def create_question(user_id: int, category_id: int, title: str, body: str, tags: str = "") -> Question:
    names = {t.strip().lstrip('#').lower() for t in tags.split(',') if t.strip()}
    question = Question(
        user_id=user_id,
        category_id=category_id,
        title=title.strip(),
        body=body.strip(),
        tags=[_get_or_create_tag(n) for n in sorted(names)],
    )
    db.session.add(question)
    db.session.commit()
    return question


def add_answer(question: Question, author_id: int, body: str) -> Answer:
    answer = Answer(question=question, author_id=author_id, body=body.strip())
    db.session.add(answer)
    db.session.commit()
    return answer


def accept_answer(question: Question, answer_id: int, acting_user_id: int) -> Answer:
    """Solo el autor de la pregunta puede marcar una respuesta como aceptada."""
    if question.user_id != acting_user_id:
        raise PermissionError("Solo el autor de la pregunta puede aceptar una respuesta")
    answer = next((a for a in question.answers if a.id == answer_id), None)
    if answer is None:
        raise LookupError("La respuesta no pertenece a la pregunta")
    answer.accept()
    db.session.commit()
    return answer
