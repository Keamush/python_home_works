from peewee import *

db = SqliteDatabase('test_db.sqlite3')


class BaseModel(Model):
    class Meta:
        database = db


class Role(BaseModel):
    name = CharField(unique=True, null=False, max_length=25)
    description = CharField(max_length=150)


class Profile(BaseModel):
    avatar = CharField(max_length=200)
    info = CharField(null=True)


class User(BaseModel):
    username = CharField(unique=True, null=False)
    password = CharField(null=False)
    role = ForeignKeyField(Role, backref='users')
    profile = ForeignKeyField(Profile, backref='user')


class Country(BaseModel):
    code = CharField(max_length=3, unique=True, null=False)
    name = CharField(max_length=100, unique=True, null=False)
    flag = CharField(max_length=200, unique=True)


class City(Model):
    name = CharField(max_length=150, unique=True, null=False)
    country = ForeignKeyField(Country, backref='cities')


class User_City(BaseModel):
    user_id = ForeignKeyField(User)
    city_id = ForeignKeyField(City)


db.connect()
db.create_tables([Role, Profile, User, Country, City, User_City])

user = User.get(User.id == 1)
print(user.username)

users = (User.select(User, Role).join(Role))

