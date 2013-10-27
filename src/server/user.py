import database

class User:
	db = database
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.computers = get_computers

	def user_creation(self, db):
		"""user creation returns error string if unsuccessful"""

		if ((db.query("select '%s' from db") % (self.name)) != self.name):
			db.update("insert '%s") % (self.name)
			return null
		else:
			return "Name already exists!! Please input another name:"

	
