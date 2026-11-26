"""Datos de prueba que se cargan una sola vez cuando la base está vacía."""
from tp2_is1.extensions import db
from tp2_is1.models.category import Category
from tp2_is1.models.user import User

# (email, password, nombre, username, apellido)
DEMO_USERS = [
    ('lucia.gomez@example.com', 'secreto123', 'Lucía', 'luciag', 'Gómez'),
    ('carlos.perez@example.com', 'clave456', 'Carlos', 'cperez', 'Pérez'),
    ('sofia.martinez@example.com', 'pass789', 'Sofía', 'smartinez', 'Martínez'),
    ('mateo.rodriguez@example.com', 'pass123', 'Mateo', 'mrod', 'Rodríguez'),
    ('valentina.lopez@example.com', 'pass321', 'Valentina', 'valen_l', 'López'),
    ('alejandro.garcia@example.com', 'pass456', 'Alejandro', 'alejandro_g', 'García'),
    ('camila.fernandez@example.com', 'pass789', 'Camila', 'camif', 'Fernández'),
    ('joaquin.diaz@example.com', 'pass111', 'Joaquín', 'jdiaz', 'Díaz'),
    ('martina.torres@example.com', 'pass222', 'Martina', 'martutorres', 'Torres'),
    ('lucas.ruiz@example.com', 'pass333', 'Lucas', 'lruiz', 'Ruiz'),
    ('florencia.alvarez@example.com', 'pass444', 'Florencia', 'flor_alvarez', 'Álvarez'),
    ('tomas.moreno@example.com', 'pass555', 'Tomás', 'tmoreno', 'Moreno'),
    ('agustina.jimenez@example.com', 'pass666', 'Agustina', 'agus_jimenez', 'Jiménez'),
    ('nicolas.ruiz@example.com', 'pass777', 'Nicolás', 'nico_ruiz', 'Ruiz'),
    ('victoria.castro@example.com', 'pass888', 'Victoria', 'vicky_c', 'Castro'),
    ('benjamin.romero@example.com', 'pass999', 'Benjamín', 'benja_romero', 'Romero'),
    ('catalina.sosa@example.com', 'pass101', 'Catalina', 'catasosa', 'Sosa'),
    ('lautaro.acosta@example.com', 'pass202', 'Lautaro', 'laucha_a', 'Acosta'),
    ('julieta.medina@example.com', 'pass303', 'Julieta', 'julietam', 'Medina'),
    ('franco.flores@example.com', 'pass404', 'Franco', 'fflores', 'Flores'),
    ('micaela.ortiz@example.com', 'pass505', 'Micaela', 'mily_ortiz', 'Ortiz'),
    ('ignacio.silva@example.com', 'pass606', 'Ignacio', 'nacho_silva', 'Silva'),
]

DEMO_CATEGORIES = [
    'Programación', 'Bases de datos', 'Ingeniería de software',
    'Redes', 'Matemática', 'Otros',
]


def seed_demo_data():
    if db.session.scalar(db.select(User.id).limit(1)) is None:
        db.session.add_all(User(*row) for row in DEMO_USERS)
    if db.session.scalar(db.select(Category.id).limit(1)) is None:
        db.session.add_all(Category(name=n) for n in DEMO_CATEGORIES)
    db.session.commit()
