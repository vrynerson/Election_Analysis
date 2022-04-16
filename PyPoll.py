# 1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.


# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1 Initializa a total vote counter
total_votes = 0

#2 Candidate Options
candidate_options = []

#3 Declare the empty dictionary
candidate_votes = {}

#4 Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)

    #Print each row in the CSV file.
    for row in file_reader:
        #1 Add to the total vote count.
        total_votes += 1
    
        #2 Print the candidate name from each row
        candidate_name = row[2]
        #Add the candidate name to the candidate list.
        #candidate_options.append(candidate_name)

        #2 If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add it to the list of candidates
            candidate_options.append(candidate_name)

            #3 Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
                      
        #Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
   
#Print the candidate list.
print(candidate_votes)

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
    #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.

    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
        #above code is only giving lowest number of votes?
        #  To do: print out the winning candidate, vote count and percentage to
        #   terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"-------------------------\n")
print(winning_candidate_summary)

