import datetime
from peewee import (
    SqliteDatabase, 
    Model,
    CharField,
    DateTimeField,
    FloatField,
    ForeignKeyField,
)
from fields import DateField

database = SqliteDatabase('data.sqlite3')

class BaseModel(Model):
    
    class Meta:
        database = database


class User(BaseModel):
    username = CharField(max_length=20)
    first_name = CharField(max_length=20)
    last_name = CharField(max_length=20)
    email = CharField(max_length=20)
    created_at = DateTimeField(default=datetime.datetime.now)


class Publication(BaseModel):
    title = CharField(max_length=50)
    body = CharField(max_length=240)
    created_date = CharField(default=datetime.datetime.now)
    update_date = CharField(default=datetime.datetime.now)
    user_created = ForeignKeyField(User, backref="publications")


def create_tables():
    with database:
        database.create_tables([User, Publication])


def drop_tables():
    with database:
        database.drop_tables([User, Publication])
