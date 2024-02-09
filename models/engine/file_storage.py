#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel
from models.user import User
"""
"""

class FileStorage:
	"""
	"""
	__file_path = "database.json"
	__objects = {}

	def all(self):
		"""
		"""
		return (FileStorage.__objects)

	def new(self, obj):
		"""
		"""
		if obj:
			key = "{}.{}".format(type(obj).__name__, obj.id)
			FileStorage.__objects[key] = obj

	def save(self):
		"""
		"""
		with open(FileStorage.__file_path, mode="w", encoding='utf-8') as files:
			new_dict = {key:value.to_dict() for key, value in FileStorage.__objects.items()}
			json.dump(new_dict, files)

	def reload(self):
		"""
		"""
		try:
			with open(FileStorage.__file_path, mode="r", encoding="utf-8") as files:
				loaded = json.load(files)
				for key, value in loaded.items():
					value = eval(value["__class__"])(**value)
					FileStorage.__objects[key] = value
		except Exception:
			pass			
