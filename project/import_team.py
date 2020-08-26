from flask import (
    Blueprint, render_template, request, abort, jsonify
)

from project.db import get_db

bp = Blueprint('import', __name__)

@bp.route('/import', methods=('POST',))
def import_team():
    if request.method == 'POST':
        team_name = request.form['name']

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
        return "INSERTED"
