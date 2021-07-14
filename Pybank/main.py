# Dependencies
import os
import csv

#Read budget_data.csv
csvpath = os.path.join ("..","Pybank", "Resources", "budget_data.csv")

# opens csv and defines values to be used later
with open(csvpath, newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    pl_total = 0.0
    line_count = 0
    inc_max = 0
    value_max = 0
    dec_max = 0
    value_min = 0
    first_month = 0
    last_month =0
    # For loop to count lines, add P/L column, determine greatest Increase/Decrease
    for row in reader:
        pl_total = float(row[1]) + pl_total
        if line_count == 0:
            line_count += 1
            first_month = row[1]
        else:
            line_count += 1
            last_month = row[1] 
            if float(row[1]) > value_max:
                inc_max, value_max = row[0], float(row[1])
            if float(row[1]) < value_min:
                dec_max, value_min = row[0], float(row[1])
    #caluculate average change over test period              
    avg_change = (int(last_month) - int(first_month)) / (line_count - 1)

#printing and formating of analysis
print("Financial Analysis")
print("----------------------")
print("Total Months: ", line_count)
print("Total: $", round(pl_total))
print('Average Change: $', round(avg_change,2))
print("Greatest Increase in Profits:", inc_max, "($",round(value_max),")")
print("Greatest Decrease in Profits:", dec_max, "($",round(value_min),")")

 
#Specify the file to write to budget_analysis.txt
output_path = os.path.join ("..","Pybank", "analysis", "budget_analysis.txt")

# Open the file using "write" mode, tf variable for write function for text file with \n line break
tf = open(output_path, 'w')

# write findings into txt file and general formating 
tf.write("Financial Analysis\n")
tf.write("----------------------\n")
tf.write("Total Months:")
tf.write(" " + str(line_count) + "\n")
tf.write("Total: $")
tf.write(str(round(pl_total)) + "\n")
tf.write("Average Change: $")
tf.write(str(round(avg_change,2)) + "\n")
tf.write("Greatest Increase in Profits:")
tf.write(str(inc_max) + " " + "($" + str(round(value_max)) + ")" + "\n")
tf.write("Greatest Decrease in Profits:")
tf.write(str(dec_max) + " " + "($" + str(round(value_min)) + ")" + "\n")

    
tf.close()
    

  







  