import os
import csv
budget_csv = os.path.join(".", "Resources", "budget_data.csv")
 
# Open and read csv
total = 0
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # number of months and dollars
    month = []
    
    money_sum = 0
    change = 0
    csv_header = next(csvfile)
    for row in csvreader:
        month.append(row[0])
        money_sum = money_sum + int(row[1])
        
    month_list = month
    
    print("Total Months: " + str(len(month_list)))  
    print("Total Dollars: " + str(money_sum))  
    for row in csvreader:
        def percentChange():
          change =  return((float((row+1)-row)/abs(row)))*100.00
    print(change)

        

        

        
    

    

    
        