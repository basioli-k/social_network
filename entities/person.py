class Person:
        def __init__(self, name, surname, gender = "m", date_of_birth = "01.01.2000.", skills = [], hobbies = []):
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

        def __hash__(self):
            return hash((self.name, self.surname))

        def __eq__(self, person):
            if isinstance(person, Person):
                return (self.name == person.name and self.surname == person.surname)
            return False
            
        def db_create(self):
            return "CREATE( " + str(self) + ");"