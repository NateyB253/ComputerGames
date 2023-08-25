# Data Cleanup for CSV File
from datetime import datetime
import csv
import re
import pandas as pd

dates = []
COL_NAME = 0
COL_DEVELOPER = 1
COL_PRODUCER = 2
COL_GENRE = 3 
COL_OP_SYSTEM = 4
COL_DATE = 5
date_regex = r'\d{1,2}-[a-zA-Z]{3}-(?:\d{2}|\d{4})'
date_object = None

with open('ComputerGames.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        dates.append(row[COL_DATE])


for date in dates:
    try:
        date_object = datetime.strptime(date, "%d-%b-%y")
    except ValueError:
        try:
            date_object = datetime.strptime(date, "%d-%b-%Y")
        except ValueError:
             if len(date) == 4:
                date_object = datetime.strptime(date, "%Y")
    if date_object != None:
        print(date_object.strftime("%m-%d-%Y"))

'''
with open('ComputerGamesOutput.csv', 'w') as file:
    writer = csv.writer(file)
    for row in writer:
'''   



