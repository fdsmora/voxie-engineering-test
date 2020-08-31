from project.models.CustomAttribute import CustomAttribute
from project.db import get_db
from project.models.Base import Base

class Contact(Base):
    def __init__(self, **kwargs):
        Base.__init__(self,**kwargs)
        self.team_id = kwargs.get('team_id')
        self.name = kwargs.get('name')
        self.phone = kwargs.get('phone')
        self.email = kwargs.get('email')
        self.custom_attributes = []

    def get_query_load_all():
        return 'SELECT * FROM contacts'

    def get_query_load_by_id():
        return 'SELECT * FROM contacts where id = ?' 

    def get_table_name():
        return 'contacts';
    
    def get_table_fields():
        return ['name', 'phone', 'email']

    def get_update_values(self):
        return [self.name,self.phone,self.email,self.id]

    def additional_processing(self):
        self.load_custom_attributes() 

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

    @staticmethod
    def load_contacts_by_phone(phone):
        if (phone):
            db = get_db()
 
            rows = db.execute(
                'select * from contacts where phone =?', (phone,) 
            ).fetchall()
 
            return [Contact(id=row['id'],name=row['name'],email=row['email'],phone=row['phone'],team_id=row['team_id']) for row in rows if rows]

        return None 

    def load_custom_attributes(self):
        if self.id:
            db = get_db()

            ca_rows = db.execute(
                'select ca.id,key,value from custom_attributes ca inner join contacts c on ca.contact_id = c.id where c.id=?',
                (self.id,) 
            ).fetchall()

        self.custom_attributes = [CustomAttribute(contact_id=self.id,id=ca['id'],key=ca['key'],value=ca['value']) for ca in ca_rows if ca_rows]
