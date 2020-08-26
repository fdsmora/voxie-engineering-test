from flask import (
    Blueprint, g, render_template, session, url_for, current_app, request
)

from project.db import get_db

bp = Blueprint('view', __name__)

@bp.route('/view', methods=('GET',))
def view_teams():
    if request.method == 'GET':
        db = get_db()

        teams = db.execute(
            'SELECT id,name FROM teams'
        ).fetchall()
    return render_template('view.html', teams=teams)
