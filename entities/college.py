class College:
	_id = 1

	def __init__(self, args):
		self.id = College._id
		self.name = args["name"]
		self.short_name = args["short_name"]
		self.area = args["area"]
		self.skills = args["skills"]

		College._id += 1
        
	def __str__(self):
		s = ":College {"
		s += "name: \'" + self.name + "\', "
		s += "short_name: \'" + self.short_name + "\', "
		s += "area: \'" + self.area + "\'}"
		return s
    
	def db_create(self):
		return "CREATE(" + str(self) + ");"

	@staticmethod
	def csv_header():
		return 'id,name,short_name,area,skills'

	def csv_format(self):
		return f'{self.id},{self.name},{self.short_name},{self.area},{":".join(self.skills)}'