import sys

sys.path.append('./entities')
sys.path.append('./database')

from database import *
from person import *

if __name__ == "__main__":
    person = Person("K", "b", id=134)

    for data in person.get_bussiness_recommendation("./database/database.cfg"):
        p, col = data
        print(str(p))
        print(col)