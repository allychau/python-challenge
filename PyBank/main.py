import os
import csv

# Set path for file
csvpath = os.path.join('Resources', 'budget_data.csv')
# Specify the file to write to
file_to_output = os.path.join("analysis/output.txt")

months = []
pl = []
netIncome = []


# Open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    # print(f'CSVHeader: {csvheader}')
    for row in csvreader:

        months.append(row[0])
        pl.append(int(row[1]))
    totalMonths = len(months)
    totalNet = sum(pl)

    for i in range(1, len(pl)):
        netIncome.append(int(pl[i]) - int(pl[i-1]))

    netMonthlyAvg = sum(netIncome)/len(netIncome)
    greatestIncrease = max(netIncome)
    greatestDecrease = min(netIncome)

# Generate output summary
output = (
    f'Financial Analysis\n'
    f'----------------------------\n'
    f'Total Months: {totalMonths} \n'
    f'Total: $ {totalNet}\n'
    f'Average Change: $ {netMonthlyAvg: .2f}\n'
    f'Greatest Increase in Profits: {months[netIncome.index(greatestIncrease)+1]} ($ { greatestIncrease})\n'
    f'Greatest Decrease in Profits: {months[netIncome.index(greatestDecrease)+1]} ($ { greatestDecrease})'
)

# Print the output to terminal
print(output)
# Export the results to text file
with open(file_to_output, "w") as txtFile:
    txtFile.write(output)
