from project.db import get_db

class CustomAttribute:
    def __init__(self,**kwargs):
        self.contact_id = kwargs['contact_id']
        self.id = kwargs['id']
        self.key = kwargs['key']
        self.value = kwargs['value']

    def update(self):
        db = get_db()

        db.execute(
            'UPDATE custom_attributes set contact_id=?, key=?, value=? WHERE id=?', 
            (self.contact_id, self.key, self.value, self.id) 
        ).fetchone()

        db.commit()

