from flask import Blueprint
## API REST
#GET    /users
#GET    /users/<id>
#GET    /users/new
#POST   /users
#GET    /users/<id>/edit
#POST   /users/<id>
#POST   /users/<id>/delete



user_bp = Blueprint('users', __name__, url_prefix='/users')
@user_bp.route('/' , methods=['GET'])
def index():
    return "Listar todos los usuaruis"

@user_bp.route('/<int:id>' , methods=['GET'])
def show_user(id):
    return "Usuario: "

@user_bp.route('' , methods=['POST'])
def create_user():
    return "Crear usuario"

@user_bp.route('/<int:id>' , methods=['PUT'])
def update_user(id):
    return "Editar usuario"

@user_bp.route('/<int:id>' , methods=['DELETE'])
def delete_user(id):
    return "Deletar usuario"
