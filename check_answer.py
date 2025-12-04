# abs() # returns the absolute value
# print(abs(-2)) # return 2


# ascii
# print(chr(90)) # returns the key from
# print(ord("a"))

# generate a random password

# num1 = 100
# num2 = 200
# num3 = num1 + num2

# print(num1, "+", num2, "=", num3)

# # f string
# print(f"{num1} + {num2} = {num3}")

# # format string
# print("{} + {} = {}".format(num1, num2, num3))


# word = "SINGAPORE"

# #<str>.find() # searches for character, returns the index

# check = word.find("GAP")
# print(check)

# ##### split string into list, without using split()

# # email validation
# email = "abc@email.com"

# if email.find("@") == -1:
#     print("email must contain @")

# import math

# print(math.ceil(3.1454675757865676457564))

# print(int(-3.14))

# print("The ".isspace())








# Task 3
# The task is to edit program code so that countries and their capital 
# cities can be added to or removed from a dictionary.

# The following program has a dictionary that contains countries 
# and their capital cities. The program allows the user to:

# • input a country
# • input whether they want to remove a country and 
#    its capital city from the dictionary
# • input whether they want to add a country and its 
#    capital city to the dictionary.


# capital_cities = {
#     'singapore':'Singapore',
#     'japan':'Tokyo', 'australia':'Canberra',
#     'england':'London',
#     'france':'Paris',
#     'germany':'Berlin'
# }

# country = input("Please enter the name of a country: ")
# remove = input("Would you like to remove any of the entries? (Y or N): ")
# add = input("Would you like to add a new entry? (Y or N): ")


# For all sub-tasks, you can assume that all user input is valid.
#  All countries input to be searched or removed are found in the dictionary.

# Task 3.1
# Edit the program so that it:
# • converts the input for country to lower case
# • searches the dictionary for the country input and outputs the capital city of that country.
# Save your program.    [3]

# capital_cities = {
#     'singapore':'Singapore',
#     'japan':'Tokyo', 'australia':'Canberra',
#     'england':'London',
#     'france':'Paris',
#     'germany':'Berlin'
# }

# country = input("Please enter the name of a country: ").lower()
# if country in capital_cities:
#     cap_city = capital_cities[country]
# print(cap_city)



# remove = input("Would you like to remove any of the entries? (Y or N): ")
# add = input("Would you like to add a new entry? (Y or N): ")


# Task 3.2
# Copy and paste your program from sub-task 3.1.
# Edit the program so that if the user enters the value ‘Y’ for remove, the program:
# • allows the user to input a country they want to remove from the dictionary
# • converts the country input to lower case
# • removes the country from the dictionary that is input by the user.

# Save your program.   [3]

# Task 3.3
# Copy and paste your program from sub-task 3.2 .
# Edit the program so that if the user enters the value ‘Y’ for add, the program:
# • allows the user to input a country they want to add to the diction nary
# • allows the user to input the capital city for the country they want to add
# • adds the country and its capital city to the dictionary in the format country:capital
# • outputs the dictionary at the end of the program.

# [4]


# A student is writing a program to note down 
# the favourite sports of each of his classmates.
# the program will help check how many students like a certain sport.

# # Write a program that will 
# # -------------------------------------------------
# # 1. ask how many students there are in the class # ???
# num_students = int(input("Enter the number of students: "))

# # -------------------------------------------------
# sportlist = [] 
# # 2. for each student, ask what is their favourite sport
# for student in range(num_students):
#     sport = input("What is your favourite sport? ")
# 	# 2a. Add the sport into a list
#     sportlist.append(sport)

# print(sportlist) # testing
# # -------------------------------------------------
# # 3. After asking all the student's sport, 
# 	# Ask the user to enter a sport to check how many students like the sport.
# check_sport = input("What sport do you want to check? ") 
# counter = 0

# # -------------------------------------------------
# # 4. if the sport exist, print out how many people like the sport.
# # existence check
# if check_sport in sportlist:
#     # count how many people like it
#     for sport in sportlist:
#         if check_sport == sport:
#             counter = counter + 1 
    
#     print(f"{counter} students like {check_sport}")
# # -------------------------------------------------
# # 5. if the sport does not exist, print out an appropriate message.
# else:
#     print(f"Nobody likes {check_sport}")

# # ** Assume that all inputs given are in lower case and valid.
# # ** the program will work for any number of students.




# A friend matching company wishes to develop an application that helps its users to find friends. 
# It does this by searching through its user database and pairing users with the same hobbies or personalities to one another.

# Open the file FRIENDS.ipynb

# It shows the following program that contains the names and profiles of the users. The program allows the user to:

# input a new name
# input whether they want to add a name and profile to the dictionary.
# For all the sub-tasks in Task 1, you can assume that all user inputs are valid.

