#!/usr/bin/python3

import uuid
from datetime import datetime
import models

"""
basemodel
"""

class BaseModel:
	"""
		intialization of the basemodel
	"""
	def __init__(self, *args, **kwargs):
		"""
			creates an instance of a class basemodel
		"""
		fmt = "%Y-%m-%dT%H:%M:%S.%f"
		if kwargs:
			for key, value in kwargs.items():
				if key == "__class__":
					continue
				elif key == "created_at" or key == "updated_at":
					setattr(self, key, datetime.strptime(value, fmt))
				else:
					setattr(self, key, value)
		else:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.utcnow()
			self.updated_at = datetime.utcnow()
			models.storage.new(self)

	def save(self):
		"""
			saves and updates the time when instancr is created
		"""
		self.updated_at = datetime.utcnow()
		models.storage.save()

	def to_dict(self):
		"""
			converts an instance into a dictionary
		"""
		instance = self.__dict__.copy()
		instance["__class__"] = self.__class__.__name__
		instance["created_at"] = self.created_at.isoformat()
		instance["updated_at"] = self.updated_at.isoformat()
		return (instance)

	def __str__(self):
		"""
			string representations of a created instance
		"""
		return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
