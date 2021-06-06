#!/usr/bin/env python3

import sys
sys.path.append('../entities')

from college import *
from person import *
from itertools import combinations
from scipy.stats import truncnorm
import random
import datetime
import pandas as pd
import codecs
import time
import os.path

POPULATION = 200

MAX_GENERATING_TIME = 5

MIN_BIRTH_DATE = datetime.date(1980, 1, 1)
MAX_BIRTH_DATE = datetime.date(2000, 1, 1)
MAX_DATE = datetime.date.today()

MEAN_HOBBIES = 6
SD_HOBBIES = 1
MIN_HOBBIES = 4
MAX_HOBBIES = 10

MEAN_SKILLS = 2
SD_SKILLS = 1
MIN_SKILLS = 0
MAX_SKILLS = 5

MEAN_COLLEGE_SKILLS = 7
SD_COLLEGE_SKILLS = 3
MIN_COLLEGE_SKILLS = 4
MAX_COLLEGE_SKILLS = 10

SD_GRADE = 0.5
GRADE_MEAN_FACTOR = 3

MEAN_FRIENDS = POPULATION * 0.05

def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

def random_date( start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date

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

def generate_person(df_names, surnames, all_skills, hobbies_data):
    name_and_gender = df_names.sample()
    gender = name_and_gender.iloc[0,1]
    name = name_and_gender.iloc[0,0].capitalize()
    surname = random.choice(surnames)
    normalSkills = get_truncated_normal(mean=MEAN_SKILLS, sd=SD_SKILLS, low=MIN_SKILLS, upp=MAX_SKILLS)
    normalHobbies = get_truncated_normal(mean=MEAN_HOBBIES, sd=SD_HOBBIES, low=MIN_HOBBIES, upp=MAX_HOBBIES)
    date_of_birth = random_date(MIN_BIRTH_DATE, MAX_BIRTH_DATE)
    skills = random.sample(all_skills,round(normalSkills.rvs()))
    hobbies = random.sample(hobbies_data,round(normalHobbies.rvs()))
    return Person(name, surname, gender, date_of_birth, skills, hobbies)

def generate_people(n, df_names, surnames, all_skills, hobbies_data):
    people=[]
    start = time.time()
    end = time.time()
    while( len(people) < n and end - start <= MAX_GENERATING_TIME ):
        people.append(generate_person(df_names, surnames, all_skills, hobbies_data))
        people = list(set(people))
        end = time.time()
    return people

def db_create_friendship(person1, person2):
    date = max(person1.date_of_birth,person2.date_of_birth) + datetime.timedelta(days=18 * 365)
    if( date > MAX_DATE):
        return
    start_date = random_date( date, MAX_DATE)

    print_to_file("./database/friendships.csv", "id_first,id_second,start_date", f"{person1.id},{person2.id},{start_date}")

def create_friendships(pop, mean, people):
    delete_file("./database/friendships.csv")
    friendCombinations = list (combinations(people, 2))
    random.shuffle(friendCombinations)
    print(pop, mean, len(friendCombinations))
    num = round(pop * mean)
    for i in range(num):
        combination = friendCombinations[i]
        db_create_friendship(combination[0], combination[1])
    return num

def db_create_attendence(person, college):
    enrollment_year = random.randint(person.date_of_birth.year + 18, MAX_DATE.year)
    graduate_year = enrollment_year + random.randint(5,10)
    normalGrade = get_truncated_normal(mean= len(person.skills)/GRADE_MEAN_FACTOR ,sd= SD_GRADE , low=2, upp=5)
    grade = round(normalGrade.rvs(), 2)

    print_to_file("./database/attendance.csv", "person_id,college_id,enrollment_year,graduate_year,grade", f"{person.id},{college.id},{enrollment_year},{graduate_year},{grade}")

def create_attendence(people, colleges):
    delete_file("./database/attendance.csv")
    normalSkills = get_truncated_normal(mean=MEAN_COLLEGE_SKILLS, sd=SD_COLLEGE_SKILLS, low=MIN_COLLEGE_SKILLS, upp=MAX_COLLEGE_SKILLS)
    for person in people:
        college = random.choice(colleges)
        person.skills= list(set(person.skills).union(random.sample(college.skills,round(normalSkills.rvs()))))
        db_create_attendence(person, college)

def same_area(colleges):
    delete_file("./database/same_area.csv")
    for combination in combinations(colleges, 2):
        if combination[0].area == combination[1].area:
            print_to_file("./database/same_area.csv", "id_first_college,id_second_college",f"{combination[0].id},{combination[1].id}" )
        

def generate_data(path = "data.cfg", path_to_names = "names-by-gender.csv", pop = 200):
    import configparser, json
    POPULATION = pop
    MEAN_FRIENDS = POPULATION * 0.05
    print(POPULATION, MEAN_FRIENDS)
    config = configparser.ConfigParser()
    config.read(path, encoding='utf-8')

    data = json.loads(config["data"]["colleges"])

    colleges = []
    all_skills = set()

    for element in data:
        college = College(element)
        colleges.append( college )
        all_skills.update(set(college.skills))
	
    hobbies_data = json.loads(config["data"]["hobbies"])

    df_names = pd.read_csv(path_to_names)

    surnames = json.loads(config["data"]["surnames"])

    people = generate_people(POPULATION, df_names, surnames, all_skills, hobbies_data)

    create_attendence(people, colleges)
    fr = create_friendships(POPULATION, MEAN_FRIENDS, people)  

    delete_file("./database/people.csv")
    for person in people:
        print_to_file("./database/people.csv", Person.csv_header(), person.csv_format())
    
    delete_file("./database/college.csv")
    for college in colleges:
        print_to_file("./database/college.csv", College.csv_header(), college.csv_format())

    same_area(colleges)
    return fr

if __name__ == "__main__":
    generate_data()
        