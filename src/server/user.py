import Database

class User:
	def __init__(self, name, email):
		self.name = name
		self.email = email

	def user_creation(self, db):
		"""user creation returns error string if unsuccessfull"""
		if (db.query("select '%s' from db") % (self.name)) != self.name):
			db.update("insert '%s") % (self.name)
		else:
			return "Name already exists!! Please input another name:"