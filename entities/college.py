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