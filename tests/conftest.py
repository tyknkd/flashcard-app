#!/usr/bin/python3

# Test configuration script to be run for each unit test 
# Reference: https://flask.palletsprojects.com/en/2.1.x/tutorial/tests/

# Class to handle user authentication procedures
class AuthActions(object):
    def __init__(self, client):
        self._client = client
    
    def login(self, username='test', password='test'):
        return self._client.post(
            '/auth/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/auth/logout')

@pytest.fixture
def auth(client):
    return AuthActions(client)
