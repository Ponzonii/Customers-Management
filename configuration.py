try:
    from Database.database import db
    from Routes.home import home
    from Routes.cliente import cliente
    from Database.Models.cliente import Cliente
except ImportError as e:
    print(f"Error: {e}")
    exit()


def configure_all(app):
    configure_routes(app)
    configure_db()


def configure_routes(app):
    app.register_blueprint(home)
    app.register_blueprint(cliente, url_prefix="/clientes")


def configure_db():
    db.connect()
    db.create_tables([Cliente])
