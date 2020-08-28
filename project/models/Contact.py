from project.models.CustomAttribute import CustomAttribute
from project.db import get_db

class Contact:
    def __init__(self, id, name, phone, email):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.custom_attributes = []

    @staticmethod
    def load_contact(id):
        db = get_db()

        row = db.execute(
            'SELECT id,name,phone,email FROM contacts WHERE id = ?', 
            (id,) 
        ).fetchone()
 
        if row :
            contact = Contact(row['id'],row['name'],row['phone'],row['email']) 

            contact.load_custom_attributes()

            return contact 

        return None

    @staticmethod
    def load_contacts_by_team_id(team_id):
        contacts = None
        if (team_id):
            db = get_db()

            contacts_rows = db.execute(
                'select c.id, c.name, phone, email from contacts c inner join teams t on c.team_id=t.id where t.id=?',
                (team_id,) 
            ).fetchall()

            contacts = [Contact(row['id'],row['name'],row['phone'],row['email']) for row in contacts_rows if contacts_rows]

            for contact in contacts:
                contact.load_custom_attributes()

        return contacts

    def load_custom_attributes(self):
        if self.id:
            db = get_db()

            ca_rows = db.execute(
                'select ca.id,key,value from custom_attributes ca inner join contacts c on ca.contact_id = c.id where c.id=?',
                (self.id,) 
            ).fetchall()

        self.custom_attributes = [CustomAttribute(contact_id=self.id,id=ca['id'],key=ca['key'],value=ca['value']) for ca in ca_rows if ca_rows]
