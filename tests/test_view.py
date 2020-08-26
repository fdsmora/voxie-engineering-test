import pytest
from project.db import get_db

def test_view(client, app):
    test_team_names = ['Fausto','David','Tomas']
    
    with app.app_context():
        db = get_db()
        for name in test_team_names:
            db.execute(
                "INSERT INTO TEAMS (name) VALUES (?)", (name,)
            )
        db.commit()

    response = client.get('/view')
    assert response.status_code == 200
    for name in test_team_names:
        assert name.encode('utf-8') in response.data
