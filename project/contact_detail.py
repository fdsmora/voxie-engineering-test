from flask import (
    Blueprint, g, render_template, session, url_for, current_app, request, abort, redirect
)

from project.db import get_db
from project.models.Contact import Contact 
from project.models.CustomAttribute import CustomAttribute

bp = Blueprint('contact_detail', __name__)

@bp.route('/contact_detail/edit/<int:contact_id>', methods=('GET',))
def edit(contact_id):
    if request.method == 'GET':
        contact = Contact.load_contact(contact_id)

        if not contact:
            abort(400, description="Could not load contact from DB")

    return render_template('contact_detail.html', contact=contact)

@bp.route('/contact_detail/update_custom_attribute/', methods=('POST',))
def update_custom_attribute():
    if request.method == 'POST':
        new_ca_id = request.form['hd_custom_attribute_id'];
        new_key = request.form['key_{}'.format(new_ca_id)]
        new_value = request.form['value_{}'.format(new_ca_id)]
        contact_id = request.form['hd_contact_id']

        ca = CustomAttribute(id=new_ca_id, key=new_key, value=new_value, contact_id=contact_id)

        ca.update()

        return redirect(url_for('contact_detail.edit', contact_id=contact_id))

    abort(400, description="Could not update custom attribute")
