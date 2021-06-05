import sys

sys.path.append('../database')
from database import *


class Person:
    _id = 1
    def __init__(self, name, surname, gender = "m", date_of_birth = "01.01.2000.", skills = [], hobbies = [], id = None):
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

    def get_bussiness_recommendation(self, path = "../database/database.cfg", limit = 10):
        db = Database.get_instance(path)
        with db.driver.session() as session:
            result = session.run("MATCH (p:Person {id: $id})-[:ATTENDED]->(:College)-[:SAME_AREA]-(c:College)<-[:ATTENDED]-(recommendation:Person) \
                                WHERE p.id <> recommendation.id RETURN recommendation, c.name, size([x IN p.skills WHERE x IN recommendation.skills]) AS \
                                common_skills ORDER BY common_skills DESC LIMIT $limit;", {"id": self.id, "limit": limit})
            
            bussiness_recommendation = []
            for recommend in result.data():
                rec = recommend["recommendation"]
                bussiness_recommendation.append((Person(rec["name"], rec["surname"], rec["gender"], rec["date_of_birth"], rec["skills"], rec["hobbies"], rec["id"]), recommend["c.name"] ))
            
        return bussiness_recommendation