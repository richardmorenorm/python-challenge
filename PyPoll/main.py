import os
import csv

# lists
candidates = []

# Starting values
total_voters = 0
candidate_0 = 0
candidate_1 = 0
candidate_2 = 0

# open path to csv
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        # count voters
        total_voters += 1
        # add candidates to list
        if row[2] not in candidates:
            candidates.append(row[2])
        # count each candidate's votes
        if row[2] == candidates[0]:
            candidate_0 += 1
        elif row[2] == candidates[1]:
            candidate_1 += 1
        elif row[2] == candidates[2]:
            candidate_2 += 1
        

# calculate percentage of votes
candidate0_percent = round((candidate_0 / total_voters)*100, 3)
candidate1_percent = round((candidate_1 / total_voters)*100, 3)
candidate2_percent = round((candidate_2 / total_voters)*100, 3)

# print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_voters}")
print("-------------------------")
print(f"{candidates[0]}: {candidate0_percent}% ({candidate_0})")
print(f"{candidates[1]}: {candidate1_percent}% ({candidate_1})")
print(f"{candidates[2]}: {candidate2_percent}% ({candidate_2})")
print("-------------------------")
print(f"Winner: {candidates[1]}")
print("-------------------------")


# Specify the file to write to
output_path = os.path.join("Analysis", "election_data.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as outfile:

    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes: {total_voters}\n")
    outfile.write("-------------------------\n")
    outfile.write(f"{candidates[0]}: {candidate0_percent}% ({candidate_0})\n")
    outfile.write(f"{candidates[1]}: {candidate1_percent}% ({candidate_1})\n")
    outfile.write(f"{candidates[2]}: {candidate2_percent}% ({candidate_2})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner: {candidates[1]}\n")
    outfile.write("-------------------------\n")