from project.db import get_db
from project.models.Base import Base

class CustomAttribute(Base):
    def __init__(self,**kwargs):
        Base.__init__(self,**kwargs)
        self.contact_id = kwargs['contact_id']
        self.key = kwargs['key']
        self.value = kwargs['value']

    def get_query_load_all():
        return 'SELECT * FROM custom_attributes'

    def get_query_load_by_id():
        return 'SELECT * FROM custom_attributes where id = ?' 

    def get_table_name():
        return 'custom_attributes';
    
    def get_table_fields():
        return ['key','value']

    def get_update_values(self):
        return [self.key,self.value,self.id]

    def additional_processing(self):
        pass
