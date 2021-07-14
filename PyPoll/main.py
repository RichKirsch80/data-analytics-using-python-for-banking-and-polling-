# Dependencies
import os
import csv

#Read election_data.csv
csvpath = os.path.join ("..","PyPoll", "Resources", "election_data.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    line_count = 0
    cand1_count = 0
    cand2_count = 0
    cand3_count = 0
    cand4_count = 0
    #creates empty candidate list
    cand = []
    
    #loop to read rows and count each candidate
    for row in reader:
        
        if line_count == 0:
            line_count += 1
            if row[2] == 'Khan':
                cand1_count += 1
            if row[2] == "Correy":
                cand2_count += 1
            if row[2] == "Li":
                cand3_count += 1
            if row[2] == "O'Tooley":
                cand4_count += 1     
        
        #counts each candidates votes
        else:
            line_count += 1
            if row[2] == 'Khan':
                cand1_count += 1
            if row[2] == "Correy":
                cand2_count += 1
            if row[2] == "Li":
                cand3_count += 1
            if row[2] == "O'Tooley":
                cand4_count += 1   

        #sorts data to find unique candidate names
        if row[2] not in cand:
            cand.append(row[2])
        
    #finds percentage of vote and coverts to correct format
    c1 = cand1_count / line_count
    c1_percent = "{:.0%}".format(c1)
    c2 = cand2_count / line_count
    c2_percent = "{:.0%}".format(c2)
    c3 = cand3_count / line_count
    c3_percent = "{:.0%}".format(c3)
    c4 = cand4_count / line_count
    c4_percent = "{:.0%}".format(c4)

# Creates dictionary with candidates and their vote counts
results ={"Khan" : cand1_count,
          "Correy" : cand2_count,
          "Li" : cand3_count,
          "O'Tooley" : cand4_count}

# using get function to sort the dict to gain max value for winner
winner = (max(results, key=results.get))  

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
print("Winner: ", winner)
print("----------------------")

#Specify the file to write to election_analysis.csv
output_path = os.path.join("..","PyPoll", "analysis", "election_analysis.txt")

# Open the file using "write" mode, tf variable for write function for text file with \n line break
tf = open(output_path, 'w')

# write findings into txt file and general formating 
tf.write("Election Results\n")
tf.write("----------------------\n")
tf.write("Total Votes:" + " " + str(line_count) + "\n")
tf.write("----------------------\n")
tf.write("Khan:" + " "  + str(c1_percent) + " " + "(" + str(cand1_count) + ")" + "\n")
tf.write("Correy:" + " "  + str(c2_percent) + " " + "(" + str(cand2_count) + ")" + "\n")
tf.write("Li:" + " "  + str(c3_percent) + " " + "(" + str(cand3_count) + ")" + "\n")
tf.write("O'Tooley:" + " "  + str(c4_percent) + " " + "(" + str(cand4_count) + ")" + "\n")
tf.write("----------------------\n")
tf.write("Winner: " + " " + str(winner) + "\n")
tf.write("----------------------")

    
tf.close()
  


