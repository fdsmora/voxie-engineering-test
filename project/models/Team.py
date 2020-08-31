from project.db import get_db
from project.models.Contact import Contact
from project.models.Base import Base

class Team(Base):
    def __init__(self, **kwargs):
       Base.__init__(self,**kwargs)
       self.name = kwargs.get('name')
       self.contacts = []

    def get_query_load_all():
        return 'SELECT id,name FROM teams'

    def get_query_load_by_id():
        return 'SELECT id,name FROM teams where id = ?' 

    def get_table_name():
        return 'teams';
    
    def get_table_fields():
        return ['name']

    def get_update_values(self):
        return [self.name,self.id]

    def additional_processing(self):
        self.contacts = Contact.load_contacts_by_team_id(self.id) 
