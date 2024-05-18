#!/usr/bin/python3
"""
Base Model
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
	"""BaseModel Class"""

	def __init__(self, *args, **kwargs):
		"""Instance Constructor
		"""
		if kwargs:
			for key, value in kwargs.items():
				if key != "__class__":
					if key == "updated_at":
						self.updated_at = datetime.fromisoformat(value)
					elif key == "created_at":
						self.created_at = datetime.fromisoformat(value)
					else:
						setattr(self, key, value)
		else:
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
		class_dict = self.__dict__.copy()
		class_dict["__class__"] = self.__class__.__name__
		class_dict["updated_at"] = self.updated_at.isoformat()
		class_dict["created_at"] = self.created_at.isoformat()
		return class_dict
