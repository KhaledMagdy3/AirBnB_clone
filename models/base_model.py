#!/usr/bin/python3
"""
Base Model
"""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """BaseModel Class"""

    def __init__(self):
        """for Public instance attributes
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """__str__

        Returns:
            String: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        """to save the update
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """to_dict

        Returns:
            dict: dictionary representation
        """
        dictFormat = {}
        dictFormat["__class__"] = self.__class__.__name__
        for key, val in self.__dict__.items():
            if isinstance(val, datetime):
                dictFormat[key] = val.isoformat()
            else:
                dictFormat[key] = val
        return dictFormat
