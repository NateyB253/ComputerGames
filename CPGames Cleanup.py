# Data Cleanup for CSV File
from datetime import datetime
import csv

outrow = []
COL_NAME = 0
COL_DEVELOPER = 1
COL_PRODUCER = 2
COL_GENRE = 3 
COL_OP_SYSTEM = 4
COL_DATE = 5


with open('ComputerGames.csv') as file:
    reader = csv.reader(file)
    
    for row in reader:
        outrow.extend(row)
        if len(outrow[COL_DATE]) == 4:
            x = outrow[COL_DATE]
            date_object = datetime.strptime(x, "%Y")
            outrow[COL_DATE] = date_object.strftime("%m-%d-%Y")

with open('ComputerGamesOutput.csv', 'wb') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerow(outrow)

""" for row in reader:
   print(row[COL_NAME], row[COL_DEVELOPER], row[COL_PRODUCER], row[COL_GENRE], row[COL_OP_SYSTEM], row[COL_DATE])
"""