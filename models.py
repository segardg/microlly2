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


class Specie(BaseModel):
    name = CharField(max_length=30)
    name_meaning = CharField()


class IngenModel(BaseModel):
    version = FloatField()
    specie = ForeignKeyField(Specie, backref="models")


class Dinosaur(BaseModel):
    name = CharField(max_length=20)
    birthday = DateField()
    created_at = DateTimeField(default=datetime.datetime.now)
    model = ForeignKeyField(IngenModel, backref="dinosaurs")


def create_tables():
    with database:
        database.create_tables([Dinosaur, IngenModel, Specie])


def drop_tables():
    with database:
        database.drop_tables([Dinosaur, IngenModel, Specie])
