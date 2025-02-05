try:
    from peewee import Model, CharField, IntegerField, DateField, DateTimeField
    from Database.database import db
    import datetime
except ImportError as e:
    print(f"Error: {e}")
    exit()


class Cliente(Model):
    nome = CharField()
    email = CharField()
    telefone = IntegerField()
    data_nascimento = DateField()
    data_registro = DateTimeField(
        default=datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
    )

    class Meta:
        database = db
