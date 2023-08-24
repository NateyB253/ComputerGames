# Data Cleanup for CSV File
from datetime import datetime
import csv

dates = []
COL_NAME = 0
COL_DEVELOPER = 1
COL_PRODUCER = 2
COL_GENRE = 3 
COL_OP_SYSTEM = 4
COL_DATE = 5

with open('ComputerGames.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        dates.append(row[COL_DATE])

for date in dates:
    if len(date) == 4:
        x = date
        date_object = datetime.strptime(x, "%Y")
        print(date_object.strftime("%m-%d-%Y"))


"""with open('ComputerGamesOutput.csv', 'w') as file:
    writer = csv.writer(file)
    for row in writer:
    
"""



