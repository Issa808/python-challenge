import os 
import csv

#create file path to csv
poll_csv = os.path.join('python-challenge', 'PyPoll', 'Resources', 'election_data.csv')

#define lists and integers to use later 
votes = []
Charles = 0
Diana = 0
Raymon = 0

#open csv file
with open(poll_csv) as csvfile:
    #open csv as a reader
    csvreader = csv.reader(csvfile)
    #define header to skip it
    csv_header = next(csvreader)

    #loop through the csv file
    for row in csvreader:
        #add the votes in the first row to the votes list
        votes.append(row[0])
        
        #count the votes for each candidate
        if row[2] == "Charles Casper Stockham":
            Charles = Charles + 1
        elif row[2] == "Diana DeGette":
            Diana = Diana + 1
        elif row[2] == "Raymon Anthony Doane":
            Raymon = Raymon + 1

#calculate the percent of votes each candidate got 
Charles_votes = round((Charles/len(votes)) * 100,3)
Diana_votes = round((Diana/len(votes)) * 100,3)
Raymon_votes = round((Raymon/len(votes)) * 100,3)

#create lists for candidate and their total votes
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
final_votes = [Charles, Diana, Raymon]

#zip those two lists together
zipping = zip(candidates, final_votes)
#create a dictionary for the zip 
candidate_dict = dict(zipping)
#find the candidate with the most votes
winner = max(candidate_dict, key=candidate_dict.get)

#print the results
print(f"Election Results")
print("-------------------------")
print(f"Total Votes: {len(votes)}")
print("-------------------------")
print(f"Charles Casper Stockham: {Charles_votes}% ({Charles})")
print(f"Diana DeGette: {Diana_votes}% ({Diana})")
print(f"Raymon Anthony Doane: {Raymon_votes}% ({Raymon})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


#create path for output file 
output_file = os.path.join('python-challenge', 'PyPoll', 'Resources', 'results.txt')

#open output file to write to
with open(output_file,'w') as datafile:
    
    #write the results in the output file
    datafile.write(f"Election Results\n")
    datafile.write("-------------------------\n")
    datafile.write(f"Total Votes: {len(votes)}\n")
    datafile.write("-------------------------\n")
    datafile.write(f"Charles Casper Stockham: {Charles_votes}% ({Charles})\n")
    datafile.write(f"Diana DeGette: {Diana_votes}% ({Diana})\n")
    datafile.write(f"Raymon Anthony Doane: {Raymon_votes}% ({Raymon})\n")
    datafile.write("-------------------------\n")
    datafile.write(f"Winner: {winner}\n")
    datafile.write("-------------------------\n")

