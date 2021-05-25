class Person:
        def __init__(self, name, surname, gender, date_of_birth, skills, hobbies):
            self.name =  name
            self.surname = surname
            self.gender = gender
            self.date_of_birth = date_of_birth
            self.skills = skills
            self.hobbies = hobbies
            
        def __str__(self):
            s = ":Person {"
            s += "name: \'" + self.name + "\', "
            s += "surname: \'" + self.surname + "\', "
            s += "gender: \'" + self.gender + "\', "
            s += "date_of_birth: \'" + str(self.date_of_birth) + "\', "
            if self.skills != "None":
                s += "skills: \'" + str(self.skills) + "\', "
            s += "hobbies: \'" + str(self.hobbies) + "\'}"
            return s
            
        def db_create(self):
            return "CREATE( " + str(self) + ");"