""""""

def test_register_user(client):
    # Test registering a normal user
    response = client.post('/register', data={
        'user_type': 'normal',
        'username': 'test_normal_user'
    })

    assert response.status_code == 200
    assert b'User test_normal_user of type normal registered successfully.' in response.data

    # Test registering an admin user
    response = client.post('/register', data={
        'user_type': 'admin',
        'username': 'test_admin_user'
    })

    assert response.status_code == 200
    assert b'User test_admin_user of type admin registered successfully.' in response.data

