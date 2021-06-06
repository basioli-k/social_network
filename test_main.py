import sys

sys.path.append('./entities')
sys.path.append('./database')

from database import *
from person import *

if __name__ == "__main__":
    person = Person("K", "b", id=79)

    # first_rec = [data[0] for data in person.get_business_recommendation("./database/database.cfg")]
    
    # second_rec = [data[0] for data in person.get_business_recommendation_2("./database/database.cfg")]

    # for person in person.get_personal_recommendation_2("./database/database.cfg"):
    #     print(str(person))

    print(Person.get_max_id("./database/database.cfg"))

    #print(len(set(person.get_personal_recommendation("./database/database.cfg")) & set(person.get_personal_recommendation_2("./database/database.cfg") ) ))

    # c = 0
    # for el1 in first_rec:
    #     for el2 in second_rec:
    #         if el1.id == el2.id:
    #             c += 1

    # print(len(set(first_rec) & set(second_rec)))
    