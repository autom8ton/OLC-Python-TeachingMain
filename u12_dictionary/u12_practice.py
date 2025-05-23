##########################################################################
# Scenario 3:Filtering High Electricity Consumption in Households
# A power company monitors monthly electricity usage for different households.
# Calculate the average electricity consumption in this block
# and store households which is above the average in a new dictionary called overuse.
# 
# Print a message to all these households advising them to save electricity
# Example: 
# "Unit 03-02, Electricity Consumption of 541 kwh is higher than the average of 354. "

electricity_usage = {
    "Unit 01-01": 450, "Unit 01-02": 158, "Unit 01-03": 320,
    "Unit 02-01": 700, "Unit 02-02": 550, "Unit 02-03": 400,
    "Unit 03-01": 210, "Unit 03-02": 346, "Unit 03-03": 548,
    "Unit 04-01": 235, "Unit 04-02": 536, "Unit 04-03": 650
}

# Write your code here 

print(len(electricity_usage))
print(sum(electricity_usage.values()))




##########################################################



# list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
#          5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
#          1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
#          756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
#          2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
#          6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
#          6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
#          4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
#          5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
#          4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]


# # sum of all values / number of value
# average = sum(list1) / len(list1)
# # print(average)

# # expected to know how to calculate sum manually
# sumnum = 0 # starting value
# count = 0 # starting count value

# for num in list1:
#     sumnum = sumnum + num # sumnum += num
#     count = count + 1

# print(sumnum)
# print(count)

# average = sumnum / count
# print(average)



# list of numbers
# nums = [78,34,4,23,6763,4676,3423,2,9867,568]

# newnums = sorted(nums, reverse = True)
# # print(newnums)

# names = ["Desmond", "Ben", "Edmund", "Albert", "Charlie","Frank"]
# newnames = sorted(names, reverse = True)
# # print(newnames)

# # Dictionary
# students_scores = {"Desmond":98, "Ben":23,"Albert":75, "Charlie":65}

# scores = sorted(students_scores.values())
# print(scores)

# newscores = sorted(students_scores.items())
# print(newscores)

# newdict = dict(newscores)
# print(newdict)


# # create dictionary containing your menu items, and the price
# menu = {"Burger":5.9, "Pasta":12, "Pizza":21, "Fries":3, "Nugget":6}

# # print out to the customer the 
# # things you sell 



# # Ask customer what do they want to buy
# # order = input("What do you want to buy? ")

# # Check if item is in dictionary

#     # If exist, then say the price
    

# # else say don't exist





# # Task 3.1
# # Edit the program so that it:
# # • converts the input for country to lower case
# # • searches the dictionary for the country input and 
# # outputs the capital city of that country.
# # Save your program.    [3]

# # Task 3.2
# # Copy and paste your program from sub-task 3.1.
# # Edit the program so that if the user enters the value ‘Y’ 
# # for remove, the program:
# # • allows the user to input a country they want to remove from the dictionary
# # • converts the country input to lower case
# # • removes the country from the dictionary that is input by the user.
# # Save your program.   [3]

# capital_cities = {
#     'singapore':'Singapore', 'japan':'Tokyo', 'australia':'Canberra',
#     'england':'London', 'france':'Paris','germany':'Berlin' }

# country = input("Please enter the name of a country: ").lower()

# # add = input("Would you like to add a new entry? (Y or N): ")

# # check if this country exist in dictionary
# if country in capital_cities:
#     print(f"The capital of {country} is {capital_cities[country]}")

# remove = input("Would you like to remove any of the entries? (Y or N): ")
# #### check if user type Y for remove
# if remove == "Y":
#     country = input("Please enter the name of a country: ").lower()
#     del(capital_cities[country])

# print(capital_cities)










# ###########################################################
# # Part 2. IN-CLASS Practice Exercises

# # In-Class Exercise 1: Student Grades Analysis
# # Scenario: A teacher needs to analyze student performance.
# # Create a dictionary with student names as keys and grades as values.
# students = {"Alice": 85, "Bob": 78, "Charlie": 92, "Diana": 88, "Eve": 76}

# # Task 1: Identify and print the name of the highest scoring student.



# #------------------------------------------------------------
# # Task 2: Calculate and display the number of students scoring above 80.



# #------------------------------------------------------------
# # Task 3: Update all grades by adding 5 points as a bonus.




# #------------------------------------------------------------
# # In-Class Exercise 2: Inventory Stock Management
# # Scenario: A warehouse manager needs to manage product stock levels.
# inventory = {"Apples": 50, "Bananas": 30, "Oranges": 20, "Grapes": 60}

# # Task 1: Add a new product "Pineapples" with an initial stock of 40.




# #------------------------------------------------------------
# # Task 2: Find and print the total stock of all items combined.




# #------------------------------------------------------------
# # Task 3: Identify and remove any product with stock below 25.



# #------------------------------------------------------------
# # In-Class Exercise 3: Library Book Management
# # Scenario: A librarian tracks the availability of books in a dictionary.
# books = {
#     "1984": {"status": "Available", "copies": 5},
#     "Brave New World": {"status": "Checked Out", "copies": 0},
#     "Fahrenheit 451": {"status": "Available", "copies": 2},
# }

# #------------------------------------------------------------
# # Task 1: Add a new book "To Kill a Mockingbird" with 3 copies.



# #------------------------------------------------------------
# # Task 2: Update the status of "1984" to "Checked Out" if all copies are borrowed.




# #------------------------------------------------------------
# # Task 3: Print all books currently available along with their copy count.






# #------------------------------------------------------------
# # In-Class Exercise 4: Customer Orders Tracking
# # Scenario: A store tracks orders with customers and the items they purchased.
# orders = {
#     "John": ["Apples", "Bananas"],
#     "Mary": ["Oranges", "Grapes"],
#     "Alice": ["Bananas", "Pineapples"],
# }

# # Task 1: Add a new order for "Mark" who purchased "Apples" and "Oranges".





# #------------------------------------------------------------
# # Task 2: Count and print the total number of unique items purchased by all customers.



# #------------------------------------------------------------
# # Task 3: Identify customers who purchased "Bananas".



# #------------------------------------------------------------