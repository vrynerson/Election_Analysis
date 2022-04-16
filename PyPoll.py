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

    #Save the results to our text file.
    with open(file_to_save, "w") as txt_file:
        #Print the final vote count to the terminal
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the txt file
        txt_file.write(election_results)
    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
        for candidate_name in candidate_votes:
            # Retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]
            # Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            #print each candidate's voter count and percentage to the terminal
            print(candidate_results)
            #Save candidate results to our text file
            txt_file.write(candidate_results)
            # Determine winning vote count, winning percentage, and winning candidate.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_candidate = candidate_name
                winning_percentage = vote_percentage
                #above code is only giving lowest number of votes?
                #  To do: print out the winning candidate, vote count and percentage to
                #   terminal.
              
        #Print the winning candidates' results to the terminal.
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        # Save the winning candidate's results to the text file.
        txt_file.write(winning_candidate_summary)
       