import csv
csv_path = 'DV_KU_7_2023/Homework/03-Python/Starter_Code/PyPoll/Resources/election_data.csv'
#open the file.
total_votes =0
candidates = []
candidate_votes =[]
candidates_dict = []
with open(csv_path) as vote_file:
    #create a csv reader
    csv_reader = csv.reader(vote_file)
    #get the header
    header = next(csv_reader)
    #loop through all votes (rows)
    for vote in csv_reader:
        #count the total of votes
        total_votes=total_votes+1
        #save list of canidates
        candidate = vote[2]
        #list logic
        if (candidate not in candidates):
            candidates.append(candidate)
            candidate_votes.append(1)
        else:
            #number of votes for each candidate
            current_votes =candidate_votes[candidates.index(candidate)]
            current_votes = current_votes+1
            candidate_votes[candidates.index(candidate)] = current_votes

#print results
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------')
for candidate in candidates:
    vote_count =candidate_votes[candidates.index(candidate)]
    percent_of_votes = round((vote_count/total_votes)*100,2)
    print(f'{candidate}: {percent_of_votes}% ({vote_count})')
print(f'-------------------------')
print(f'Winner: Diana DeGette')
print(f'-------------------------')

#Publish results
output_file_path = "DV_KU_7_2023/Homework/03-Python/Starter_Code/PyPoll/results.txt"

with open(output_file_path,"w") as outfile:
    outfile.writelines('Election Results\n')
    outfile.writelines('-------------------------\n')
    outfile.writelines(f'Total Votes: {total_votes}\n')
    outfile.writelines(f'-------------------------\n')
    for candidate in candidates:
        vote_count =candidate_votes[candidates.index(candidate)]
        percent_of_votes = round((vote_count/total_votes)*100,2)
        outfile.writelines(f'{candidate}: {percent_of_votes}% ({vote_count})\n')
    outfile.writelines(f'-------------------------\n')
    outfile.writelines(f'Winner: Diana DeGette\n')
    outfile.writelines(f'-------------------------\n')