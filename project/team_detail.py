from flask import (
    Blueprint, g, render_template, session, url_for, current_app, request, abort, redirect
)

from project.db import get_db
from project.models.Team import Team

bp = Blueprint('team_detail', __name__)

@bp.route('/team_detail/<int:team_id>', methods=('GET',))
def view_teams(team_id):
    if request.method == 'GET':
        team = Team.load_by_id(team_id)

        if not team:
            abort(400, description="Could not load team from DB")

    return render_template('team_detail.html', team=team)

@bp.route('/team_detail/update', methods=('POST',))
def update():
    if request.method == 'POST':
        team_id = request.form.get('team_id')
        new_name = request.form.get('name')
 
        team = Team(id=team_id, name=new_name)

        team.update()

        return redirect(url_for('team_detail.view_teams', team_id=team_id))

    abort(400, description="Could not update team")

@bp.route('/team_detail/delete/<int:team_id>', methods=('GET',))
def delete(team_id):
    if request.method == 'GET':

        Team.delete(team_id)

        return redirect(url_for('view.view_teams'))

    abort(400, description="Could not delete team")
