#!/usr/bin/python3
"""
creates an instance of user
"""
from models.base_model import BaseModel

class User(BaseModel):
	"""
		creates an instance of an user
	"""
	email = ""
	password = ""
	first_name = ""
	last_name = ""
