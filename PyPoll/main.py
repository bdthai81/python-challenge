# Voter ID	County	Candidate
# main.py
# A program to analyzing the Election results

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
import numpy as np

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
        dataSet = [row for row in csvreader]
    return dataSet

# Calculate Financial Analysis
def getAnalysis(ds):

    # declare and initialize variables with calculated results
    totalVotes = len(ds)
    # declare and initialize set of distinct candidates
    candidateSet = set([row[2] for row in ds])
    
    # declare and initialize list of candidate's dictionary info
    candidates = []
    # declare winner
    winner = ""
    winnerVotes = 0
    for candidate in candidateSet:
        votes = len([row for row in ds if row[2] == candidate])
        percentage = votes / totalVotes * 100
        candidates.append({"name": candidate, "percentage": percentage, "votes": votes})
        # update leading winner
        if votes > winnerVotes:
            winner = candidate
            winnerVotes = votes

    # sort list by most votes
    candidates = sorted(candidates, key=lambda k: k['votes'], reverse=True)  

    # Print Header
    results = f"""Election Results
-------------------------
Total Votes: {totalVotes}
-------------------------\n"""
    # Print Candidates
    for candidate in candidates:
        results += candidate["name"] + ": " + format(candidate["percentage"],'.3f') + "% (" + str(candidate["votes"]) + ")\n"
        #results += f"{candidate["name"]}: " #{candidate["percentage"]}% ({candidate["votes"]})\n"

    # Print Winner
    results += f"""-------------------------
Winner: {winner}
-------------------------"""
    # return results
    return results
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
    csvpath = os.path.join('Resources', 'PyPoll_Resources_election_data.csv')
    # load dataset from csv    
    dataSet = readDataSet(csvpath)
    # calculate financial analysis
    pollAnalysis = getAnalysis(dataSet)
    # print/write analysis
    print(pollAnalysis)
    writeAnalysis(pollAnalysis)
    
# execute main
main ()