# userbase = {
# "Name": ['Gender', 'Personality', 'Hobby'],
# "Alice": ["Female", "Extroverted", "Travel"],
# "Bob": ["Male", "Introverted", "Coding"1,
# "Carol": ["Female", "Extroverted", "Photography"], "David": "Male", "Introverted", "Coding"],
# "Emily": ["Female", "Extroverted", "Travel"),
# "Frank": ["Male", "Kind", "Volunteering"],
# "Grace": "Female", "Kind", "Reading"],
# "Henry": ["Male", "Kind", "Music"],
# "Ivy": ["Female", "Introverted", "Reading",
# "John": ["Male", "Extroverted", "Travel"]

# name = input("Please enter the name of a user: ")
# add = input ("Would you like to add a new entry? (Y/N): ")

# Save the file as:
# TASK1_<your name>_<class>_<index number>.ipynb

# For each of the sub-tasks, begin in a new code cell and add a comment using the 
# hash symbol '#' at the beginning of your code to indicate the sub-task 
# that the program code belongs to.
# For example:

# #Task 1.1

# Program Code

# Task 1.1

# Edit the program so that it:
#  searches the dictionary for the name input and outputs the profile of that name
# asks the user whether the name is to be added as a new entry 
# if the name is not found in the dictionary.

# Save your program.

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

# Task 1.2

# Copy and paste your program from sub-task 1.1.
# Edit the program so that if the user inputs "Y" for add, the program allows the
#  user to input the name and profile of the person to the dictionary in the format 
# "Name": ['Gender', 'Personality', 'Hobby']
# Appropriate messages must be used to prompt the user to input each of the profile field.

# Save your program.

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

# Task 1.3

# Copy and paste your program from sub-task 1.2.

# Edit the program so that it:

# initialises a new dictionary variable called personalities which contains 
# the personality types: "Extroverted", "Introverted", "Kind" and "Curious" as keys

# searches through userbase and adds the names of those with the same 
# personality together, in personalities.

# allows the user to input a personality type

# prints out a message "['N1', 'N2', 'N3'] should be friends as they are all P4.", 
# where N1, N2, N3 are to be replaced with the names of the persons and P4 to be 
# replaced with the personality type input by the user.

# Save your program.


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

# print(personalities)

# # {'Extroverted': ['Alice', 'Carol', 'Emily', 'John'], 'Introverted': ['Bob', 'David', 'Ivy'], 'Kind': ['Frank', 'Grace', 'Henry', 'John2'], 'Curious': ['John3']}
"""
[45.5 / 60]

Task 1 [10/10]
1. 1/1
2. 2/2
3. 1/1
4. 2/2
5. 3/3
6. 1/1

#----------------------------------------------


Task 2 [9.5 / 10]
2.1
a. 3/3
b. 1/1

2.2
5.5/ 6 
-0.5 for unnecessary and strange use of verified variable
#----------------------------------------------

Task 3 [12/ 15]
3.1
4/ 4

3.2
3.5 / 6
-1 infinite loop if "N" entered
-0.5 no suitable output message used when character already exists, currently repeat question only
-1 did not validate for input power to be between 1 and 100

3.3 
4.5 / 5
-0.5 no suitable output message for average


#----------------------------------------------

Task 4
7 / 10

#----------------------------------------------
Task 5 [7 / 15]
5.1
3 / 3

5.2 
4 / 4

5.3 
1/ 6

-1 improper type conversion for time string, unable to continue program
-1 improper code sequence. should not use 6 while loops. 2 while loops with if conditions inside would have been sufficient
-1 did not compute wage amount and output
-2 Program does not work.

-1 no proper comments


"""





# # Task 5.1
# def calculate_minutes(time):
#     hour = time[:2]
#     min = time[3:]

#     hour_num = int(hour)
#     min_num = int(min)

#     total_minutes = hour_num * 60 + min_num

#     return total_minutes

# # print(calculate_minutes("00:30"))
# print(calculate_minutes("22:00"))

# # Task 5.2
# def calculate_wage(clock_in, clock_out):
#     clock_in_mins = calculate_minutes(clock_in)
#     clock_out_mins = calculate_minutes(clock_out)
#     time_in_mins = clock_out_mins - clock_in_mins
#     hour_worked = time_in_mins // 60

#     if hour_worked <= 8:
#         money = hour_worked * 20
#     else:
#         normal_pay = 8 * 20
#         OT = hour_worked - 8
#         OT_pay = OT * 30
#         money = normal_pay + OT_pay

#     return money
    
# print(calculate_wage("00:00", "08:00"))
# print(calculate_wage("00:00", "10:00"))

