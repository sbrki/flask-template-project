from peewee import *

db = SqliteDatabase("database_name.db")

# 
# FOR POSTGRESQL, USE THIS INSTEAD
#
#from playhouse.postgres_ext import *
#
# Creating the database connection
#db = PostgresqlExtDatabase(
#    'database_name',
#    register_hstore=False)