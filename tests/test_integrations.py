import os
import pytest
from app import app
from flask import url_for
from models import Dinosaur


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
    for dinosaur in Dinosaur.select():
        assert dinosaur.name in str(rv.data)
