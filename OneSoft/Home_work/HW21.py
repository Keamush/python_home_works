from peewee import *

db = SqliteDatabase('test_db.sqlite3')

class City(Model):
    id = IntegerField()
    name = CharField()
    country_id = IntegerField()

