# Dependencies
import os
import csv

#Read budget_data.csv
csvpath = os.path.join ("..","Pybank", "Resources", "budget_data.csv")


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


#Specify the file to write to budget_analysis.csv
output_path = os.path.join ("..","Pybank", "analysis", "budget_analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write (column headers)
    csvwriter.writerow(['Total Months', 'Total Profit/Losses', 'Average Change', 'Greatest Increase', 'Greatest Decrease'])

  







  