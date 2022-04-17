# Election_Analysis
## Overview of Election Audit
The Colorado Board of Elections wants to audit a local congressional election's data. The client has been given the following list to complete the audit so the election can be certified. 

1. The total number of votes cast
2. The percentage of votes from each county
3. The total number of voters in each county
4. The county with the largest number of votes    
5. A complete list of candidates who received votes  
6. The percentage of votes each candidate won  
7. The total number of votes each candidate won  
8. The winner of the election based on popular vote.

The following voting and counting methods were used in this election:
* Mail-in ballot, counted by hand
* Punch cards, counted by machine
* Direct recording electronic, counted through the computer

Votes are gathered into a csv file and sorted by column A: Ballot ID, column B: County, and column C: Candidate name.

## Election-Audit Results
* How many votes were cast in this congressional election?
  * There were **369,711** total votes cast in this election. 
### By County
* Number of voters and percentage of total votes for each county in the precinct.
  * Jefferson county had 38,855 voters, **10.5%** of the total votes.
  * Denver county had 306,055 voters, **82.8%** of the total votes.
  * Arapahoe county had 24,801 voters, **6.7%** of the total votes.
* Which county had the largest number of votes?
  * **Denver county** had the largest number of votes.
### By Candidate
* Number of votes and the percentage of the total votes each candidate received.
  * Charles Casper Stockham received **23.0%** of the vote and 85,213 number of votes.  
  * Diana DeGette received **73.8%** of the vote and 272,892 number of votes.  
  * Raymon Anthony Doane received **3.1%** of the vote and 11,606 number of votes.  
* Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
  * **Candidate Diana DeGette**, who received **73.8%** of the vote and 272,892 number of votes, won the election based on popular vote.

Results: [election_analysis.txt](https://github.com/vrynerson/Election_Analysis/blob/main/analysis/election_analysis.txt)

## Election-Audit Summary
The script written for the congressional election can be transferred to use in any election. Changing files, variable names, and strings to reflect the new data in quesiton to reuse this code would make for efficient use of time. Examples are shown below. 

**Example 1: Change the data file.**
```
# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
```
The code `import csv` can be altered to accomodate a different data storage file, such as json.

The code `file_to_load = os.path.join("Resources", "election_results.csv")` can be changed to load any file that holds the desired election's data by changing to the relative file name.
The code `file_to_save = os.path.join("analysis", "election_analysis.txt")` can be changed to the file the data wants to be written to.

**Example 2: Select where the data is pulled from.**
 ```
 for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # Extract the county name from each row.
        counties = row[1]
```
This code is used to select what data is being used for each variable. The code `candidate_name = row[2]` is taking data from Row 3, which has candidate data. The code `counties = row[1]` is using data from Row 2, which has data on which county a voter is in. To use it for a different election, the variables `candidate_name` or `counties` and the strings `row[1]` and `row[2]` would need to be changed to reflect the data they are representing.

## Resources
-Data Source: [election_results.csv](https://github.com/vrynerson/Election_Analysis/blob/main/Resources/election_results.csv)  
-Software: Python 3.7, Visual Studio Code 1.66.2   
