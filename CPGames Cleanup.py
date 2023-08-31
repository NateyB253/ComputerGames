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
date_object = None
i=0

with open('ComputerGames.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        outrow.append(row)
    
for row in outrow:
    x = outrow[i][COL_DATE]
    try:
        date_object = datetime.strptime(x, "%d-%b-%y")
    except ValueError:
        try:
            date_object = datetime.strptime(x, "%d-%b-%Y")
        except ValueError:
            if len(outrow[i][COL_DATE]) == 4:
                date_object = datetime.strptime(x, "%Y")
    if date_object != None:
        outrow[i][COL_DATE] = date_object.strftime("%m-%d-%Y")
        print(outrow[i][COL_DATE])
    i+=1
  

        
with open('ComputerGamesOutput.csv', 'w', newline = '') as file:
    
    for row in outrow:
        writer = csv.writer(file)
        writer.writerow(row)




