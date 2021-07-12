# Dependencies
import os
import csv
from typing import List, Dict

#Read budget_data.csv
csvpath = os.path.join ("..","Pybank", "Resources", "budget_data.csv")


with open(csvpath, newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    pl_total = 0.0
    line_count = 0
    inc_max = 0
    value_max = 0
    dec_max = 0
    value_min = 0
    
    for row in reader:
        pl_total += float(row[1])
        if line_count == 0:
            line_count += 1
        else:
            line_count += 1
            if float(row[1]) > value_max:
                inc_max, value_max = row[0], float(row[1])
            if float(row[1]) < value_min:
                dec_max, value_min = row[0], float(row[1])   
     


print("Financial Analysis")
print("----------------------")
print("Total Months: ", line_count)
print("Total: $", pl_total)
print('Average Change: $', )
print("Greatest Increase in Profits:", {inc_max}, {value_max})
print("Greatest Decrease in Profits:", {dec_max}, {value_min})



        
    
    
        
   