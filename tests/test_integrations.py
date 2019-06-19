import os
import pytest
from app import app
from flask import url_for
from models import User


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    with app.app_context():
        pass
    yield client


def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200
    for user in User.select():
        assert user.username in str(rv.data)
