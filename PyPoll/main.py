# Dependencies
import os
import csv

#Read election_data.csv
csvpath = os.path.join ("..","PyPoll", "Resources", "election_data.csv")


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


#Specify the file to write to election_analysis.csv
output_path = os.path.join("..","PyPoll", "analysis", "election_analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write (column headers)
    csvwriter.writerow(['Candidate', 'Percentage of Vote', 'Total Number of Votes', 'Total Number of Votes', 'Winner of Election'])

  


