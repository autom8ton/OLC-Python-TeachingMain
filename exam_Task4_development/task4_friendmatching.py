
# A friend matching company wishes to develop an application that helps its users to find friends. 
# It does this by searching through its user database and pairing users with the same hobbies or personalities to one another.

# Open the file FRIENDS.ipynb

# It shows the following program that contains the names and profiles of the users. The program allows the user to:

# input a new name
# input whether they want to add a name and profile to the dictionary.
# For all the sub-tasks in Task 1, you can assume that all user inputs are valid.

userbase = {
"Name": ['Gender', 'Personality', 'Hobby'],
"Alice": ["Female", "Extroverted", "Travel"],
"Bob": ["Male", "Introverted", "Coding"],
"Carol": ["Female", "Extroverted", "Photography"], 
"David": ["Male", "Introverted", "Coding"],
"Emily": ["Female", "Extroverted", "Travel"],
"Frank": ["Male", "Kind", "Volunteering"],
"Grace": ["Female", "Kind", "Reading"],
"Henry": ["Male", "Kind", "Music"],
"Ivy": ["Female", "Introverted", "Reading"],
"John": ["Male", "Extroverted", "Travel"]
}

name = input("Please enter the name of a user: ")
add = input ("Would you like to add a new entry? (Y/N): ")

# Save the file as:
# TASK1_<your name>_<class>_<index number>.ipynb

# For each of the sub-tasks, begin in a new code cell and add a comment using the 
# hash symbol '#' at the beginning of your code to indicate the sub-task 
# that the program code belongs to.
# For example:

#Task 1.1

# Edit the program so that it:
#  searches the dictionary for the name input and outputs the profile of that name
# asks the user whether the name is to be added as a new entry 
# if the name is not found in the dictionary.

# [2]



####################################################
# Task 1.2

# Copy and paste your program from sub-task 1.1.
# Edit the program so that if the user inputs "Y" for add, the program allows the
#  user to input the name and profile of the person to the dictionary in the format 
# "Name": ['Gender', 'Personality', 'Hobby']
# Appropriate messages must be used to prompt the user to input each of the profile field.

# [2]
####################################################

# Task 1.3

# Copy and paste your program from sub-task 1.2.

# Edit the program so that it:
#->  initialises a new dictionary variable called personalities which contains 
# the personality types: "Extroverted", "Introverted", "Kind" and "Curious" as keys

#->   searches through userbase and adds the names of those with the same 
# personality together, in personalities.

#->  allows the user to input a personality type

# prints out a message "['N1', 'N2', 'N3'] should be friends as they are all P4.", 
# where N1, N2, N3 are to be replaced with the names of the persons and P4 to be 
# replaced with the personality type input by the user.

# [6]

#######
# Code Task 1.3






# ###############################################
# # ANSWER BELOW


# # A friend matching company wishes to develop an application that helps its users to find friends. 
# # It does this by searching through its user database and pairing users with the same hobbies or personalities to one another.

# # Open the file FRIENDS.ipynb

# # It shows the following program that contains the names and profiles of the users. The program allows the user to:

# # input a new name
# # input whether they want to add a name and profile to the dictionary.
# # For all the sub-tasks in Task 1, you can assume that all user inputs are valid.

# userbase = {
# "Name": ['Gender', 'Personality', 'Hobby'],
# "Alice": ["Female", "Extroverted", "Travel"],
# "Bob": ["Male", "Introverted", "Coding"],
# "Carol": ["Female", "Extroverted", "Photography"], 
# "David": ["Male", "Introverted", "Coding"],
# "Emily": ["Female", "Extroverted", "Travel"],
# "Frank": ["Male", "Kind", "Volunteering"],
# "Grace": ["Female", "Kind", "Reading"],
# "Henry": ["Male", "Kind", "Music"],
# "Ivy": ["Female", "Introverted", "Reading"],
# "John": ["Male", "Extroverted", "Travel"]
# }

# name = input("Please enter the name of a user: ")
# add = input ("Would you like to add a new entry? (Y/N): ")

# # Save the file as:
# # TASK1_<your name>_<class>_<index number>.ipynb

# # For each of the sub-tasks, begin in a new code cell and add a comment using the 
# # hash symbol '#' at the beginning of your code to indicate the sub-task 
# # that the program code belongs to.
# # For example:

# #Task 1.1

# # Edit the program so that it:
# #  searches the dictionary for the name input and outputs the profile of that name
# # asks the user whether the name is to be added as a new entry 
# # if the name is not found in the dictionary.

# # Save your program.

