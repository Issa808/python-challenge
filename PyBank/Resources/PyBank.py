import os 
import csv

#create file path to csv
bank_csv = os.path.join('python-challenge', 'PyBank', 'Resources', 'budget_data.csv')

#define lists to use later 
months = []
profits =[]
changes = []

#open csv file
with open(bank_csv) as csvfile:
    #open csv as a reader
    csvreader = csv.reader(csvfile)

    #define header to skip it
    csv_header = next(csvreader)

    #loop through the csv file
    for row in csvreader:
        #add the months in the first row to the months list
        months.append(row[0])
        #convert profits from string to integer and add to profits list
        profits.append(int(row[1]))
    
    #loop through the length of of profits list
    for i in range(len(profits)-1):
        #add the changes in profits to the changes list
        changes.append(profits[i+1]-profits[i])

#find the maximum and minimum changes in the profits
increase = changes.index(max(changes)) + 1
decrease = changes.index(min(changes)) + 1

#find average change in profits
ave_change = round(sum(changes)/len(changes),2)

#print the results
print(f"Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(profits)}")
print(f"Average Change: ${ave_change}")
print(f"Greatest Increase in Profits: {months[increase]} (${str(max(changes))})")
print(f"Greatest Decrease in Profits: {months[decrease]} (${str(min(changes))})")

#create path for output file 
output_file = os.path.join('python-challenge', 'PyBank', 'Resources', 'results.txt')

#open output file to write to
with open(output_file,'w') as datafile:
    
    #write the results in the output file
    datafile.write(f"Financial Analysis\n")
    datafile.write("----------------------------\n")
    datafile.write(f"Total Months: {len(months)}\n")
    datafile.write(f"Total: ${sum(profits)}\n")
    datafile.write(f"Average Change: ${ave_change}\n")
    datafile.write(f"Greatest Increase in Profits: {months[increase]} (${str(max(changes))})\n")
    datafile.write(f"Greatest Decrease in Profits: {months[decrease]} (${str(min(changes))})\n")

