from project.models.CustomAttribute import CustomAttribute
from project.db import get_db

class Contact:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.team_id = kwargs.get('team_id')
        self.name = kwargs.get('name')
        self.phone = kwargs.get('phone')
        self.email = kwargs.get('email')
        self.custom_attributes = []

    def update(self):
        db = get_db()

        row = db.execute(
            'UPDATE contacts SET name=?,phone=?,email=? WHERE id = ?', 
            (self.name,self.phone,self.email,self.id,) 
        ).fetchone()
 
        db.commit()
        

    @staticmethod
    def load_contact(id):
        db = get_db()

        row = db.execute(
            'SELECT * FROM contacts WHERE id = ?', 
            (id,) 
        ).fetchone()
 
        if row :
            contact = Contact(id=row['id'],team_id=row['team_id'],name=row['name'],phone=row['phone'],email=row['email']) 

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

            contacts = [Contact(id=row['id'],name=row['name'],phone=row['phone'],email=row['email']) for row in contacts_rows if contacts_rows]

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
