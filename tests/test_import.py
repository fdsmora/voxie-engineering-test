from project.db import get_db
import json
import os 

current_path = os.path.dirname(os.path.realpath(__file__)) 
json_dir = os.path.join(current_path,'json')

def load_json_from_file(file_name):
    with open(os.path.join(json_dir,file_name)) as f:
        return json.load(f)

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
                'SELECT count(*) FROM custom_attributes WHERE contact_id IN (SELECT id from contacts)'
            ).fetchone()
        assert row[0] == len(data['contacts'][0]['custom_attributes'])
