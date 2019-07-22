import os
import csv
csv_file = os.path.join(".", "resources", "budget_data.csv")
with open(csv_file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    for row in csvreader:
        print(row)


