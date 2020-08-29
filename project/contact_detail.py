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
        contact = Contact.load_by_id(contact_id)

        if not contact:
            abort(400, description="Could not load contact from DB")

    return render_template('contact_detail.html', contact=contact)

@bp.route('/contact_detail/update_contact', methods=('POST',))
def update_contact():
    if request.method == 'POST':
        contact_id = request.form.get('contact_id')
        new_name = request.form.get('name')
        new_phone = request.form.get('phone')
        new_email = request.form.get('email')

        contact = Contact(id=contact_id,name=new_name,phone=new_phone,email=new_email) 

        contact.update()

        return redirect(url_for('contact_detail.edit', contact_id=contact_id))

    abort(400, description="Could not update contact")

@bp.route('/contact_detail/update_custom_attribute/', methods=('POST',))
def update_custom_attribute():
    if request.method == 'POST':
        new_ca_id = request.form['custom_attribute_id'];
        new_key = request.form['key_{}'.format(new_ca_id)]
        new_value = request.form['value_{}'.format(new_ca_id)]
        contact_id = request.form['contact_id']

        ca = CustomAttribute(id=new_ca_id, key=new_key, value=new_value, contact_id=contact_id)

        ca.update()

        return redirect(url_for('contact_detail.edit', contact_id=contact_id))

@bp.route('/contact_detail/delete/<int:contact_id>', methods=('GET',))
def delete(contact_id):
    if request.method == 'GET':
        # load contact just to get team_id 
        contact = Contact.load_by_id(contact_id)
        team_id = contact.team_id

        Contact.delete(contact_id)

        return redirect(url_for('team_detail.view_teams', team_id=team_id))

    abort(400, description="Could not delete contact")   
