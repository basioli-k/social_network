#!/usr/bin/env python3

if __name__ == "__main__":
	import configparser, json
	
	config = configparser.ConfigParser()

	config.read("data.ini")

	data = eval(config["data"]["data"])

	for element in data:
		print("College name:", element["name"])
		print("Short name:", element["short_name"])
		print("Area:",element["area"])
		print("Skills:",element["skills"])