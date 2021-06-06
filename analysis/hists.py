import pandas as pd
import matplotlib

people = pd.read_csv("../database/people.csv", encoding='utf-8')

people.plot.hist("date_of_birth")