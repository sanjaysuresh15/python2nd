import os
import csv
budget_csv = os.path.join(".", "Resources", "budget_data.csv")
 
# Open and read csv
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # number of months
    
    for row in csvreader:
        print(row[0])



        



