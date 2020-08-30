from flask import (
    Blueprint, g, render_template, session, url_for, current_app, request
)

from project.db import get_db
from project.models.Team import Team
from project.models.Contact import Contact
import urllib.parse

bp = Blueprint('search_contacts', __name__)

@bp.route('/search_contacts/<string:phone>', methods=('GET',))
@bp.route('/search_contacts/', methods=('GET',))
def search(phone=None):
    contacts=[]
    if phone:
        phone = urllib.parse.unquote(phone)
        contacts = Contact.load_contacts_by_phone(phone)
    else:
        contacts = Contact.load_all()

    teams = get_teams_in_contacts(contacts)

    return render_template('search_contacts.html', contacts=contacts, teams=teams)

def get_teams_in_contacts(contacts):
    teams = {}
    for c in contacts:
        team = Team.load_by_id(c.team_id)
        teams[c.team_id] = team
    return teams
