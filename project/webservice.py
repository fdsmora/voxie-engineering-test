import functools
import pdb

from flask import (
    Blueprint, flash, g, render_template, session, url_for, current_app, request
)

from project.db import get_db

bp = Blueprint('webservice', __name__)

@bp.route('/add_team/<name>', methods=('POST','GET'))
def add_team(name):
    if request.method == 'GET':
        db = get_db()

        error = None 
        if not name:
            error = 'No team name provided'

        if error is not None:
            flash(error)
            return "nada"

        db.execute(
            'INSERT INTO teams (name)'
            ' VALUES (?)',
            (name,)
        )
        db.commit()
        return "INSERTED"
        #return redirect(url_for('blog.index'))

#    return render_template('blog/create.html')
    return "nothing"
