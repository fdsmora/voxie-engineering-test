from project.db import get_db
from test_import import test_import_team_contacts

def test_team_detail(client, app):
    test_import_team_contacts(client, app)

    team_id=None
    with app.app_context():
        row = get_db().execute('SELECT MAX(id) FROM teams').fetchone()
        team_id = row[0]

    response = client.get("/team_detail/{}".format(team_id))
    assert response.status_code == 200 

    assert b'Name' in response.data
    assert b'Phone' in response.data
    assert b'Email' in response.data

