from project.db import get_db
from testutil import load_json_from_file

def test_import(client, app):
    data = { 'name':'Michigan kangaroos' }
    response = client.post('/import', json=data)
    assert response.status_code == 200 

    with app.app_context():
        db = get_db()
        team = db.execute('SELECT * FROM teams WHERE id = 1').fetchone()
        assert team['name'] == data['name']

def test_import_empty_data(client, app):
    data = { 'name': ''}
    response = client.post('/import', json=data)
    assert response.status_code == 400 
    assert b"No team name provided" in response.data

    data = { }
    response = client.post('/import', json=data)
    assert response.status_code == 400 

def test_import_team_contacts(client, app):
    data = load_json_from_file('team_contacts.json')
    response = client.post('/import', json=data)
    assert response.status_code == 200 
    
    with app.app_context():
        db = get_db()
        team = db.execute('SELECT * FROM teams WHERE id = 1').fetchone()
        assert team['name'] == data['name']
        db = get_db()
        team = db.execute('SELECT * FROM teams WHERE id = 1').fetchone()
        assert team['name'] == data['name']
        row = db.execute(
                'SELECT count(*) FROM contacts WHERE team_id = ?', (team['id'],)
            ).fetchone()
        assert row[0] == len(data['contacts']) 
        row = db.execute(
                'SELECT count(*) FROM custom_attributes ca inner join contacts c on ca.contact_id = c.id'
            ).fetchone()
        total_custom_attributes = 0
        for contact in data['contacts']:
            if 'custom_attributes' in contact:
                total_custom_attributes += len(contact['custom_attributes'])
        assert row[0] == total_custom_attributes 
