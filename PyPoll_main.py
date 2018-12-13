# PyPoll Challenge
# Module for OS
import os

# Module for subprocess/terminal output
# import subprocess
# with open("output.txt", "w+") as output:
#    subprocess.call(["python", "./main.py"], stdout=output)


# Module for reading CSV file
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

# The total number of votes cast
    voter_id = []
    county_name = []
    candidate_name = []
    total_votes = 0 
    
    for row in csvreader:
        candidate_name.append(row[2])
        total_votes +=  1

# A complete list of candidates who received votes
# The total number of votes each candidate won

    khan_total = 0
    correy_total = 0
    li_total = 0
    otooley_total = 0
    for x in candidate_name:
        if x == "Khan":
            khan_total += 1
        
        elif x == "Correy":
            correy_total += 1 

        elif x == "Li":
            li_total += 1
        elif x == "O'Tooley": 
            otooley_total += 1

# The percentage of votes each candidate won

    khan_vote_percentage = round((khan_total/(total_votes - 1)), 3) 
    correy_vote_percentage = round((correy_total/(total_votes -1)), 3)
    li_vote_percentage = round((li_total/(total_votes -1)), 3)
    otooley_vote_percentage = round((otooley_total/(total_votes -1)), 3)

    all_candidate_names = ["Khan", "Correy", "Li", "O'Tooley"]
    candidate_vote_count_list = [(khan_total), (correy_total), (li_total), (otooley_total)]

# The winner of the election based on popular vote.
    highest_vote = max(candidate_vote_count_list)
    highest_vote_index = candidate_vote_count_list.index(highest_vote)
 
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes - 1))
print("-------------------------")
print(all_candidate_names[0] + ": {:.3%}".format(khan_vote_percentage) + " (" + str(khan_total) + ")")
print(all_candidate_names[1] + ": {:.3%}".format(correy_vote_percentage) + " (" + str(correy_total) + ")")
print(all_candidate_names[2] + ": {:.3%}".format(li_vote_percentage) + " (" + str(li_total) + ")")
print(all_candidate_names[3] + ": {:.3%}".format(otooley_vote_percentage) + " (" + str(otooley_total) + ")") 
print("-------------------------")
print("Winner: " + all_candidate_names[highest_vote_index] )
print("-------------------------")