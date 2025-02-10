""""""

def test_login_with_basic_auth(client):
    # Test successful login with BasicAuthStrategy
    response = client.post('/login', json={
        'auth_type': 'basic',
        'username': 'admin',
        'credential': 'secret'
    })

    assert response.status_code == 200
    assert b'"success":true' in response.data
    assert b'"message":"Logged in"' in response.data

    # Test failed login with incorrect credentials
    response = client.post('/login', json={
        'auth_type': 'basic',
        'username': 'admin',
        'credential': 'wrong_password'
    })

    assert response.status_code == 200
    assert b'"success":false' in response.data
    assert b'"message":"Invalid credentials"' in response.data

def test_login_with_token_auth(client):
    # Test successful login with TokenAuthStrategy
    response = client.post('/login', json={
        'auth_type': 'token',
        'username': 'admin',
        'credential': 'valid_api_token'
    })

    assert response.status_code == 200
    assert b'"success":true' in response.data
    assert b'"message":"Logged in"' in response.data
