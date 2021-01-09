
import csv 
#import numpy as np

csvpath = r"Resources/budget_data.csv"
print(csvpath)
# master = []

totalMonths = 0
totalProfit = 0
isFirstRow = True
lastRowProfit = 0
changeDict = {}

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    #add new column headers and append to master

    # Read each row of data after the header
    for row in csvreader:

        totalMonths += 1
        totalProfit += int(row[1])

        if isFirstRow:
            lastRowProfit = int(row[1])
            isFirstRow = False
        else:
            change = int(row[1]) - lastRowProfit
            changeDict[row[0]] = change
            lastRowProfit = int(row[1])


averageChange = np.mean(list(changeDict.values()))

maxChangeMonth = max(changeDict, key=changeDict.get)
maxChangeValue = changeDict[maxChangeMonth]

minChangeMonth = min(changeDict, key=changeDict.get)
minChangeValue = changeDict[minChangeMonth]

summaryString = f"""Finanical Analysis
-------------------------
Total Months: {totalMonths}
Total: ${totalProfit}
Average Change: ${round(averageChange, 2)}
Greatest Increase in Profits: {maxChangeMonth} (${maxChangeValue})
Greatest Decrease in Profits: {minChangeMonth} (${minChangeValue})
"""
with open("bank_results.txt", "w") as file1:
    file1.write(summaryString)
