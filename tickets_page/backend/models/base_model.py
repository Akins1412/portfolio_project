"""Model for all other classes"""
from datetime import datetime
from backend import db


class BaseModel:
    created_at = datetime.utcnow()

    def save(self):
        """Saves a model to the database
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Deletes the a model instance from the database"""
        db.session.delete(self)
        db.session.commit()

    def update(self):
        """Update a Model instance in the database"""
        # db.session.merge(self)
        self.verified = True
        db.session.commit()

    def rollback():
        """Rollback a database commit incase of errors"""
        db.session.rollback()

    def to_dict(self):
        dictionary = {}
        for key in self.__mapper__.c.keys():
            value = getattr(self, key)
            if key == "password":
                continue
            if isinstance(value, datetime):
                dictionary[key] = value.isoformat()
            else:
                dictionary[key] = value
        return dictionary
