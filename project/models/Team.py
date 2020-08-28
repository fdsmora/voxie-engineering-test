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

            team.load_contacts()

            return team

        return None

    def load_contacts(self):
        if (self.id):
            db = get_db()

            contacts_rows = db.execute(
                'select c.id, c.name, phone, email from contacts c inner join teams t on c.team_id=t.id where t.id=?',
                (self.id,) 
            ).fetchall()

            self.contacts = [Contact(row['id'],row['name'],row['phone'],row['email']) for row in contacts_rows if contacts_rows]

            for contact in self.contacts:
                contact.load_custom_attributes()
                    
