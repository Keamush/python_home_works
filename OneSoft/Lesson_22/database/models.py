from peewee import *

db = SqliteDatabase('users.sqlite3')


class BaseModel(Model):
    class Meta:
        database = db


class Role(BaseModel):
    name = CharField(unique=True, null=False, max_length=20)
    description = CharField(max_length=100)


class Profile(BaseModel):
    avatar = CharField(max_length=200)
    info = CharField(null=True)


class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    role = ForeignKeyField(Role, backref='users', on_delete='CASCADE')
    profile = ForeignKeyField(Profile, backref='user')


class Country(BaseModel):
    code = CharField(max_length=3, unique=True, null=False)
    name = CharField(max_length=100, unique=True, null=False)
    flag = CharField(max_length=200, unique=True)
    description = TextField()


class City(BaseModel):
    name = CharField(max_length=150, unique=True, null=False)
    country = ForeignKeyField(Country, backref='cities', on_delete='CASCADE')


class Weather(BaseModel):
    cloudiness = CharField(max_length=100)
    temperature = FloatField()
    wind = FloatField()
    icon = CharField(max_length=200)
    city = ForeignKeyField(City, backref='weather', on_delete='CASCADE')


class UserCity(BaseModel):
    user_id = ForeignKeyField(User)
    city_id = ForeignKeyField(City)


tables = [Role, Profile, User, Country, City, UserCity, Weather]
db.create_tables(tables)

