# Data Cleanup for CSV File
import csv
COL_NAME = 0
COL_DEVELOPER = 1

with open('ComputerGames.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[COL_NAME], row[COL_DEVELOPER])

