"""Acceso a usuarios sobre la base de datos.

Mantiene la misma interfaz que la versión en memoria (get_all_users, add_user, ...)
para que las rutas de /users y /auth no cambien, pero ahora los usuarios se
guardan en la BD y por lo tanto también están disponibles en /questions.
"""
from tp2_is1.extensions import db
from tp2_is1.models.answer import Answer
from tp2_is1.models.question import Question
from tp2_is1.models.user import User


def add_user(user):
    db.session.add(user)
    db.session.commit()
    return user


def get_all_users():
    return db.session.scalars(db.select(User).order_by(User.username)).all()


def get_user_by_id(user_id):
    return db.session.get(User, user_id)


def update_user(user_id, data):
    user = get_user_by_id(user_id)

    if user is None:
        return None

    for field, value in data.items():
        setattr(user, field, value)

    db.session.commit()
    return user


def delete_user(user_id):
    user = get_user_by_id(user_id)

    if user is None:
        return False

    has_questions = db.session.scalar(
        db.select(Question.id).where(Question.user_id == user_id).limit(1)
    )
    has_answers = db.session.scalar(
        db.select(Answer.id).where(Answer.author_id == user_id).limit(1)
    )
    if has_questions or has_answers:
        raise ValueError("No se puede eliminar un usuario que tiene preguntas o respuestas")

    db.session.delete(user)
    db.session.commit()
    return True
