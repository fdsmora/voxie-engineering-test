import json
from flask import (
    Blueprint, render_template, request, abort, jsonify
)

from project.db import get_db

bp = Blueprint('import', __name__)

@bp.route('/import', methods=('POST',))
def import_team():
    if request.method == 'POST':
        json_data = request.get_json()
        team_name = json_data.get('name')

        error = None 
        if not team_name:
            error = 'No team name provided'

        if error is not None:
            abort(400, description=error)

        # TODO: Put this into a data model
        insert_team(json_data)

        return "INSERTED"

def insert_team(request):
    team_name = request.get('name')

    error = None 
    if not team_name:
        error = 'No team name provided'

        if error is not None:
            abort(400, description=error)

    db = get_db()

    db.execute(
        'INSERT INTO teams (name)'
        ' VALUES (?)',
        (team_name,)
    )
    db.commit()

    team_id = get_last_table_id('teams')
    contacts = request.get('contacts')
    for contact in contacts or []:
        contact['team_id'] = team_id
    
    insert_contacts(contacts)

def insert_contacts(contacts):
    if contacts:
        db = get_db()

        for contact in contacts:
            db.execute(
                'INSERT INTO contacts (team_id, name, phone, email)'
                ' VALUES (?,?,?,?)',
                (contact.get('team_id'),contact.get('name'),contact.get('phone'),contact.get('email'))
            )
            db.commit()
            contact['id'] = get_last_table_id('contacts')
            insert_custom_attributes(contact)

def insert_custom_attributes(contact):
    if contact:
        db = get_db()
        
        custom_attributes = contact.get('custom_attributes')
        for ca in custom_attributes or []:
            db.execute(
                'INSERT INTO custom_attributes (contact_id, key, value) VALUES (?,?,?)',
                (contact.get('id'), ca.get('key'), ca.get('value'))
            )

def get_last_table_id(table):
    db = get_db()

    query = 'SELECT id FROM {} order by id desc limit 1'.format(table)
    row = db.execute(query).fetchone()

    return row[0]
    

