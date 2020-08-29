from project.db import get_db
from project.models.Contact import Contact

class Team:
    def __init__(self, **kwargs):
       self.id = kwargs.get('id')
       self.name = kwargs.get('name')
       self.contacts = []

    def update(self):
        db = get_db()

        row = db.execute(
            'UPDATE teams SET name=? WHERE id = ?', 
            (self.name,self.id,) 
        ).fetchone()
 
        db.commit()

    @staticmethod
    def load_teams():
        db = get_db()

        rows = db.execute(
            'SELECT id,name FROM teams'
        ).fetchall()
 
        return [Team(id=r['id'],name=r['name']) for r in rows if rows]
        
    @staticmethod
    def load_team(id):
        db = get_db()

        team_row = db.execute(
            'SELECT id,name FROM teams where id = ?', 
            (id,) 
        ).fetchone()
 
        if team_row:
            team = Team(id=team_row['id'],name=team_row['name']) 

            team.contacts = Contact.load_contacts_by_team_id(id)

            return team

        return None

    @staticmethod
    def delete(team_id):
        db = get_db()
        db.execute('DELETE FROM teams WHERE id = ?', (team_id,))
        db.commit()
