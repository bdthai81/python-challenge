# main.py
# A program to analyzing the financial records of the company

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

# Read CVS File data set & return list with store data
def readDataSet(csvpath):
    dataSet = []
    # Reading using CSV module
    with open(csvpath, newline='') as csvfile:

        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')

        # Read the header row first ('Date', 'Profit/Losses')
        csv_header = next(csvreader)

        # Read each row of data after the header & store into dataSet
        dataSet = [[row[0], int(row[1])] for row in csvreader]
    return dataSet

# Calculate Financial Analysis
def getAnalysis(ds):

    # declare and initialize variables with calculated results
    totalMonths = len(ds)
    totalNet = sum([row[1] for row in ds])
    changeList = [[val[0], val[1] - ds[idx][1]] for idx, val in enumerate(ds[1:])]
    avgChange = sum([row[1] for row in changeList])/len(changeList)
    maxProfit = max([row[1] for row in changeList])
    maxMonth = [row[0] for row in changeList if row[1] == maxProfit][0]
    minProfit = min([row[1] for row in changeList])
    minMonth = [row[0] for row in changeList if row[1] == minProfit][0]
    
    return (f"""Financial Analysis
----------------------------
Total Months: {totalMonths}
Total: ${totalNet}
Average  Change: ${round(avgChange, 2)}
Greatest Increase in Profits: {maxMonth} (${maxProfit})
Greatest Decrease in Profits: {minMonth} (${minProfit})""")

# Print analysis to terminal & write to results.txt
def writeAnalysis(financialPrint):
    # save the output file path
    output_file = os.path.join("results.txt")

    # open the output file, write Financial Analysis
    with open(output_file, "w", newline="") as datafile:
        datafile.write(financialPrint)

# main function to execute program
def main ():
    dataSet = []
    # path
    csvpath = os.path.join('Resources', 'PyBank_Resources_budget_data.csv')
    # load dataset from csv    
    dataSet = readDataSet(csvpath)
    # calculate financial analysis
    financialAnalysis = getAnalysis(dataSet)
    # print/write analysis
    print(financialAnalysis)
    writeAnalysis(financialAnalysis)
    
# execute main
main ()