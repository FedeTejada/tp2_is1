from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from tp2_is1.models.user import User
from tp2_is1.services.user_store import (add_user, get_all_users)

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.get('/register')
def register():
    return render_template('auth/register.html')

@auth_bp.post('/register')
def reg_date():
    users = get_all_users()
    username = request.form.get('username',"").strip()
    name = request.form.get('name',"").strip()
    password = request.form.get('password',"").strip()
    lastname = request.form.get('lastname',"").strip()
    email = request.form.get('email',"").strip()
    confirm_pass = request.form.get('confirm_password',"").strip()

    if not all([username, name, password, confirm_pass]):
        flash('Los campos son obligatorio',"error")
        return render_template('auth/register.html')

    if password != confirm_pass:
        flash('Son distinta las password',"error")
        return render_template('auth/register.html')

    if any(user.username == username for user in users):
        flash('El username ya existe',"error")
        return render_template('auth/register.html')

    if any(user.email == email for user in users):
        flash('El email ya existe',"error")
        return render_template('auth/register.html')


    user = User(email, password, name, username, lastname)
    add_user(user)


    print(user.id, user.email, user.name, user.lastname)
    print(len(users))
    return redirect(url_for('auth.register'))