# userbase = {
# "Alice": ["Female", "Extroverted", "Travel"],
# "Bob": ["Male", "Introverted", "Coding"],
# "Carol": ["Female", "Extroverted", "Photography"], 
# "David": ["Male", "Introverted", "Coding"],
# "Emily": ["Female", "Extroverted", "Travel"],
# "Frank": ["Male", "Kind", "Volunteering"],
# "Grace": ["Female", "Kind", "Reading"],
# "Henry": ["Male", "Kind", "Music"],
# "Ivy": ["Female", "Introverted", "Reading"],
# "John": ["Male", "Extroverted", "Travel"]
# }

# name = input("Please enter the name of a user: ")

# if name in userbase:
#     print(f"The profile for {name} is {userbase[name]}")
# else:
#     add = input ("Would you like to add a new entry? (Y/N): ")




# [2]

# # Task 1.2

# # Copy and paste your program from sub-task 1.1.
# # Edit the program so that if the user inputs "Y" for add, the program allows the
# #  user to input the name and profile of the person to the dictionary in the format 
# # "Name": ['Gender', 'Personality', 'Hobby']
# # Appropriate messages must be used to prompt the user to input each of the profile field.

# # Save your program.

# userbase = {
# "Alice": ["Female", "Extroverted", "Travel"],
# "Bob": ["Male", "Introverted", "Coding"],
# "Carol": ["Female", "Extroverted", "Photography"], 
# "David": ["Male", "Introverted", "Coding"],
# "Emily": ["Female", "Extroverted", "Travel"],
# "Frank": ["Male", "Kind", "Volunteering"],
# "Grace": ["Female", "Kind", "Reading"],
# "Henry": ["Male", "Kind", "Music"],
# "Ivy": ["Female", "Introverted", "Reading"],
# "John": ["Male", "Extroverted", "Travel"]
# }

# name = input("Please enter the name of a user: ")

# if name in userbase:
#     print(f"The profile for {name} is {userbase[name]}")
# else:
#     add = input ("Would you like to add a new entry? (Y/N): ")

#     if add.upper() == "Y":
#         newname = input("What is your name? ")
#         newgender = input("What is your Gender? ")
#         newpersonality = input("What is your Personality? ")
#         newhobby = input("What is your hobby? ")

#         # add this to the dictionary
#         newlist = [newgender, newpersonality, newhobby]

#         userbase[newname] = newlist # add the new person into the dictionary

# print(userbase)
# [2]

# # Task 1.3

# # Copy and paste your program from sub-task 1.2.

# # Edit the program so that it:

# # initialises a new dictionary variable called personalities which contains 
# # the personality types: "Extroverted", "Introverted", "Kind" and "Curious" as keys

# # searches through userbase and adds the names of those with the same 
# # personality together, in personalities.

# # allows the user to input a personality type

# # prints out a message "['N1', 'N2', 'N3'] should be friends as they are all P4.", 
# # where N1, N2, N3 are to be replaced with the names of the persons and P4 to be 
# # replaced with the personality type input by the user.

# # Save your program.


# userbase = {
# "Alice": ["Female", "Extroverted", "Travel"],
# "Bob": ["Male", "Introverted", "Coding"],
# "Carol": ["Female", "Extroverted", "Photography"], 
# "David": ["Male", "Introverted", "Coding"],
# "Emily": ["Female", "Extroverted", "Travel"],
# "Frank": ["Male", "Kind", "Volunteering"],
# "Grace": ["Female", "Kind", "Reading"],
# "Henry": ["Male", "Kind", "Music"],
# "Ivy": ["Female", "Introverted", "Reading"],
# "John": ["Male", "Extroverted", "Travel"],
# "John2": ["Male", "Kind", "Travel"],
# "John3": ["Male", "Curious", "Travel"]
# }

# name = input("Please enter the name of a user: ")

# if name in userbase:
#     print(f"The profile for {name} is {userbase[name]}")
# else:
#     add = input ("Would you like to add a new entry? (Y/N): ")

#     if add.upper() == "Y":
#         newname = input("What is your name? ")
#         newgender = input("What is your Gender? ")
#         newpersonality = input("What is your Personality? ")
#         newhobby = input("What is your hobby? ")

#         # add this to the dictionary
#         newlist = [newgender, newpersonality, newhobby]

#         userbase[newname] = newlist # add the new person into the dictionary

# #######
# # Task 1.3

# userbase = {
# "Alice": ["Female", "Extroverted", "Travel"],
# "Bob": ["Male", "Introverted", "Coding"],
# "Carol": ["Female", "Extroverted", "Photography"]
# }
# personalities = {"Extroverted":[],"Introverted":[],"Kind":[],"Curious":[]}

# for name, profile in userbase.items():

#     # for each name, i pull the personality of that name
#     curr_personality = profile[1]

#     # pull out value from personalities
#     friends = personalities[curr_personality] # 
#     friends.append(name)

#     personalities[curr_personality] = friends
