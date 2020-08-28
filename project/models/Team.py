from project.db import get_db
from project.models.Contact import Contact

class Team:
    def __init__(self, id, name):
       self.id = id
       self.name = name
       self.contacts = []

    @staticmethod
    def load_team(id):
        db = get_db()

        team_row = db.execute(
            'SELECT id,name FROM teams where id = ?', 
            (id,) 
        ).fetchone()
 
        if team_row:
            team = Team(team_row['id'],team_row['name']) 

            team.contacts = Contact.load_contacts_by_team_id(id)

            return team

        return None
