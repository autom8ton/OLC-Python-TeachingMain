

# integer
# var1 = 10 # integer # do math here
# var2 = "10" # string
# var3 = 3.14 # float
# var4 = True # or False Boolean

# var5 = [1, 2, 3, 4, 5] # list of numbers


menu = {"hamburger": 6, "pizza": 15, "fries": 5, "coke": 2}
menu["sausage"] = 6
print(menu)

# # how to retrieve a value from the dictionary
# # example retrieve price of pizza
# pizzaprice = menu["pizza"]
# print(f"The price of pizza is ${pizzaprice}")

# # how to add a new key value/ pair into dictionary
# print(menu) # before adding
# menu["hotdog"] = 9
# print(menu) # after adding

# # how to change the value of key/ value pair
# menu["hamburger"] = 10
# print(menu)

# # check for existence for a key in dictionary
# choice = input("What do you want to eat? ")
# if choice in menu:
#     print(f"Yes, I sell {choice}")
#     #add code here to tell customer the price
#     print(f"Give me ${menu[choice]}")
# else:
#     print(f"Sorry, I do not sell {choice}. Go next door.")

# # how to loop through the items in the dictionary
# print("Welcome to my restaurant!")
# print('Here is the menu')
# for food,price in menu.items():
#     print(f"{food} : ${price}")


# # the more traditional way of looping through dictionary
# for food in menu:
#     print(food) # loops through the key in dictionary
#     print(menu[food]) # pulls out the value in dictionary
















# # string, integer, floats, boolean, list, dictionary
# # key and value pair

# # define a dictionary 
# countries = {"malaysia":"kuala lumpur", "china":"beijing", "indonesia":"jakarta"}

# # how to retrieve a value from dictionary
# cap1 = countries["malaysia"]
# print(cap1)

# # add to dictionary
# countries["japan"] = "tokyo" # if the key does not exist, it will add it
# print(countries)

# # change a value in a dictionary
# countries["japan"] = "osaka" # if the key does exist, it will change the value
# print(countries)

# # delete a key/ value pair from dictionary
# del countries["malaysia"]
# print(countries)

# # check whether a particular key exist in dictionary # existance check
# if "malaysia" in countries:
#     print("malaysia exists")
# else:
#     print("malaysia does not exist")

# # how to loop through all the key/ value pairs in dictionary
# for country, capital in countries.items():
#     # print(country)
#     # print(capital)
#     print(f"The capital of {country} is {capital}.")


# #### Code a Restaurant Ordering Program

# # Task 1: Create a dictionary containing 3 food items and their prices

# # Task 2: Ask customer what they want to eat?

# # Task 3: Check if order is available
#             # if available, print the price
#             # else, tell customer not available



# # Challenge: Advanced Grade Analysis
 
# # Scenario: A teacher needs detailed analysis of class performance.
# students = {"Alice": 85, "Bob": 78, "Charlie": 92, "Diana": 88, "Eve": 76}

# # Task 1: Find and print the names of students who scored below the average grade.

# # average >>> add up total / number students

# # average

# # for student,score in students.items():
# #     if score < average:
# #         print(f"{student} scored less than {average}")


# #------------------------------------------------------------
# # Task 2: Create a new dictionary with students categorized as "Pass" or "Fail".
# # Assume a passing grade is 80 or above.
# # print a message warning students who fail e.g. Bob failed! You need to work harder.





















# # food = ["hamburger",
# #            "pasta",
# #            "pizza",
# #            "fries",
# #            "nuggets"]

# # price = [2,
# #         15,
# #         21,
# #         5,
# #         6]

# # # key/ value
# # # key must be unique
# # menu = {"hamburger":2,
# #         "pasta":15,
# #         "pizza":21,
# #         "fries":5,
# #         "nuggets":6}

# # ###################################################
# # # Part 1: Learning Exercises

# # # Practice Exercise 1: Creating a Dictionary
# # # Create a dictionary to store student names and their grades.
# # students = {"Alice": 85, "Bob": 90, "Charlie": 78}





# # #------------------------------------------------------------
# # # Practice Exercise 2: Accessing Dictionary Values
# # # Access Bob's grade from the dictionary.
# # students = {"Alice": 85, "Bob": 90, "Charlie": 78}

# # bobgrade = students["Bob"] # pull out a value using the key
# # print(bobgrade)




# # #------------------------------------------------------------
# # # Practice Exercise 3: Adding New Key-Value Pairs
# # # Add a new student, Diana, with a grade of 92 to the dictionary.
# # students = {"Alice": 85, "Bob": 90, "Charlie": 78}

# # students["Diana"] = 92 # add a new key/ value
# # print(students)

# # # if the key does not exist, then it will add
# # # but if key already exist, it will update


# # #------------------------------------------------------------
# # # Practice Exercise 4: Updating Existing Values
# # # Update Charlie's grade to 80 in the dictionary.
# # students = {"Alice": 85, "Bob": 90, "Charlie": 78}

# # students["Charlie"] = 80
# # print(students)



# # #------------------------------------------------------------
# # # Practice Exercise 5: Deleting Key-Value Pairs
# # # Remove Alice's entry from the dictionary.
# # students = {"Alice": 85, "Bob": 90, "Charlie": 78}

# # del(students["Alice"])
# # print(students)



# # #------------------------------------------------------------
# # # Practice Exercise 6: Checking for Existence of a Key
# # # Check if 'Diana' is in the student dictionary.
# # students = {"Alice": 85, "Bob": 90, "Charlie": 78}

# # stu = "Bob"
# # if stu in students:
# #     print(f"{stu} is in the class")
# # else:
# #     print(f"{stu} is not in the class")



# # #------------------------------------------------------------
# # # Practice Exercise 7: Iterating Through a Dictionary
# # # Print all student names and their grades.
# # students = {"Alice": 85, "Bob": 90, "Charlie": 78}

# # for stu, score in students.items(): # read the values
# #     print(f"{stu} scored {students[stu]}")
    

# # ######
# # for stu in students: # stu is the key
# #     # print(stu) # key
# #     # print(students[stu]) # value from dictionary using key

# #     # print(f"{stu} scored {students[stu]}")
# #     students[stu] = students[stu] - 10
# # print(students)








# #------------------------------------------------------------



# ###########################################################
# # Part 2. IN-CLASS Practice Exercises

# # In-Class Exercise 1: Student Grades Analysis
# # Scenario: A teacher needs to analyze student performance.
# # Create a dictionary with student names as keys and grades as values.
# students = {
#     'Ali': 88, 'Benny': 75, 'Chloe': 92, 'Diana': 85,
#     'Ethan': 78, 'Farid': 81, 'Grace': 66, 'Haziq': 94,
#     'Ivy': 71, 'Jun': 88, 'Ullas':45, 'Josephine':98,
#     'Sor Lang': 23, 'Jimmy': 5, 'Borui': 78, 'Esther': 9}

# # Task 1: Identify and print the name of the highest scoring student.
# # [2,5,7,45,45,35,3413436,46,345,4356,4567]

# # maxscore = 0
# # maxname = ""

# # for student, score in students.items():
# #     print(student)
# #     print(score)
# #     if score > maxscore:
# #         maxscore = score 
# #         maxname = student

# # print(f"{maxname} has the highest score of {maxscore}")

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
