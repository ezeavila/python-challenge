import os
import csv

csvpath = os.path.join('..' , 'Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

# We want to define all the variables and lists that we'll need for our analysis
totalmonth = 0
netgains = 0
previousnet = 0
avgchange = []
max_increase = ["",0]
max_decrease = ["",99999999999999999]
netchangelist = []
monthlist = []

with open(csvpath) as pybankcsv:
    csvreader = csv.reader(pybankcsv, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    skipjan = next(csvreader)
    print (f"CSV Header : {csv_header}")

    totalmonth = totalmonth + 1
    netgains = netgains + int(skipjan[1]) #value of the month from which we are going to be substracting to get the monthly net gain
    previousnet = int(skipjan[1]) #value that will be substracting from the next month
    for row in csvreader:
        totalmonth += 1 #calculates the total of months (rows) in our data set - we are adding one because we are skipping Jan
        netgains = netgains + int(row[1])
        netchange = int(row[1]) - previousnet
        previousnet = int(row[1])
        netchangelist += [netchange]
        monthlist = monthlist + [row[0]]
        if netchange > max_increase[1]:
            max_increase[0] = row[0]
            max_increase[1] = netchange
        if netchange < max_decrease[1]:
            max_decrease[0] = row[0]
            max_decrease[1] = netchange

averagenetchange = round(sum(netchangelist) / len(netchangelist),2)

print("Financial Analysis")
print("---------------------------------------------------")
print(f"Total months: {totalmonth}")
print(f"Net gains: {netgains}")
print(f"Average Change: {averagenetchange}")
print(f"Greatest Increase in Profit: {max_increase[0]} ({max_increase[1]})")
print(f"Greatest Decrease in Profit: {max_decrease[0]} ({max_decrease[1]})")

output_file = os.path.join("output.csv")

with open(output_file, "w") as summary:
    writer = csv.writer(summary)
    writer.writerow(["Financial Analysis"])
    writer.writerow([f"Total months: {totalmonth}"])
    writer.writerow([f"Net gains: {netgains}"])
    writer.writerow([f"Average Change: {averagenetchange}"])
    writer.writerow([f"Greatest Increase in Profit: {max_increase[0]} ({max_increase[1]})"])
    writer.writerow([f"Greatest Decrease in Profit: {max_decrease[0]} ({max_decrease[1]})"])



