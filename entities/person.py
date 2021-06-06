import sys
import datetime
import time

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
        else:
            self.id = id
        Person._id += 1          #na ovaj nacin je _id staticka varijabla
        
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
        start = time.time()
        with db.driver.session() as session:
            result = session.run(cypher, {"id": self.id, "first_limit": first_limit, "limit": limit})
            
            bussiness_recommendation = []
            for recommend in result.data():
                rec = recommend["recommendation"]
                bussiness_recommendation.append(Person(rec["name"], rec["surname"], rec["gender"], rec["date_of_birth"], rec["skills"], rec["hobbies"], rec["id"]) )
        end = time.time()
        db.close()
        
        return end-start
    
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
        start = time.time()
        with db.driver.session() as session:
            result = session.run(cypher, {"id": self.id, "first_limit": first_limit, "second_limit": second_limit, "limit": limit})

            personal_recommendation = []
            for recommend in result.data():
                rec = recommend["recommendation"]
                personal_recommendation.append( Person(rec["name"], rec["surname"], rec["gender"], rec["date_of_birth"], rec["skills"], rec["hobbies"], rec["id"]) )
        end = time.time()
        db.close()

        return end-start
    
    @staticmethod
    def get_max_id(path = "../database/database.cfg"):
        db = Database.get_instance(path)
        with db.driver.session() as session:
            return session.run("MATCH (p:Person) RETURN MAX(p.id) as max_id;").single()["max_id"]
        
    #POKOJNE IDEJE
    # #mozemo podesiti da ova funkcija bude pozvana za mlade ljude (jer zelimo da mladi ljudi budu povezani sa mladima), treba adjustati weightove
    # def get_business_recommendation_younger(self, path = "../database/database.cfg", limit = 10):
    #     w1, w2, w3 = (1, 1, 1)  #mozemo setati neke weightove ako zelimo, jer na ovaj nacin gledamo neki relativno mali broj + mali broj + broj zaj skillova
    #     db = Database.get_instance(path)

    #     with db.driver.session() as session:
    #         result = session.run("MATCH (p:Person {id:$id})-[att1:ATTENDED]->(:College)-[:SAME_AREA]-(c:College)<-[att2:ATTENDED]-(recommendation:Person) WHERE p.id <> recommendation.id AND \
    #                             NOT((p)-[:IS_FRIEND]-(recommendation)) RETURN recommendation, c.name, sqrt($w1/(abs(p.date_of_birth.year - recommendation.date_of_birth.year)+1)^2  +\
    #                             $w2/(abs(att1.enrollment_year-att2.enrollment_year)+1)^2 + $w3*size([x IN p.skills WHERE x IN recommendation.skills])^2) \
    #                             AS rating ORDER BY rating DESC LIMIT $limit;", {"id": self.id, "limit": limit, "w1": w1, "w2": w2, "w3": w3})

    #         bussiness_recommendation = []
    #         for recommend in result.data():
    #             rec = recommend["recommendation"]
    #             bussiness_recommendation.append((Person(rec["name"], rec["surname"], rec["gender"], rec["date_of_birth"], rec["skills"], rec["hobbies"], rec["id"]), recommend["c.name"] ))
        
    #     db.close()
        
    #     return bussiness_recommendation

    #vraca broj ljudi s najvecim presjekom skillova i hobija
    # def get_personal_recommendation(self, path = "../database/database.cfg", limit = 10):
    #     db = Database.get_instance(path)

    #     with db.driver.session() as session:
    #         result = session.run("MATCH (p:Person {id:$id})-[:IS_FRIEND]-(:Person)-[:IS_FRIEND]-(recommendation:Person) WHERE p.id <> recommendation.id AND NOT((p)-[:IS_FRIEND]-(recommendation)) \
    #                             RETURN recommendation, (size([x IN p.skills WHERE x IN recommendation.skills]) + size([x IN p.hobbies WHERE x IN recommendation.hobbies])) AS common ORDER BY common DESC LIMIT $limit;", 
    #                             {"id": self.id, "limit": limit})
    #         personal_recommendation = []
    #         for recommend in result.data():
    #             rec = recommend["recommendation"]
    #             personal_recommendation.append( Person(rec["name"], rec["surname"], rec["gender"], rec["date_of_birth"], rec["skills"], rec["hobbies"], rec["id"]) )
        
    #     db.close()

    #     return personal_recommendation

    #preporuka po zajednickim prijateljima
    # def get_personal_recommendation_2(self, path = "../database/database.cfg", limit = 10):
    #     db = Database.get_instance(path)

    #     with db.driver.session() as session:
    #         result = session.run("MATCH (p:Person {id:$id})-[:IS_FRIEND]-(:Person)-[:IS_FRIEND]-(recommendation:Person) WHERE p.id <> recommendation.id \
    #                             AND NOT((p)-[:IS_FRIEND]-(recommendation)) return recommendation, count(recommendation) AS common_friends ORDER BY \
    #                             common_friends DESC LIMIT $limit;", 
    #                             {"id": self.id, "limit": limit})

    #         personal_recommendation = []
    #         for recommend in result.data():
    #             rec = recommend["recommendation"]
    #             personal_recommendation.append( Person(rec["name"], rec["surname"], rec["gender"], rec["date_of_birth"], rec["skills"], rec["hobbies"], rec["id"]) )
        
    #     db.close()

    #     return personal_recommendation
    
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
                                  per["p"]["skills"], per["p"]["hobbies"])
    
    def get_attendance_info(self, path = "../database/database.cfg"):
        db = Database.get_instance(path)
        with db.driver.session() as session:
            result = session.run("MATCH (:Person {id:$id})-[att:ATTENDED]-(c:College) RETURN c, att;", 
                                 {"id" : self.id })
            if not result:
                return None
            else:
                coll, att = result.single()
                return (College({"name" : coll["name"], "short_name" : coll["short_name"], 
                                "area" : coll["area"], "skills" : coll["skills"]}),
                        att["enrollment_year"], att["graduate_year"], att["grade"])                          
                                 
    # def get_college_enroll(self, path = "../database/database.cfg"):
    #     db = Database.get_instance(path)
    #     with db.driver.session() as session:
    #         result = session.run("MATCH (p:Person {name: $name, surname: $surname})-[c:ATTENDED]-() RETURN c.enrollment_year", 
    #                              {"name" : self.name, "surname" : self.surname})
    #         if not result:
    #             return None
    #         else:
    #             for coll in result.data():                     
    #                 return (coll["c.enrollment_year"])                          
    # def get_college_graduate(self, path = "../database/database.cfg"):
    #     db = Database.get_instance(path)
    #     with db.driver.session() as session:
    #         result = session.run("MATCH (p:Person {name: $name, surname: $surname})-[c:ATTENDED]-() RETURN c.graduate_year", 
    #                              {"name" : self.name, "surname" : self.surname})
    #         if not result:
    #             return None
    #         else:
    #             for coll in result.data():                     
    #                 return (coll["c.graduate_year"])                               
    # def get_college_grade(self, path = "../database/database.cfg"):
    #     db = Database.get_instance(path)
    #     with db.driver.session() as session:
    #         result = session.run("MATCH (p:Person {name: $name, surname: $surname})-[c:ATTENDED]-() RETURN c.grade", 
    #                              {"name" : self.name, "surname" : self.surname})
    #         if not result:
    #             return None
    #         else:
    #             for coll in result.data():                     
    #                 return (coll["c.grade"])                               
                                 
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
                                                per["friend"]["skills"], per["friend"]["hobbies"]) )                            
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
                                                per["friend"]["skills"], per["friend"]["hobbies"]) )                            
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
                                                per["friend"]["skills"], per["friend"]["hobbies"]) )                            
                db.close()
                return friends_list

    def get_friends_by_college_info(self, value = "", key = "" , path = "../database/database.cfg"):
        db = Database.get_instance(path)
        with db.driver.session() as session:
            result = session.run(f"MATCH (p:Person {{name: $name, surname: $surname}})-[:IS_FRIEND]-(friend:Person)-[a:ATTENDED {{ {key} : $value}}]-(c:COLLEGE) RETURN friend;", 
                                 {"name" : self.name, "surname" : self.surname, "value" : value})
            friends_list = []
            if not result:
                return None
            else:
                for per in result.data():
                    friends_list.append( Person(per["friend"]["name"], per["friend"]["surname"], 
                                                per["friend"]["gender"], per["friend"]["date_of_birth"], 
                                                per["friend"]["skills"], per["friend"]["hobbies"]) )                            
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
                                                per["friend"]["skills"], per["friend"]["hobbies"]) )                            
                db.close()
                return friends_list                             
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 	
