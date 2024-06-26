import os

import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Ballot IDs in row[0] will be appended here
totalBallots = []
candidate_votes = {}

sumVotes = 0

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    # csvheader = next(csvreader)
    # print(f"CSV Header: {csvheader}")


    for row in csvreader:
        totalBallots.append(row[0])
        # I used Xpert Learning Assistant to fine-tune any errors in the if/else lines, including calculating the sumVotes
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
        sumVotes += 1

output_folder = 'Resources'
with open (os.path.join(output_folder, 'Election Results.txt'), 'w') as f:

    print("Election Results",file=f)

    print("-------------------------",file=f)

    print("Total Votes: ",len(totalBallots),file=f)

    print("-------------------------",file=f)
# I used Xpert Learning Assitant to help me correct my errors as well as build the for statement below:
    for candidate, count in candidate_votes.items(): 
        percentage = (count / sumVotes) * 100
        print(f'{candidate}: {percentage:.2f}% ({count} votes)',file=f)
    print("-------------------------",file=f)
    winner = max(candidate_votes, key=candidate_votes.get)
    print(f'Winner: {winner}',file=f)
    print("-------------------------",file=f)
