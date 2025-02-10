try:
    from Database.database import db
    from Routes.home import home
    from Routes.customer import customers
    from Database.Models.customer import Customer
except ImportError as e:
    print(f"Error: {e}")
    exit()


def configure_all(app):
    configure_routes(app)
    configure_db()


def configure_routes(app):
    app.register_blueprint(home)
    app.register_blueprint(customers, url_prefix="/customers")


def configure_db():
    db.connect()
    db.create_tables([Customer])
