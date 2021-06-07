import sys
sys.path.append('../database')
from database import *

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
    
	@staticmethod
	def get_all_skills_from_college(s_name, path = "../database/database.cfg"):
		db = Database.get_instance(path)
		with db.driver.session() as session: 
			result = session.run("MATCH (c:College {short_name: $name}) RETURN c.skills AS s;", {"name" : s_name})
			if not result:
				return None
			else:
				s = result.single()
				db.close()
				return s["s"]