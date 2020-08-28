from project.models.CustomAttribute import CustomAttribute
from project.db import get_db

class Contact:
    def __init__(self, id, name, phone, email):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.custom_attributes = []

    def load_custom_attributes(self):
        if self.id:
            db = get_db()

            ca_rows = db.execute(
                'select key,value from custom_attributes ca inner join contacts c on ca.contact_id = c.id where c.id=?',
                (self.id,) 
            ).fetchall()

        self.custom_attributes = [CustomAttribute(ca['key'],ca['value']) for ca in ca_rows if ca_rows]
