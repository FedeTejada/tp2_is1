from flask import (Blueprint,render_template,request,url_for, flash,redirect)
from tp2_is1.services.user_store import (get_all_users, delete_user, update_user , get_user_by_id)

## API REST
#GET    /users
#GET    /users/<id>
#GET    /users/new
#POST   /users
#GET    /users/<id>/edit
#POST   /users/<id>
#POST   /users/<id>/delete

user_bp = Blueprint('users', __name__, url_prefix='/users')

##  OBTENER USUARIOS
@user_bp.route('/' , methods=['GET'])
def index():
    users = get_all_users()
    return render_template("users/index.html", users = users)


##  EDITAR USUARIOS
@user_bp.get('/<int:id>/edit')
def user_edit(id):
    user = get_user_by_id(id)
    if user is None:
        return "Usuario no encontrado", 404
    return render_template('users/edit.html', user=user)

@user_bp.patch('/<int:id>/edit')
def edit_user(id):
    user = get_user_by_id(id)

    if user is None:
        return "Usuario no encontrado", 404

    payload = request.get_json()

    data = {
        'username': payload.get('username'),
        'email': payload.get('email'),
        'name': payload.get('name'),
        'lastname': payload.get('lastname'),
    }

    print(data['username'])
    print(data['name'])
    print(data['lastname'])
    if not all(data.values()):
        flash("Todos los datos son obligatorios")

    for existing in get_all_users():
        if existing.id == id:
            check_user = update_user(id, data)
            print(check_user.lastname)
            return {
                "message": "Usuario actualizado correctamente",
                "redirect_url": url_for('users.show_user', id=id)
            }, 200
    flash("Usuario no encontrado")
    return redirect(url_for('users.index'))


## ELIMINAR UN USUARIO POR SU ID
## Recibimos una solicitud desde el front con el metodo delete al endpoint declarado, verificamos que este el usuario a eliminar, si esta lo borramos y si no arrojamos un error usuario invalido
@user_bp.delete('/<int:id>')
def delete_user_route(id):
    try:
        deleted = delete_user(id)
    except ValueError as error:
        return {"error": str(error)}, 409
    if not deleted:
        return {"error": "Usuario no encontrado"}, 404
    return {
        "message": "Usuario eliminado correctamente"
    }, 200


@user_bp.get('/<int:id>')
def show_user(id):
    user = get_user_by_id(id)

    if user is None:
        return "Usuario no encontrado", 404

    return render_template('users/show.html', user=user)