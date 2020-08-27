from flask import (
    Blueprint, g, render_template, session, url_for, current_app, request, abort
)

from project.db import get_db
import pdb;

bp = Blueprint('team_detail', __name__)

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
                    
class Contact:
    def __init__(self, id, name, phone, email):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.custom_attributes = []

    def load_custom_attributes(self):
        if self.id:
            db = get_db()

            ca_rows = db.execute(
                'select key,value from custom_attributes ca inner join contacts c on ca.contact_id = c.id where c.id=?',
                (self.id,) 
            ).fetchall()

        self.custom_attributes = [CustomAttribute(ca['key'],ca['value']) for ca in ca_rows if ca_rows]
        

class CustomAttribute:
    def __init__(self,key,value):
        self.key = key
        self.value = value

@bp.route('/team_detail/<int:team_id>', methods=('GET',))
def view_teams(team_id):
    if request.method == 'GET':
        #fausto        
#        pdb.set_trace()

        team = Team.load_team(team_id)

        if not team:
            abort(400, description="Could not load team from DB")

    return render_template('team_detail.html', team=team)

