import os
import csv

csvpath = os.path.join('..' , 'Resources', '02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')

totalvotes = 0


with open(csvpath) as pypollcsv:
    csvreader = csv.reader(pypollcsv, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    #print (f"CSV Header : {csv_header}")

    #totalvotes = totalvotes + 1

    candidates = {}
    for row in csvreader:
        totalvotes += 1
        if row[2] not in candidates:
            candidates[row[2]] = 0
        candidates[row[2]] = candidates[row[2]] + 1

        final_list = [{'Candidate' : row, 'Percentage of Votes (%)' : round(float(candidates[row]/totalvotes * 100),2), 'Total Votes' : candidates[row], } for row in candidates]


print("Election Results")
print("___________________________________")
print([f"Total Votes: {int(totalvotes)}"])
print(final_list)
print("-----------------------------------")
print(final_list[0])
print(final_list[1])
print(final_list[2])
print(final_list[3])
print("-----------------------------------")
print(f"Winner: {final_list[0]}")

output_file = os.path.join("outputpypoll.csv")

with open(output_file, "w") as summaryelection:
    writer = csv.writer(summaryelection)
    writer.writerow(["Election Results"])
    writer.writerow([f"Total Votes: {totalvotes}"])
    writer.writerow([f"Results by Candidate: {final_list}"])
    writer.writerow([f" {final_list[0]}"])
    writer.writerow([f" {final_list[1]}"])
    writer.writerow([f" {final_list[2]}"])
    writer.writerow([f" {final_list[3]}"])
    writer.writerow([f"Winner: {final_list[0]}"])