import sys
import random
import time

sys.path.append('./entities')
sys.path.append('./database')
sys.path.append('./data_prep')

from database import *
from person import *
from college import *
from db_create import *

if __name__ == "__main__":

    for i in range(50, 1050, 50):
        POPULATION = i
        generate_data("./data_prep/data.cfg", "./data_prep/names-by-gender.csv", POPULATION)
        fill_database("./database/database.cfg")
        for i in range(10): # za 10 razlicitih ljudi ovo ucini
            person = Person("K", "b", id=random.randint(1, POPULATION))
            t = person.get_personal_recommendation("./database/database.cfg")
            print_to_file("./analysis/personal.csv", "population,time",f"{POPULATION},{t}")

            t = person.get_business_recommendation("./database/database.cfg") 
            print_to_file("./analysis/business.csv", "population,time",f"{POPULATION},{t}")