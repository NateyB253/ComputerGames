# Data Cleanup for CSV File
from datetime import datetime
import csv

outrows = []
COL_NAME = 0
COL_DEVELOPER = 1
COL_PRODUCER = 2
COL_GENRE = 3 
COL_OP_SYSTEM = 4
COL_DATE = 5
i = 0

with open('ComputerGames.csv') as file:
    reader = csv.reader(file)
    
    for row in reader:
        outrows.append(row)
        if len(outrows[i][COL_DATE]) == 4:
            x = outrows[i][COL_DATE]
            date_object = datetime.strptime(x, "%Y")
            outrows[i][COL_DATE] = date_object.strftime("%m-%d-%Y")
        i+=1

with open('ComputerGamesOutput.csv', 'w') as file:
    for row in outrows:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerow(row)

""" for row in reader:
   print(row[COL_NAME], row[COL_DEVELOPER], row[COL_PRODUCER], row[COL_GENRE], row[COL_OP_SYSTEM], row[COL_DATE])
"""