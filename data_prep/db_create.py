#!/usr/bin/env python3

import sys
sys.path.append('../entities')

from college import *
from person import *
from itertools import combinations
import random
import datetime
import pandas as pd
import codecs
import time
import os.path

MAX_GENERATING_TIME = 5

MIN_BIRTH_YEAR = 1980
MAX_BIRTH_YEAR = 2000
MAX_YEAR = 2020

MIN_HOBBIES = 3
MAX_HOBBIES = 8

MIN_FRIENDS = 0
MAX_FRIENDS = 20

MIN_SKILLS = 0
MAX_SKILLS = 5
MIN_COLLEGE_SKILLS = 3
MAX_COLLEGE_SKILLS = 8

POPULATION = 200

COLLEGE_ATTENDECE = 0.9

def delete_file(path):
    if os.path.exists(path):
        os.remove(path)

def print_to_file(path, header, element):
    standard_output = sys.stdout
    if (not os.path.exists(path)):
        with open(path, 'a', encoding="utf-8") as file:
            sys.stdout = file
            print(header)

    with open(path, 'a',  encoding="utf-8") as file:
        sys.stdout = file   
        print(element)

    sys.stdout = standard_output

def generate_person():
    name_and_gender = df_names.sample()
    gender = name_and_gender.iloc[0,1]
    name = name_and_gender.iloc[0,0].capitalize()
    surname = random.choice(surnames)
    date_of_birth = datetime.date(random.randint(MIN_BIRTH_YEAR,MAX_BIRTH_YEAR),random.randint(1,12),random.randint(1,28))
    skills = random.sample(all_skills,random.randint(MIN_SKILLS,MAX_SKILLS))
    hobbies = random.sample(hobbies_data,random.randint(MIN_HOBBIES,MAX_HOBBIES))
    return Person(name, surname, gender, date_of_birth, skills, hobbies)

def generate_people(n):
    people=[]
    start = time.time()
    end = time.time()
    while( len(people) <= n and end - start <= MAX_GENERATING_TIME ):
        people.append(generate_person())
        people = list(set(people))
        end = time.time()
    return people

def db_create_friendship(person1, person2):
    year = max(person1.date_of_birth.year,person2.date_of_birth.year) +18
    if( year > 2020):
        return
    start_date = datetime.date(random.randint(year,MAX_YEAR),random.randint(1,12),random.randint(1,28))

    print_to_file("../database/friendships.csv", "id_first,id_second,start_date", f"{person1.id},{person2.id},{start_date}")

    s = "MATCH (p1" + str(person1) + "), (p2" + str(person2) + ")\n"
    s += "CREATE (p1)-[:IS_FRIEND {start_date: " + str(start_date) + "}]->(p2);"
    return s

def create_friendships(people):
    s = ""
    delete_file("../database/friendships.csv")
    for person in people:
        friends = random.sample(people,random.randint(MIN_FRIENDS,MAX_FRIENDS))
        for friend in friends:
            if(person is not friend):
                s += db_create_friendship(person, friend) + "\n"
    return s

def db_create_attendence(person, college):
    enrollment_year = random.randint(person.date_of_birth.year + 18,2020)
    graduate_year = enrollment_year + random.randint(5,10)
    grade = random.randint(2,5)

    print_to_file("../database/attendance.csv", "person_id,college_id,enrollment_year,graduate_year,grade", f"{person.id},{college.id},{enrollment_year},{graduate_year},{grade}")

    s = "MATCH (p" + str(person) + "), (s" + str(college) + ")\n"
    s += "CREATE (p)-[:ATTENDED {enrollment_year: \'" + str(enrollment_year) + "\', "
    if graduate_year < 2020:
        s += "graduate_year: \'" + str(graduate_year) + "\', "
    s += "grade: \'" + str(grade) + "\'}]->(s);"
    return s

def create_attendence(people, colleges):
    s = ""
    delete_file("../database/attendance.csv")
    for person in people:
        college = random.choice(colleges)
        person.skills= list(set(person.skills).union(random.sample(college.skills,random.randint(MIN_COLLEGE_SKILLS,MAX_COLLEGE_SKILLS))))
        s += db_create_attendence(person, college) + "\n"
        s += "MATCH (p" + str(person) + ")\n"
        s += "SET p.skills = \'" + str(person.skills) + "\';"

def same_area(colleges):
    for combination in combinations(colleges, 2):
        if combination[0].area == combination[1].area:
            print_to_file("../database/same_area.csv", "id_first_college,id_second_college",f"{combination[0].id},{combination[1].id}" )
        


if __name__ == "__main__":
    import configparser, json

    config = configparser.ConfigParser()
    config.read("data.cfg", encoding='utf-8')

    data = json.loads(config["data"]["colleges"])

    colleges = []
    all_skills = set()

    for element in data:
        college = College(element)
        colleges.append( college )
        all_skills.update(set(college.skills))
	
    hobbies_data = json.loads(config["data"]["hobbies"])

    df_names = pd.read_csv("names-by-gender.csv")

    surnames = json.loads(config["data"]["surnames"])

    people = generate_people(POPULATION)

    create_attendence(people, colleges)
    create_friendships(people)  

    delete_file("../database/people.csv")
    for person in people:
        print_to_file("../database/people.csv", Person.csv_header(), person.csv_format())
    
    delete_file("../database/college.csv")
    for college in colleges:
        print_to_file("../database/college.csv", College.csv_header(), college.csv_format())

    same_area(colleges)
        