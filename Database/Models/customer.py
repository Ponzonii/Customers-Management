try:
    # Import necessary modules from Peewee ORM
    from peewee import Model, CharField, IntegerField, DateField, DateTimeField

    # Import the database instance
    from Database.database import db

    # Import datetime for handling date and time
    import datetime
except ImportError as e:
    # Print the error message and exit if an import fails
    print(f"Error: {e}")
    exit()


# Define the Customer model
class Customer(Model):
    name = CharField()  # Customer's name
    email = CharField()  # Customer's email
    phone = IntegerField()  # Customer's phone number
    date_birth = DateField()  # Customer's date of birth
    date_register = DateTimeField(
        default=datetime.datetime.now().strftime(
            "%d/%m/%Y - %H:%M:%S"
        )  # Auto-set to current date/time
    )

    class Meta:
        database = db  # Link the model to the database