# # # Task 5.3
# while True:
#     while True:
#         validate_clock_in_time = input("Enter time in the HH:MM format: ")
#         hour = validate_clock_in_time[:2]
#         minute = validate_clock_in_time[3:]
#         if hour >= 00 and hour <= 23:
#             print("Valid hour")
#             break
#         else:
#             print("Invalid hour")
#     while True:
#         validate_clock_in_time = input("Enter time in the HH:MM format: ")
#         if minutes >= 00 and minutes <= 59:
#             print("Valid minute")
#             break
#         else:
#             print("Invalid minute")
#     while True:
#         validate_clock_in_time = input("Enter time in the HH:MM format:")
#         if len(validate_clock_in_time) != 5 and validate_clock_in_time[3] != ":":
#             print("Invalid format")
#         else:
#             print("Valid format")
#             break
#     while True:
#         validate_clock_out_time = input("Enter time in the HH:MM format: ")
#         hours = validate_clock_out_time[:2]
#         minutes = validate_clock_out_time[3:]
#         if hours >= 00 and hours <= 23:
#             print("Valid hour")
#             break
#         else:
#             print("Invalid hour")
#     while True:
#         validate_clock_out_time = input("Enter time in the HH:MM format: ")
#         if minutes >= 00 and minutes <= 59:
#             print("Valid minute")
#             break
#         else:
#             print("Invalid minute")
#     while True:
#         validate_clock_out_time = input("Enter time in the HH:MM format: ")
#         if len(validate_clock_out_time) != 5 and validate_clock_out_time[3] != ":":
#             print("Invalid format")
#         else:
#             print("Valid format")
#             break

#         hours_difference = validate_clock_out_time - validate_clock_in_time
#         if hours_difference > 0:
#             print("Valid Time")
#             break
#         else:
#             print("Invalid time")

###############################################

# count = 0 # 6 count should start from 0
# total = 0
# max_score = 0 # 4 max_score should start from 0
# min_score = 50

# print("Enter student scores (0-50). Enter -1 to send.")
# score = int(input("Enter score: ")) # 1 add bracket
# while score != -1:
#     if score > 0 and score < 50:# 5 change or to and
#         count += 1
#         total = total + score
#         if score > max_score:
#             max_score = score
#         elif score < min_score:
#             min_score = score
# else:
#     print("Invalid score! Please enter 0 - 50 only") # 2 extra indentation
#     score = int(input("Enter score: "))

# print("Processing results...")
# if count == 0: # 3 more equal sign
#     print("No scores were entered")
# else:
#     average = total / count # 7 should only be 1 slash
#     print(f"Number of scores: {count}")
#     print(f"Maximum score: {max_score}\tMinimum score: {min_score}")
#     print(f"Average score: {average}") #8 should be an f string

################################

# character_power = {
#     'mario':50,
#     'luigi':45,
#     'bowser':80,
#     'peach':40,
#     'yoshi':55,
#     'toad':30,
#     'wario':70,
#     'daisy':42,
#     'waluigi':65,
#     'donkey kong':75,
# }

# character = input("Please enter the character name: ")
# add = input("Would you like to add any of the entries (Y or N): ")


#Task 3.1
# character_power = {
#     'mario':50,
#     'luigi':45,
#     'bowser':80,
#     'peach':40,
#     'yoshi':55,
#     'toad':30,
#     'wario':70,
#     'daisy':42,
#     'waluigi':65,
#     'donkey kong':75,
# }

# character = input("Please enter the character name: ").lower()
# if character in character_power:
#     print(f"{character} has a power of {character_power[character]}")
# else:
#     print("character not found in database")
# add = input("Would you like to add any of the entries (Y or N): ")


#Task 3.2
# character_power = {
#     'mario':50,
#     'luigi':45,
#     'bowser':80,
#     'peach':40,
#     'yoshi':55,
#     'toad':30,
#     'wario':70,
#     'daisy':42,
#     'waluigi':65,
#     'donkey kong':75,
# }

# character = input("Please enter the character name: ").lower()
# if character in character_power:
#     print(f"{character} has a power of {character_power[character]}")
# else:
#     print("character not found in database")
# add = input("Would you like to add any of the entries (Y or N): ")

# while True:
#     if add == "Y":
#         new_character = input("Enter the new characters name: ").lower()
#         new_power = int(input("Enter the new character's power level: "))
#         if new_character in character_power:
#             print("Please try again.")
#         else:
#             character_power[new_character] = new_power
#             print("New character has been added to database")
#             print(character_power)
#             break

#Task 3.3
# character_power = {
#     'mario':50,
#     'luigi':45,
#     'bowser':80,
#     'peach':40,
#     'yoshi':55,
#     'toad':30,
#     'wario':70,
#     'daisy':42,
#     'waluigi':65,
#     'donkey kong':75,
# }

