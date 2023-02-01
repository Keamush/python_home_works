import datetime
from peewee import SqliteDatabase, DatabaseProxy, Model, CharField, DateTimeField


database_proxy = DatabaseProxy()


class BaseModel(Model):
    class Meta:
        database = database_proxy


class User(BaseModel):
    login = CharField(max_length=100, unique=True, index=True)
    password_hash = CharField(max_length=128)
    last_visit = DateTimeField(default=datetime.datetime.now)


database_name = 'tkinter_db.sqlite3'
db = SqliteDatabase(database_name)

database_proxy.initialize(db)

db.create_tables([User])

# user = User(
#     login='user',
#     password_hash='127'
# )
# user.save()

users = User.select()

for user in users:
    print(user.login, user.last_visit)
