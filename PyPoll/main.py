#import libraries for reading csv file
import os
import csv

#defining csv file path found in the resources folder
pollfilepath = os.path.join("Resources", "election_data.csv")

#initializing the total vote count, creating a lst to store candidate names, and creating a dictionary for matching candidate names with their vote counts
totalvotes = 0
candidates = []
candidatevotes = {}

#opening and reading csv file
with open(pollfilepath) as csvfile:
    csvreader = csv.reader(csvfile)
    #stores header row
    csvheader = next(csvfile)

    #loop through each row in the csv
    for row in csvreader:
        #add up the total votes as you go through each row
        totalvotes += 1
        #looking at the candidate column - if the name is not in the candidates list, add them to the list. Also set the keyvalue to 1 in the candidatevotes dictionary
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidatevotes[candidate] = 1
        else:
            #if found within the candidates list, increase the keyvalue in the candidatevotes dictionary by 1
            candidatevotes[candidate] += 1    


    #define output path to store the results in the analysis folder
    outputpath = os.path.join("analysis", "output.txt") 
    file = open(outputpath, "w")
    #print the total votes in both the display and the output file
    print("Election Results")
    file.write("Election Results \n")
    print("--------------------") 
    file.write("-------------------- \n") 
    print(f"Total Votes: {totalvotes}")
    file.write(f"Total Votes: {totalvotes} \n")
    print("--------------------") 
    file.write("-------------------- \n") 
    
    #initialize the winner variable
    winnercount = 0
    winner = ""
    #for each keyword, compare the value against the previous to determine where the highest value is and return the winner
    for person in candidatevotes:
        votes = candidatevotes[person]
        if votes > winnercount:
            winnercount = votes
            winner = person
        #calculate the percentage of votes for keyvalue against the total 
        votepercentage = round((votes / totalvotes)*100,3)
        #print the results in both the display and output file
        print(f"{person}: {votepercentage}%  ({votes})")
        file.write(f"{person}: {votepercentage}%  ({votes}) \n")
    
    #print the winner in both the display and output file
    print("--------------------")
    file.write("-------------------- \n")      
    print(f"Winner: {winner} ")
    file.write(f"Winner: {winner} \n")
    print("--------------------")    
    file.write("-------------------- \n")      