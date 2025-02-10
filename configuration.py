try:
    # Importing necessary modules and components for the app
    from Database.database import db
    from Routes.home import home
    from Routes.customer import customers
    from Database.Models.customer import Customer
except ImportError as e:
    # If any import fails, print the error message and exit the program
    print(f"Error: {e}")
    exit()


def configure_all(app):
    # Configure routes and database connections for the app
    configure_routes(app)
    configure_db()


def configure_routes(app):
    # Registering the home and customers blueprints to the app
    app.register_blueprint(home)
    app.register_blueprint(customers, url_prefix="/customers")


def configure_db():
    # Establishing the database connection and creating necessary tables
    db.connect()
    db.create_tables([Customer])
