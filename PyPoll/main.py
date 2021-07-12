# Dependencies
import os
import csv

#Read election_data.csv
csvpath = os.path.join ("..","PyPoll", "Resources", "election_data.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(csvpath, newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    line_count = 0
    cand1_count = 0
    cand2_count = 0
    cand3_count = 0
    cand4_count = 0
    cand = []
    #loop to read rows and count each candidate
    for row in reader:
        if line_count == 0:
            line_count += 1
        #sorts data to find unique cancidate names
        if row[2] not in cand:
            cand.append(row[2])
        #counts each candidates votes
        else:
            line_count += 1
            if row[2] == 'Khan':
                cand1_count = cand1_count + 1
            if row[2] == "Correy":
                cand2_count = cand2_count + 1
            if row[2] == "Li":
                cand3_count = cand3_count + 1
            if row[2] == "O'Tooley":
                cand4_count = cand4_count + 1
    #finds percentage and coverts to correct format
    c1 = cand1_count / line_count
    c1_percent = "{:.0%}".format(c1)
    c2 = cand2_count / line_count
    c2_percent = "{:.0%}".format(c2)
    c3 = cand3_count / line_count
    c3_percent = "{:.0%}".format(c3)
    c4 = cand4_count / line_count
    c4_percent = "{:.0%}".format(c4)

#Prints findings
print("Election Results")
print("----------------------")
print("Total Votes: ", line_count)
print("----------------------")
print("Khan:", c1_percent, cand1_count)
print("Correy:",c2_percent, cand2_count)
print("Li",c3_percent, cand3_count)
print("O'Tooley;",c4_percent, cand4_count)
print("----------------------")
print("Winner: ")
print("----------------------")

#Specify the file to write to election_analysis.csv
output_path = os.path.join("..","PyPoll", "analysis", "election_analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write (column headers)
    csvwriter.writerow(['Candidate', 'Percentage of Vote', 'Total Number of Votes', 'Total Number of Votes', 'Winner of Election'])

  


