#!/usr/bin/env python3

import sys
sys.path.insert(1, '../entities')
sys.path.insert(2, '../database')

from database import *

from college import *

if __name__ == "__main__":
	import configparser, json
	
	config = configparser.ConfigParser()
	config.read("data.cfg", encoding='utf-8')

	data = json.loads(config["data"]["colleges"])

	colleges = []

	d = Database.get_instance("../database/database.cfg")

	for element in data:
		colleges.append( College(element) )
	
	for college in colleges:
		college.print_college()

	print("--------------------------------------------------------------------")
	#pogledajte kolike presjeke imate
	for el1 in colleges:
		for el2 in colleges:
			if el1.short_name != el2.short_name:
				print(el1.short_name, "and", el2.short_name, "have intersection:", len(set(el1.skills).intersection( set(el2.skills) ) ) )