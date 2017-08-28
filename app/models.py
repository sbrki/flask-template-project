from peewee import *

db = SqliteDatabase("database.db")

#
# FOR POSTGRESQL, USE THIS INSTEAD
#
# from playhouse.postgres_ext import *
#
# db = PostgresqlExtDatabase(
#     'database_name',
#     register_hstore=False)

class Example(Model):
    text = CharField()
    number = IntegerField()
    float = FloatField()
    bool = BooleanField()

    class Meta:
        database = db


def try_create_tables():
    """
    Creates tables in the database.
    Wrapped in a "try" exception block.
    """
    try:
        db.create_tables([Example])
    except Exception as e:
        pass
