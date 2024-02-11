#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel
from models.user import User
"""
used to store a class instance
"""

class FileStorage:
	"""
		class intialization of FileStorage
	"""
	__file_path = "database.json"
	__objects = {}

	def all(self):
		"""
			dispalys all created instance of class filestorage
		"""
		return (FileStorage.__objects)

	def new(self, obj):
		"""
			used to create a new istance of a using the arguement provided of obj
		"""
		if obj:
			key = "{}.{}".format(type(obj).__name__, obj.id)
			FileStorage.__objects[key] = obj

	def save(self):
		"""
			serialize an instance into a json file
		"""
		with open(FileStorage.__file_path, mode="w", encoding='utf-8') as files:
			new_dict = {key:value.to_dict() for key, value in FileStorage.__objects.items()}
			json.dump(new_dict, files)

	def reload(self):
		"""
			deserialize an isntance form a json file yo a dictionary
		"""
		try:
			with open(FileStorage.__file_path, mode="r", encoding="utf-8") as files:
				loaded = json.load(files)
				for key, value in loaded.items():
					value = eval(value["__class__"])(**value)
					FileStorage.__objects[key] = value
		except Exception:
			pass			
