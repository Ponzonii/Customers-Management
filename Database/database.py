try:
    from peewee import SqliteDatabase as Sqlite
except ImportError as e:
    print(f"Error: {e}")

db = Sqlite("customers.db")
