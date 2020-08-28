from flask import (
    Blueprint, g, render_template, session, url_for, current_app, request, abort
)

from project.db import get_db
from project.models.Team import Team

bp = Blueprint('team_detail', __name__)

@bp.route('/team_detail/<int:team_id>', methods=('GET',))
def view_teams(team_id):
    if request.method == 'GET':
        team = Team.load_team(team_id)

        if not team:
            abort(400, description="Could not load team from DB")

    return render_template('team_detail.html', team=team)

