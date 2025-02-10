try:
    from peewee import Model, CharField, IntegerField, DateField, DateTimeField
    from Database.database import db
    import datetime
except ImportError as e:
    print(f"Error: {e}")
    exit()


class Customer(Model):
    name = CharField()
    email = CharField()
    phone = IntegerField()
    date_birth = DateField()
    date_register = DateTimeField(
        default=datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
    )

    class Meta:
        database = db
