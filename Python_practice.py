#3.2.10
from turtle import width


counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
    #El Paso is not the list of counties.
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
    #Arapahoe or El Paso is not in the list of counties.
if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")
    #Only Arapahoe is in the list of counties.

#Iterate Through Lists and Tuples
for county in counties:
    print(county)
for i in range(len(counties)):
    print(counties[i])

counties_tuples = ("Arapahoe","Denver","Jefferson")

for county in counties_tuples:

      print(counties)

for i in range(len(counties_tuples)):

      print(counties_tuples[i])

#Iterate Through a Dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#Get the Values of a Dictionary
for county in counties_dict:
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict.get(county))
#422829
#463353
#432438

#Get the Key-Value Pairs of a Dictionary
#for key, value in dictionary_name.items():
 #   print(key, value)

for county, voters in counties_dict.items():
    print(county, voters)
#Arapahoe 422829
#Denver 463353
#Jefferson 432438

#Get Each Dictionary in a List of Dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)
#{'county': 'Arapahoe', 'registered_voters': 422829}
#{'county': 'Denver', 'registered_voters': 463353}
#{'county': 'Jefferson', 'registered_voters': 432438}

#How would you use the range() function to iterate over the list of dictionaries and print the counties in voting_data?
for i in range(len(voting_data)):

      print(voting_data[i]['county'])
#Get the Values from a List of Dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
#Arapahoe
#422829
#Denver
#463353
#Jefferson
#432438

#How would you retrieve the number of registered voters from each dictionary?
for county_dict in voting_data:

     print(county_dict['registered_voters'])

#print county name from each dict, use county_dict['county']
for county_dict in voting_data:
    print(county_dict['county'])
    #Arapahoe
    #Denver
    #Jefferson

#3.2.11 f string in place of concatenation
#original code:
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

#using f strings:
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#print each county and registered voter from the dictionary, skill drill
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
county_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county_dict in voting_data:
    print(county_dict['county'], 'county has', (county_dict['registered_voters']), "registered voters.")

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
#print each county and registered voter from the dictionary using f strings, skill drill
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#multiline f strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in this election?"))
message_to_candidate = (
    f"You received {candidate_votes} number of votes."
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes. ")
print(message_to_candidate)

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

#Format Floating-Point Decimals
f'{value:{width}.{precision}}'
# 2 decimal places = .2f
#add a thousands separator with a comma
f'{value:{width},.{precision}}'

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}."
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes. ")
print(message_to_candidate)


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

#can't get this code to work, should yield same as above code:
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for 'county', 'registered_voters' in voting_data:
    print(f"'county' county has 'registered_voters' registered voters.")


