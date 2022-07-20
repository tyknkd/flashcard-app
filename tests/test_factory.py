#!/usr/bin/python3

# Application factory unit test 
# Reference: https://flask.palletsprojects.com/en/2.1.x/tutorial/tests/

from flaskr import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
