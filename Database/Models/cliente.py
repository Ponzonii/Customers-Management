try:
    from peewee import Model, CharField, DateField, DateTimeField
    from Database.database import db
    import datetime
except ImportError as e:
    print(f"Error: {e}")
    exit()


class Cliente(Model):
    nome = CharField()
    email = CharField()
    data_nascimento = DateField()
    data_registro = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
