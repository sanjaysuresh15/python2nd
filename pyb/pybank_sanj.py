import os
import csv
budget_csv = os.path.join(".", "resources", "budget_data.csv")
 
# Open and read csv
total = 0
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #define variables
    month = []
    month_list = month
    money_sum = 0
    change = 0
    
    def percentChange():
        float((row+1)-row)/abs(row)*100.00
    
    csv_header = next(csvfile)
    for row in csvreader:
        month.append(row[0])
        money_sum = money_sum + int(row[1])
        
    # number of months and dollars

    print("Total Months: " + str(len(month_list)))  
    print("Total Dollars: " + str(money_sum))  
    
    
    for row in csvreader:
      change + percentChange()
    print("Percent Change: " + str(change))        

        

        

        
    

    

    
        