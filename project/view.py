from flask import (
    Blueprint, g, render_template, session, url_for, current_app, request
)

from project.db import get_db
from project.models.Team import Team

bp = Blueprint('view', __name__)

@bp.route('/view', methods=('GET',))
def view_teams():
    teams = [] 
    if request.method == 'GET':
        teams = Team.load_teams()

    return render_template('view.html', teams=teams)
