from project.db import get_db
from abc import ABC, abstractmethod

class Base (ABC):
    db = None

    def __init__(self,**kwargs):
        self.id=kwargs.get('id')

    @classmethod
    @abstractmethod
    def get_query_load_all(cls):
        pass

    @classmethod
    @abstractmethod
    def get_query_load_by_id(cls):
        pass

    @classmethod
    @abstractmethod
    def get_table_name(cls):
        pass

    @classmethod
    @abstractmethod
    def get_table_fields(cls):
        pass

    @abstractmethod
    def additional_processing(self):
        pass

    @abstractmethod
    def get_update_values(self):
        pass

    @classmethod
    def process(cls, rows):
        return [cls(**r) for r in rows if rows] 
 
    @classmethod
    def load_all(cls):
        Base.get_db()

        rows = Base.db.execute(cls.get_query_load_all()).fetchall()

        return cls.process(rows)

    @classmethod
    def load_by_id(cls, id):
        Base.get_db()

        row = Base.db.execute(cls.get_query_load_by_id(), (id,)).fetchone()

        if row:
            instance = cls(**row)

            instance.additional_processing()
            return instance

        return None

    @classmethod
    def delete(cls,id):
        Base.get_db()
        Base.db.execute(cls.get_delete_query(), (id,))
        Base.db.commit()

    def update(self):
        db = get_db()

        cls = type(self)
        db.execute(cls.get_update_query(), self.get_update_values())
 
        db.commit()

    @classmethod
    def get_update_query(cls):
        return 'UPDATE {} SET {} WHERE id = ?'.format(cls.get_table_name(), ",".join(map(lambda i: i + '=?',cls.get_table_fields())))

    @classmethod
    def get_delete_query(cls):
        return 'DELETE FROM {} WHERE id = ?'.format(cls.get_table_name())

    @classmethod
    def get_db(cls):
        cls.db = get_db()
