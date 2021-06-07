import sys
import datetime

sys.path.append('../database')
from database import *

OLD_LIMIT = 26
from college import *

class Person:
    _id = 1
    def __init__(self, name, surname, gender = "m", date_of_birth = datetime.date(1980, 1, 1), skills = [], hobbies = [], id = None):
        self.name =  name
        self.surname = surname
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.skills = skills
        self.hobbies = hobbies
        if id == None:
            self.id = Person._id
            Person._id += 1
        else:
            self.id = id
        
    def __str__(self):
        s = ":Person {"
        s += "name: \'" + self.name + "\', "
        s += "surname: \'" + self.surname + "\', "
        s += "gender: \'" + self.gender + "\', "
        s += "date_of_birth: \'" + str(self.date_of_birth) + "\', "
        s += "skills: \'" + str(self.skills) + "\', "
        s += "hobbies: \'" + str(self.hobbies) + "\'}"
        return s

    def __hash__(self):
        return hash((self.name, self.surname))

    def __eq__(self, person):
        if isinstance(person, Person):
            return (self.name == person.name and self.surname == person.surname)
        return False
    
    @staticmethod
    def csv_header():
        return 'id,name,surname,gender,date_of_birth,skills,hobbies'

    def csv_format(self):
        return f'{self.id},{self.name},{self.surname},{self.gender},{self.date_of_birth},{":".join(self.skills)},{":".join(self.hobbies)}'

    def db_create(self):
        return "CREATE( " + str(self) + ");"

    
    #daje nam ljude iz istog podrucja, za starije korisnike suzi po skillovima prvo pa po godini rodenja, za mlade radi obrnuto
    def get_business_recommendation(self, path = "../database/database.cfg", limit = 10):
        first_limit = 2 * limit

        cypher = "MATCH (p:Person {id: $id})-[:ATTENDED]->(:College)-[:SAME_AREA]-(:College)<-[:ATTENDED]-(recommendation:Person) \
                WHERE p.id <> recommendation.id AND NOT((p)-[:IS_FRIEND]-(recommendation))"

        if datetime.date.today().year - self.date_of_birth.year > OLD_LIMIT:
            cypher += " WITH p, recommendation, size([x IN p.skills WHERE x IN recommendation.skills]) AS common_skills ORDER BY common_skills DESC LIMIT $first_limit"
            cypher += " RETURN recommendation, abs(p.date_of_birth.year - recommendation.date_of_birth.year) AS birth_delta ORDER BY birth_delta DESC LIMIT $limit;"
        else:
            cypher += " WITH p, recommendation, abs(p.date_of_birth.year - recommendation.date_of_birth.year) AS birth_delta ORDER BY birth_delta DESC LIMIT $first_limit"
            cypher += " RETURN recommendation, size([x IN p.skills WHERE x IN recommendation.skills]) AS common_skills ORDER BY common_skills DESC LIMIT $limit;"

        db = Database.get_instance(path)
        with db.driver.session() as session:
            result = session.run(cypher, {"id": self.id, "first_limit": first_limit, "limit": limit})
            
            bussiness_recommendation = []
            for recommend in result.data():
                rec = recommend["recommendation"]
                bussiness_recommendation.append(Person(rec["name"], rec["surname"], rec["gender"], rec["date_of_birth"], rec["skills"], rec["hobbies"], rec["id"]) )
        
        db.close()
        
        return bussiness_recommendation
    
    def get_personal_recommendation(self, path = "../database/database.cfg", limit = 10):
        first_limit = 3 * limit
        second_limit = 2 * limit
        # find first_limit people with most common friends
        cypher = "MATCH (p:Person {id:$id})-[:IS_FRIEND]-(:Person)-[:IS_FRIEND]-(recommendation:Person) \
                WHERE p.id <> recommendation.id AND NOT((p)-[:IS_FRIEND]-(recommendation)) \
                WITH p, recommendation, count(recommendation) AS common_friends ORDER BY common_friends DESC LIMIT $first_limit"
        #out of those choose second_limit people who are the closest by year of birth
        cypher += " WITH p, recommendation, abs(recommendation.date_of_birth.year - p.date_of_birth.year) AS birth_delta ORDER BY birth_delta LIMIT $second_limit"
        # out of those choose limit people who have the biggest intersection in skills and hobbies
        cypher += " RETURN recommendation, size([skill IN p.skills WHERE skill IN recommendation.skills]) + \
                size([hobby IN p.hobbies WHERE hobby IN recommendation.hobbies]) AS common ORDER BY common DESC LIMIT $limit;"

        db = Database.get_instance(path)
        with db.driver.session() as session:
            result = session.run(cypher, {"id": self.id, "first_limit": first_limit, "second_limit": second_limit, "limit": limit})

            personal_recommendation = []
            for recommend in result.data():
                rec = recommend["recommendation"]
                personal_recommendation.append( Person(rec["name"], rec["surname"], rec["gender"], rec["date_of_birth"], rec["skills"], rec["hobbies"], rec["id"]) )
        
        db.close()
        if len(personal_recommendation) == 0:
            return self.get_business_recommendation(path, limit)
            
        return personal_recommendation
    
    @staticmethod
    def get_max_id(path = "../database/database.cfg"):
        db = Database.get_instance(path)
        with db.driver.session() as session:
            return session.run("MATCH (p:Person) RETURN MAX(p.id) as max_id;").single()["max_id"]
    
    @staticmethod
    def get_max_id(path = "../database/database.cfg"):
        db = Database.get_instance(path)
        with db.driver.session() as session:
            return session.run("MATCH (p:Person) RETURN MAX(p.id) as max_id;").single()["max_id"]
        
    @staticmethod
    def get_person_by_name_surname(user_name, user_surname, path = "../database/database.cfg"):
        db = Database.get_instance(path)
        with db.driver.session() as session:
            result = session.run("MATCH (p:Person {name: $name, surname: $surname}) RETURN p;", 
                                 {"name" : user_name, "surname" : user_surname})
            if not result:
                return None
            else:
                for per in result.data():
                    return Person(per["p"]["name"], per["p"]["surname"], 
                                  per["p"]["gender"], per["p"]["date_of_birth"], 
                                  per["p"]["skills"], per["p"]["hobbies"], per["p"]["id"])
    
    def get_attendance_info(self, path = "../database/database.cfg"):
        db = Database.get_instance(path)
        with db.driver.session() as session:
            result = session.run("MATCH (p:Person {id: $id})-[att:ATTENDED]-(c:College) RETURN c, att;", 
                                 {"id" : self.id} )
            if not result:
                return None
            else:
                coll, att = result.single()
                return (College({"name" : coll["name"], "short_name" : coll["short_name"], 
                                "area" : coll["area"], "skills" : coll["skills"]}),
                        att["enrollment_year"], att["graduate_year"], att["grade"])                                                
                                 
    def get_all_friends(self, path = "../database/database.cfg"):
        db = Database.get_instance(path)
        with db.driver.session() as session:
            result = session.run("MATCH (p:Person {name: $name, surname: $surname})--(friend:Person) RETURN friend;", 
                                 {"name" : self.name, "surname" : self.surname})
            friends_list = []
            if not result:
                return None
            else:
                for per in result.data():
                    friends_list.append( Person(per["friend"]["name"], per["friend"]["surname"], 
                                                per["friend"]["gender"], per["friend"]["date_of_birth"], 
                                                per["friend"]["skills"], per["friend"]["hobbies"], per["friend"]["id"] ))                            
                return friends_list                 
                                 
    def get_friends_by_sur_name(self, value = "", key = "" , path = "../database/database.cfg"):
        db = Database.get_instance(path)
        with db.driver.session() as session:
            result = session.run(f"MATCH (p:Person {{name: $name, surname: $surname}})-[:IS_FRIEND]-(friend:Person {{ {key}: $value}}) RETURN friend;", 
                                 {"name" : self.name, "surname" : self.surname, "value" : value})
            friends_list = []
            if not result:
                return None
            else:
                for per in result.data():
                    friends_list.append( Person(per["friend"]["name"], per["friend"]["surname"], 
                                                per["friend"]["gender"], per["friend"]["date_of_birth"], 
                                                per["friend"]["skills"], per["friend"]["hobbies"], per["friend"]["id"]  ))                           
                db.close()
                return friends_list  
                            
    def get_friends_by_birthyear(self, year, path = "../database/database.cfg"):
        db = Database.get_instance(path)
        with db.driver.session() as session:
            result = session.run(f"MATCH (p:Person {{name: $name, surname: $surname}})-[:IS_FRIEND]-(friend:Person) WHERE friend.date_of_birth.year = $value RETURN friend;", 
                                 {"name" : self.name, "surname" : self.surname, "value" : year})
            friends_list = []
            if not result:
                return None
            else:
                for per in result.data():
                    friends_list.append( Person(per["friend"]["name"], per["friend"]["surname"], 
                                                per["friend"]["gender"], per["friend"]["date_of_birth"], 
                                                per["friend"]["skills"], per["friend"]["hobbies"], per["friend"]["id"]  ))                            
                db.close()
                return friends_list

    def get_friends_by_college_info(self, value = "", key = "" , path = "../database/database.cfg"):
        db = Database.get_instance(path)
        with db.driver.session() as session:
            result = session.run(f"MATCH (p:Person {{name: $name, surname: $surname}})-[:IS_FRIEND]-(friend:Person)-[a:ATTENDED {{ {key} : $value}}]-() RETURN friend;", 
                                 {"name" : self.name, "surname" : self.surname, "value" : value})
            friends_list = []
            if not result:
                return None
            else:
                for per in result.data():
                    friends_list.append( Person(per["friend"]["name"], per["friend"]["surname"], 
                                                per["friend"]["gender"], per["friend"]["date_of_birth"], 
                                                per["friend"]["skills"], per["friend"]["hobbies"], per["friend"]["id"]  ))                            
                db.close()
                return friends_list                            
                                 
    def get_friends_by_college(self, college, path = "../database/database.cfg"):
        db = Database.get_instance(path)
        with db.driver.session() as session:
            result = session.run("MATCH (p:Person {name: $name, surname: $surname})-[:IS_FRIEND]-(friend:Person)-[:ATTENDED]-(c:College { short_name: $value}) RETURN friend;", 
                                 {"name" : self.name, "surname" : self.surname, "value" : college})
            friends_list = []
            if not result:
                return None
            else:
                for per in result.data():
                    friends_list.append( Person(per["friend"]["name"], per["friend"]["surname"], 
                                                per["friend"]["gender"], per["friend"]["date_of_birth"], 
                                                per["friend"]["skills"], per["friend"]["hobbies"], per["friend"]["id"] ))                            
                db.close()
                return friends_list     
                        
    def make_friendship(self, person, path = "../database/database.cfg"):
        db = Database.get_instance(path)
        with db.driver.session() as session:
            result = session.run("MATCH (p:Person {name: $name, surname: $surname})-[if:IS_FRIEND]-(friend:Person {name : $name_f,surname:  $surname_f}) RETURN if, count(if) as broj;",
                                 {"name" : self.name, "surname" : self.surname, "name_f" : person.name, "surname_f" : person.surname})
            data = result.single()
            if not data:
                #print("usla")
                #not friends - continue
                result = session.run("MATCH (p:Person {name: $name, surname: $surname}),(f:Person {name : $name_f,surname:  $surname_f}) CREATE (p)-[if:IS_FRIEND {start_date: date()}]->(f) RETURN if;",
                                 {"name" : self.name, "surname" : self.surname, "name_f" : person.name, "surname_f" : person.surname})
                if not result:
                    db.close()
                    return "Error - not added"
                else:
                    db.close()
                    return True
            else:
                db.close()
                return False

    def add_person_to_db(self,  path = "../database/database.cfg"):
        db = Database.get_instance(path)
        with db.driver.session() as session:
            result = session.run("CREATE (p:Person {name : $name, surname : $surname, date_of_birth : $date, gender : $g, skills : $skills, hobbies : $hobbies, id : $id})", 
                                   {"name" : self.name, "surname" : self.surname, "g" : self.gender, "date" : self.date_of_birth, "skills" : self.skills, "hobbies" : self.hobbies, "id" : self.id})
            db.close() 
            return                       
                              
    def add_to_college(self, s_name, ey, gy, grade, path = "../database/database.cfg" ):
        db = Database.get_instance(path)
        with db.driver.session() as session:
            result = session.run("MATCH (p:Person {id : $id}),(c:College {short_name : $s_name}) CREATE (p)-[:ATTENDED {enrollment_year : $ey, graduate_year : $gy, grade : $grade}]->(c);",
                                 {"id" : self.id, "s_name" : s_name, "ey" : ey, "gy" : gy, "grade" : grade})                     
            db.close()                     
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 	
