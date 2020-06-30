import os
import csv

# Set path for file
csvpath = os.path.join('Resources', 'election_data.csv')
file_to_output = os.path.join("analysis/output.txt")
votes = []

# Create a candidates dictionary
candidatesData = {}
candidates = []
totalNumberVotes = []
percentageVotes = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    # print(csvheader)
    for row in csvreader:
        votes.append(row)
        # Get a complete list of candidates that receive votes
        if row[2] in candidatesData.keys():
            candidatesData[row[2]] = candidatesData[row[2]] + 1
        else:
            candidatesData[row[2]] = 1
    # print(candidatesData)
    totalVotes = len(votes)

# unique list of candidates
for key, value in candidatesData.items():
    candidates.append(key)
    totalNumberVotes.append(value)
    # print(f'candidate: {candidates}')
output1 = (
    f'\nElection Results\n'
    f'-------------------------\n'
    f'Total Votes: {totalVotes}\n'
    f'-------------------------\n'
)

# Percentage of votes
for i in totalNumberVotes:
    percentageVotes.append(round(i/totalVotes * 100, 1))

# iterator of tuples where the first item in each passed iterator is paired together, second item iterator, etc
new_list = list(zip(candidates, totalNumberVotes, percentageVotes))

winnerName = []
output2 = ''
for nameItem in new_list:
    # print(f'{nameItem[0]}: {nameItem[2]} ({nameItem[1]})')
    outTmp = (
        f'{nameItem[0]}: {nameItem[2]:.3f}% ({nameItem[1]})\n'
    )
    output2 = output2 + outTmp
    if max(totalNumberVotes) == nameItem[1]:
        winnerName.append(nameItem[0])
        winner = winnerName[0]

output3 = (
    f'-------------------------\n'
    f'Winner: {winner}\n'
    f'-------------------------\n'
)
outputResult = output1 + output2 + output3
# Print the output to terminal
print(outputResult)

# Export the results to text file
with open(file_to_output, "w") as txtFile:
    txtFile.write(outputResult)
