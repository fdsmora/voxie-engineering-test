from project.db import get_db

def test_import(client, app):
    data = { 'name':'Michigan kangaroos' }
    response = client.post('/import', data=data)
    assert response.status_code == 200 

    with app.app_context():
        db = get_db()
        team = db.execute('SELECT * FROM teams WHERE id = 1').fetchone()
        assert team['name'] == data['name']

def test_import_empty_data(client, app):
    data = { 'name': ''}
    response = client.post('/import', data=data)
    assert response.status_code == 400 
    assert b"No team name provided" in response.data

    data = { }
    response = client.post('/import', data=data)
    assert response.status_code == 400 
