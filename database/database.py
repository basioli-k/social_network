from neo4j import GraphDatabase
import shutil, os, sys

sys.path.insert(1, '../entities')

from college import *
from person import *

def add_attribute(header_element):
    integer_values = ["id", "person_id", "college_id", "enrollment_year", "graduate_year", "grade", "id_first", "id_second"]
    date_values = ["date_of_birth", "start_date"]
    array_values = ["skills", "hobbies"]

    if header_element in integer_values:
        return f"{header_element}: toInteger(csv_line.{header_element})"
    elif header_element in date_values:
        return f"{header_element}: date(csv_line.{header_element})"
    elif header_element in array_values:
        return f"{header_element}: split(csv_line.{header_element}, \":\")"
    return f"{header_element}: csv_line.{header_element}"

#napravi da bude singleton
class Database:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_constraint(self, entity):
        cypher = f"CREATE CONSTRAINT {entity.lower()}IdConstraint ON ({entity.lower()}:{entity}) ASSERT {entity.lower()}.id IS UNIQUE"
        with self.driver.session() as session:
            session.run(cypher)


    def get_load_command_entity(self, file_name, header, entity):
        header = header.split(",")
        cypher = f"LOAD CSV WITH HEADERS FROM \"file:///{file_name}\" AS csv_line CREATE (p:{entity}" + "{"
        first = True

        for header_element in header:
            if first:
                cypher += add_attribute(header_element)
                first = False
            else:
                cypher += ", " + add_attribute(header_element)

        cypher += "});"

        return cypher
    
    def load_csv_entities(self, entity):
        cypher = self.get_load_command_entity(entity["file_name"], entity["header"], entity["entity"])
        with self.driver.session() as session:
            result = session.run(cypher)
            print(result)
    
    def get_load_command_relation(self, file_name, header, relation):
        header = header.split(",")
        header_rest = header[2:]

        cypher = f"USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM \"file:///{file_name}\" AS csv_line MATCH (p:Person " + "{id:toInteger(csv_line." + f"{header[0]}" + ")}), (q:"
        
        if "college" in header[1]:
            cypher += "College {id:toInteger(csv_line."
        else:
            cypher += "Person {id:toInteger(csv_line."

        cypher += f"{header[1]}" + ")}) CREATE (p)-" + f"[:{relation} " 
        cypher += "{"
        first = True
        for header_element in header_rest:
            if first:
                cypher += add_attribute(header_element)
                first = False
            else:
                cypher += ", " + add_attribute(header_element)

        cypher += "}]->(q);"    

        return cypher

    def load_csv_relationship(self, rel):
        cypher = self.get_load_command_relation(rel["file_name"], rel["header"], rel["relation"])
        print(cypher)
        with self.driver.session() as session:
            result = session.run(cypher)
            print(result)
    
    def delete_database(self):
        with self.driver.session() as session:
            try:
                session.run("MATCH (a) -[r] -> () DELETE a, r")  #delete all nodes with directed relationships
                session.run("MATCH (a)-[r]-() DELETE a, r;")    #delete all nodes with undirected relatinoships
                session.run("MATCH (a) DELETE a;")              #delete all remaining nodes
            except Exception as ce:
                print(ce.message)
                

if __name__ == "__main__":
    import configparser, json

    config = configparser.ConfigParser()

    config.read("database.cfg", encoding='utf-8')

    db_url = config["database"]["url"] 
    username = config["database"]["username"]
    password = config["database"]["password"]
    import_path = config["database"]["import_path"]   #todo generalizacija onog patha u configu
    entity_info = json.loads(config["database"]["entity_info"])
    relationship_info = json.loads(config["database"]["relationship_info"])

    db = Database(db_url, username, password)

    db.delete_database()

    for filename in os.listdir():
        if filename.endswith(".csv"):
            if os.path.exists(f'{import_path}/{filename}'):
                os.remove(f'{import_path}/{filename}')
            # shutil.copyfile(filename, import_path)      ovo treba pristup iz nekog razloga?
            shutil.move(filename, import_path)

    for entity in entity_info:
        try:
            db.create_constraint(entity["entity"])
        except Exception as ce:
            print(ce.message)
        
        try:
            db.load_csv_entities(entity)
        except Exception as ce:
            print(ce.message)

    for rel in relationship_info:
        try:
            db.load_csv_relationship(rel)
        except Exception as ce:
            print(ce.message)

    db.close()
