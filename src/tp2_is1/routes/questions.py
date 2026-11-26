from flask import (
    Blueprint, abort, current_app, flash, redirect, render_template, request, url_for,
)

from tp2_is1.extensions import db
from tp2_is1.models.user import User
from tp2_is1.services import question_service as qs
from tp2_is1.services.ai_response_service import AIResponseService
from tp2_is1.services.llm import strategy_from_config

## Rutas HTML (server-side)
#GET    /questions
#GET    /questions/new
#POST   /questions
#GET    /questions/<id>
#POST   /questions/<id>/answers
#POST   /questions/<id>/answers/<answer_id>/accept
#POST   /questions/<id>/ai-answer

question_bp = Blueprint('questions', __name__, url_prefix='/questions')


def _question_or_404(id):
    question = qs.get_question(id)
    if question is None:
        abort(404)
    return question


def _current_user_id():
    """Provisorio: sin autenticación aún, el usuario llega por el formulario."""
    try:
        user_id = int(request.form['user_id'])
    except (KeyError, ValueError):
        abort(400, 'user_id requerido')
    if db.session.get(User, user_id) is None:
        abort(400, 'usuario inexistente')
    return user_id


@question_bp.get('/')
def index():
    return render_template('questions/index.html', questions=qs.list_questions())


@question_bp.get('/new')
def new_question():
    users = db.session.scalars(db.select(User).order_by(User.username)).all()
    return render_template('questions/new.html', categories=qs.list_categories(), users=users)


@question_bp.post('')
def create_question():
    title = request.form.get('title', '').strip()
    body = request.form.get('body', '').strip()
    category_id = request.form.get('category_id', type=int)
    if not title or not body or category_id is None:
        abort(400, 'título, cuerpo y categoría son obligatorios')
    question = qs.create_question(
        user_id=_current_user_id(),
        category_id=category_id,
        title=title,
        body=body,
        tags=request.form.get('tags', ''),
    )
    return redirect(url_for('questions.show_question', id=question.id))


@question_bp.get('/<int:id>')
def show_question(id):
    users = db.session.scalars(db.select(User).order_by(User.username)).all()
    return render_template('questions/show.html', question=_question_or_404(id), users=users)


@question_bp.post('/<int:id>/answers')
def create_answer(id):
    question = _question_or_404(id)
    body = request.form.get('body', '').strip()
    if not body:
        abort(400, 'el cuerpo de la respuesta es obligatorio')
    qs.add_answer(question, _current_user_id(), body)
    return redirect(url_for('questions.show_question', id=id))


@question_bp.post('/<int:id>/answers/<int:answer_id>/accept')
def accept_answer(id, answer_id):
    question = _question_or_404(id)
    try:
        qs.accept_answer(question, answer_id, _current_user_id())
    except PermissionError:
        abort(403)
    except LookupError:
        abort(404)
    return redirect(url_for('questions.show_question', id=id))


@question_bp.post('/<int:id>/ai-answer')
def ai_answer(id):
    question = _question_or_404(id)
    service = AIResponseService(strategy_from_config(current_app.config))
    if not service.should_answer(question):
        flash('Esta pregunta no requiere respuesta automática.')
    else:
        service.generate_answer(question)
    return redirect(url_for('questions.show_question', id=id))
