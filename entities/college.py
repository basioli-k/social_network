class College:

	def __init__(self, args):
		self.name = args["name"]
		self.short_name = args["short_name"]
		self.area = args["area"]
		self.skills = args["skills"]

	def print_college(self): #samo za testiranje
		print("College name:", self.name)
		print("Short name:", self.short_name)
		print("Area:", self.area)
		print("Skills:", self.skills)
		
	# def __init__ (self, name, short_name, area):
	# 	self.name = name
	# 	self.short_name = short_name
	# 	self.area = area
        
	def __str__(self):
		s = ":College {"
		s += "name: \'" + self.name + "\', "
		s += "short_name: \'" + self.short_name + "\', "
		s += "area: \'" + self.area + "\'}"
		return s
    
	def db_create(self):
		return "CREATE(" + str(self) + ");"