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

    person = Person("k","b","m", id= 134)

    print(person.get_attendance_info("./database/database.cfg"))