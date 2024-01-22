#import libraries for reading csv file
import os
import csv

#defining csv file path found in the resources folder
budgetfilepath = os.path.join("Resources", "budget_data.csv")

#initializing month variables 
totalmonth = 0
months= []

#initializing revenue (P/L) variables
totalrevenue = 0
revenue = []
revenuechange = []
averagerevenuechange = 0
greatestincrease = 0
greatestdecrease = 0

#opening and reading csv file
with open(budgetfilepath,'r') as csvfile:
    csvreader = csv.reader(csvfile)
    #stores header row
    csvheader = next(csvfile)

    #loop through each row in csv and store the month and revenue in the respective lists
    for row in csvreader:
        months.append(row[0])
        revenue.append(int(row[1]))
        
#returns the total number of months in the dataset
totalmonth = len(months)

#returns the total revenue for the entire period 
totalrevenue = sum(revenue)

#stores the changes in revenue into a list
for i in range(1, len(revenue)):
    revenuechange.append(int(revenue[i]) - int(revenue[i-1]))

#calculates average change in revenue
averagerevenuechange = round((sum(revenuechange) / len (revenuechange)),2)

#determines greatest increase in revenue and the date it occured
greatestincrease = max(revenuechange)
greatestincreasedate =months[revenuechange.index(greatestincrease) + 1]

#determines greatest decrease in revenue and the date it occured
greatestdecrease = min(revenuechange)
greatestdecreasedate =months[revenuechange.index(greatestdecrease) + 1]

#prints the results in the display
print("Financial Analysis")
print("--------------------")
print(f"Total Months: {totalmonth}")
print(f"Total: ${totalrevenue}")
print(f"Average Change: ${averagerevenuechange}")
print(f"Greatest Increase in Profits: {greatestincreasedate} -- (${greatestincrease})")
print(f"Greatest Decrease in Profits: {greatestdecreasedate} -- (${greatestdecrease})")

#defines the output path and writes the results in the output file stored in the analysis folder
outputpath = os.path.join("analysis", "output.txt")
file = open(outputpath, "w")
file.write("Financial Analysis \n")
file.write("-------------------- \n")
file.write(f"Total Months: {totalmonth} \n")
file.write(f"Total: ${totalrevenue} \n")
file.write(f"Average Change: ${averagerevenuechange} \n")
file.write(f"Greatest Increase in Profits: {greatestincreasedate} -- (${greatestincrease}) \n")
file.write(f"Greatest Decrease in Profits: {greatestdecreasedate} -- (${greatestdecrease}) \n")