# character = input("Please enter the character name: ").lower()
# if character in character_power:
#     print(f"{character} has a power of {character_power[character]}")
# else:
#     print("character not found in database")
# add = input("Would you like to add any of the entries (Y or N): ")
# while True:
#     if add == "Y":
#         new_character = input("Enter the new characters name: ").lower()
#         new_power = int(input("Enter the new character's power level: "))
#         if new_character in character_power:
#             print("Please try again.")
#         else:
#             character_power[new_character] = new_power
#             print("New character has been added to database")
#             print(character_power)
#             break

# highest_power = 0
# strongest_character = ""
# for character in character_power:
#     if character_power[character] > highest_power:
#         highest_power = character_power[character]
#         strongest_character = character
# print(f"The character with the highest power is {strongest_character} with {highest_power}")

# total_power = 0
# count = 0

# for power in character_power.values():
#     total_power += power
#     count += 1

# average_power = total_power / count
# round1dp = round(average_power, 1)
# print(round1dp)

##########################################################

# # from random import randint
# # firstname = input("Enter first name: ")
# # lastname = input("Enter last name: ")
# # library_id = firstname + lastname
# # print("Library ID is " + library_id)
# # pin = ""
# # for i in range(4):
# #     pin += str(randint(0,9))
# # print("PIN is " + pin)

# #Task 2.1(a)
# # from random import randint
# # firstname = input("Enter first name: ")
# # lastname = input("Enter last name: ")
# # year = "2025"
# # library_id = firstname[0] + lastname[-3:] + year
# # print("Library ID is " + library_id.upper())
# # pin = ""
# # for i in range(4):
# #     pin += str(randint(0,9))
# # print("PIN is " + pin)

# # Task 2.1 (b)

# # from random import randint
# # firstname = input("Enter first name: ")
# # lastname = input("Enter last name: ")
# # year = "2025"
# # library_id = firstname[0] + lastname[-3:] + year
# # print("Library ID is " + library_id.upper())
# # pin = ""
# # for i in range(6):
# #     pin += str(randint(0,9))
# # print("PIN is " + pin)

# # Task 2.2 
# from random import randint
# firstname = input("Enter first name: ")
# lastname = input("Enter last name: ")
# year = "2025"
# library_id = firstname[0] + lastname[-3:] + year
# print("Library ID is " + library_id.upper())
# pin = ""

# attempts = 0 
# while attempts < 3:
#     pin = ""
#     for i in range(6):
#         pin += str(randint(0,9))
#     print("PIN is " + pin)
    
#     ENTER_PIN = input("Please enter the pin: ")

#     if ENTER_PIN == pin:
#         print("Library account activated. ")
#         verified = True
#         break
#     else:
#         attempts += 1
#         if attempts < 3:
#             print("PIN not verified! New PIN generated.")
#         else:
#             print("Inactive account! ")














# # -------------------------------------------------
# # Task 5.5

# # Start of 5.1 Code
# def total_cost(cost):
#     tax = cost * 0.09 # calculate the tax of 9%
#     total = cost + tax

#     return total


# print(total_cost(100))

# # Start of 5.2 Code
# def discount(cost):
#     cost = total_cost(cost) # calculate the tax

#     if cost >= 50 and cost < 100:
#         discounted = 0.05 * cost
        
#     elif cost >= 100:
#         discounted = 0.1 * cost
#     else:
#         discounted = 0

#     cost = cost - discounted # apply the discount first

#     return cost

# print(discount(100))


# # Start of 5.3 Code
# def reward_points(total_cost_with_discount):

#     # round down then multiply by 3
#     reward = int(total_cost_with_discount) * 3

#     return reward

# # Start of 5.4 Code
# def voucher(total_cost_with_discount, customer_first_name):
#     if total_cost_with_discount > 25 and total_cost_with_discount <= 50:
#         voucher_code = f"{customer_first_name[:3]}05PERCENT"
#     elif total_cost_with_discount > 50:
#         voucher_code = f"{customer_first_name[:3]}10PERCENT"
#     else:
#         voucher_code = None

#     return voucher_code

# # Start of 5.5 code
# fname = input("Enter Customer's First Name: ")
# cost_of_sale = float(input("Enter the cost of sale: ")) # convert to float

# print("-"*30)
# print("Receipt")

# print(None)

# total_cost_of_sale = total_cost(cost_of_sale)
# print(f"Total cost of sale: ${round(total_cost_of_sale, 2)}")

# discounted_cost = discount(cost_of_sale)
# print(f"Discounted cost of sale: ${round(discounted_cost,2)}")

# rewards = reward_points(discounted_cost)
# print(f"Rewards received: {rewards}")

# vcode = voucher(discounted_cost, fname)
# if vcode == None:
#     print("You need to spend over $25 for a voucher code.")
# else:
#     print(f"Your Voucher Code is {vcode}")

#     with open("vouchercode.txt", "w") as fobj:
#         fobj.write(vcode)

# print("Thank you for shopping. Bye!")
# print("-"*30)