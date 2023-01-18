# Import os module
import os

# Module for reading CSV files
import csv

# Lists
profit = []
dates = []
profit_changes = []

# Starting values
total_months = 0

# Path to budget_data file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Open file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        # get the number of months
        total_months += 1
        # add dates to list
        dates.append(row[0])
        # add profit/losses to list
        profit.append((int(row[1])))

#Calculate profit/losses total
profit_total = sum(profit)

# Calculates changes in profit
for i in range(1, len(profit)):
    x = profit[i] - profit[i - 1]
    profit_changes.append(int(x))

# Calculate average profit change
changes_sum = sum(profit_changes)
average_change = round((changes_sum / (len(profit_changes))), 2)

# Find greatest increase
greatest_increase = max(profit_changes)
increase_index = profit_changes.index(greatest_increase)
increase_date = dates[increase_index + 1]

# Find greatest decrease
greatest_decrease = min(profit_changes)
decrease_index = profit_changes.index(greatest_decrease)
decrease_date = dates[decrease_index + 1]

# Print final results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${profit_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {increase_date} ${greatest_increase}")
print(f"Greatest Decrease in Profits: {decrease_date} ${greatest_decrease}")

# path to create file
output_path = os.path.join("Analysis", "budget_data.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months: {total_months}\n")
    outfile.write(f"Total: ${profit_total}\n")
    outfile.write(f"Average Change: ${average_change}\n")
    outfile.write(f"Greatest Increase in Profits: {increase_date} ${greatest_increase}\n")
    outfile.write(f"Greatest Decrease in Profits: {decrease_date} ${greatest_decrease}\n")
