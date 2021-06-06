import sys
import random
import pandas as pd
import time

sys.path.append('./entities')
sys.path.append('./database')
sys.path.append('./data_prep')

from database import *
from person import *
from college import *
from db_create import *

from mysql.connector import (connection)

path = "C:/Users/kbasi/Desktop/Faks/4/ljetni/NBP/social_network/database"
class mysql_db:
    #uredeni parovi, ime csv, ime tablice
    tables = [("friendships", "is_friend")  ] #[("people", "person"), ("college", "college"), ("attendance", "attended"), 

    def __init__(self):
        self.cnx = connection.MySQLConnection(user='', password='',
                                        host='127.0.0.1',
                                        database='social_network')
        self.cursor = self.cnx.cursor()

    def delete_database(self):
        for el in reversed(self.tables):
            sql = f"DELETE FROM {el[1]};"
            try:
                self.cursor.execute(sql)
                self.cnx.commit()
            except Exception as mye:
                print("ne ide")

    def fill_database(self):
        for el in self.tables:
            empdata = pd.read_csv(f'./database/{el[0]}.csv', index_col=False, delimiter = ',')
            for i,row in empdata.iterrows():
                sql = f"INSERT INTO {el[1]} VALUES("
                first = True
                for i in range(len(tuple(row))):
                    if first:
                        sql += "%s"
                        first = False
                    else:
                        sql += ", %s"
                sql+=");"
                try:
                    self.cursor.execute(sql, tuple(row))
                    self.cnx.commit()
                except Exception as mye:
                    print("ne ide")

    def friend_recommendation(self):
        pass
    
    def business_recommendation(self):
        pass

    def close(self):
        self.cnx.close()

if __name__ == "__main__":
    #generate_data("./data_prep/data.cfg", "./data_prep/names-by-gender.csv", 200)
    db = mysql_db()
    db.fill_database()