from tp2_is1.models.user import User

users = [
    User('lucia.gomez@example.com', 'secreto123', 'Lucía', 'luciag', 'Gómez'),
    User('carlos.perez@example.com', 'clave456', 'Carlos', 'cperez', 'Pérez'),
    User('sofia.martinez@example.com', 'pass789', 'Sofía', 'smartinez', 'Martínez'),
    User('mateo.rodriguez@example.com', 'pass123', 'Mateo', 'mrod', 'Rodríguez'),
    User('valentina.lopez@example.com', 'pass321', 'Valentina', 'valen_l', 'López'),
    User('alejandro.garcia@example.com', 'pass456', 'Alejandro', 'alejandro_g', 'García'),
    User('camila.fernandez@example.com', 'pass789', 'Camila', 'camif', 'Fernández'),
    User('joaquin.diaz@example.com', 'pass111', 'Joaquín', 'jdiaz', 'Díaz'),
    User('martina.torres@example.com', 'pass222', 'Martina', 'martutorres', 'Torres'),
    User('lucas.ruiz@example.com', 'pass333', 'Lucas', 'lruiz', 'Ruiz'),
    User('florencia.alvarez@example.com', 'pass444', 'Florencia', 'flor_alvarez', ''),
    User('tomas.moreno@example.com', 'pass555', 'Tomás', 'tmoreno', 'Moreno'),
    User('agustina.jimenez@example.com', 'pass666', 'Agustina', 'agus_jimenez', 'Jiménez'),
    User('nicolas.ruiz@example.com', 'pass777', 'Nicolás', 'nico_ruiz', 'Ruiz'),
    User('victoria.castro@example.com', 'pass888', 'Victoria', 'vicky_c', 'Castro'),
    User('benjamin.romero@example.com', 'pass999', 'Benjamín', 'benja_romero', 'Romero'),
    User('catalina.sosa@example.com', 'pass101', 'Catalina', 'catasosa', 'Sosa'),
    User('lautaro.acosta@example.com', 'pass202', 'Lautaro', 'laucha_a', 'Acosta'),
    User('julieta.medina@example.com', 'pass303', 'Julieta', 'julietam', 'Medina'),
    User('franco.flores@example.com', 'pass404', 'Franco', 'fflores', 'Flores'),
    User('micaela.ortiz@example.com', 'pass505', 'Micaela', 'mily_ortiz', 'Ortiz'),
    User('ignacio.silva@example.com', 'pass606', 'Ignacio', 'nacho_silva', 'Silva')
]


next_user_id = 0


def add_user(user):
    global next_user_id

    user.id = next_user_id
    users.append(user)

    next_user_id += 1

    return user


def get_all_users():
    return users


def get_user_by_id(user_id):
    return next(
        (user for user in users if user.id == user_id),
        None
    )
def update_user(user_id, data):
    user = get_user_by_id(user_id)

    if user is None:
        return None

    for field, value in data.items():
        setattr(user, field, value)

    return user


def delete_user(user_id):
    user = get_user_by_id(user_id)

    if user is None:
        return False

    users.remove(user)
    return True