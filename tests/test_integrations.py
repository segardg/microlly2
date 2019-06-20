import os
import pytest
from app import *
from flask import url_for
from models import User, Publication

def user_create():
    user = User()
    assert user.created_at == datetime.datetime.now

@pytest.fixture
def user():
    user = User()
    yield user

def publi_create():
    publi = Publication.create(title='osef', body='essai', username=user)
    assert publi.user_created == datetime.datetime.now

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    with app.app_context():
        pass
    yield client


def test_publication(client):
    with app.app_context():
        rv = client.get(url_for('publication'))
    assert rv.status_code == 200
    for user in User.select():
        assert user.username in str(rv.data) is str
        assert 5==4

