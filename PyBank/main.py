import os
import csv

# Set path for file
csvpath = os.path.join('Resources', 'budget_data.csv')


# def printAnalysis()
months = []
pl = []
revenueChange = []
totalRevenueChange = 0

# Open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    # print(f'CSVHeader: {csvheader}')
    for row in csvreader:
        # print(row[0] + ' ' + row[1])
        months.append(row[0])
        pl.append(int(row[1]))
    totalMonths = len(months)
    totalAmtProfitLosses = sum(pl)

    for i in range(1, len(pl)):
        revenueChange.append(int(pl[i]) - int(pl[i-1]))
        # print(str(months[i]) + ',' + str(pl[i]))
        # print(revenueChange)
        # print(int(pl[i]))
        # print(int(pl[i-1]))

    # print(months[25])
    # print(months[25])

    # print(f'Months Size: {len(months)}')
    # print(f'PL Size: {len(pl)}')
    # print(f'Revenue Change Size: {len(revenueChange)}')
    avgRevenueChange = sum(revenueChange)/len(revenueChange)
    greatestIncrease = max(revenueChange)
    greatestDecrease = min(revenueChange)
    print(greatestIncrease)
    print(revenueChange.index(max(revenueChange)))
    # print(pl.index[greatestIncrease])
    # print(myList.index("Matt"))
    # print(str(months[revenueChange.index(max(revenueChange))+1]))


print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {totalMonths}')
print(f'Total: $ {totalAmtProfitLosses}')
print(f'Average Change: $ {avgRevenueChange}')
print(
    f'Greatest Increase in Profits: {months[revenueChange.index(max(revenueChange))+1]} ({greatestIncrease})')
print(
    f'Greatest Decrease in Profits: {months[revenueChange.index(min(revenueChange))+1]} ({greatestDecrease})')
