# string, integer, floats, boolean, list, dictionary

food = ["hamburger",
           "pasta",
           "pizza",
           "fries",
           "nuggets"]

price = [2,
        15,
        21,
        5,
        6]

# key/ value
# key must be unique
menu = {"hamburger":2,
        "pasta":15,
        "pizza":21,
        "fries":5,
        "nuggets":6}

###################################################
# Part 1: Learning Exercises

# Practice Exercise 1: Creating a Dictionary
# Create a dictionary to store student names and their grades.
students = {"Alice": 85, "Bob": 90, "Charlie": 78}





#------------------------------------------------------------
# Practice Exercise 2: Accessing Dictionary Values
# Access Bob's grade from the dictionary.
students = {"Alice": 85, "Bob": 90, "Charlie": 78}

bobgrade = students["Bob"] # pull out a value using the key
print(bobgrade)




#------------------------------------------------------------
# Practice Exercise 3: Adding New Key-Value Pairs
# Add a new student, Diana, with a grade of 92 to the dictionary.
students = {"Alice": 85, "Bob": 90, "Charlie": 78}

students["Diana"] = 92 # add a new key/ value
print(students)

# if the key does not exist, then it will add
# but if key already exist, it will update


#------------------------------------------------------------
# Practice Exercise 4: Updating Existing Values
# Update Charlie's grade to 80 in the dictionary.
students = {"Alice": 85, "Bob": 90, "Charlie": 78}

students["Charlie"] = 80
print(students)



#------------------------------------------------------------
# Practice Exercise 5: Deleting Key-Value Pairs
# Remove Alice's entry from the dictionary.
students = {"Alice": 85, "Bob": 90, "Charlie": 78}

del(students["Alice"])
print(students)



#------------------------------------------------------------
# Practice Exercise 6: Checking for Existence of a Key
# Check if 'Diana' is in the student dictionary.
students = {"Alice": 85, "Bob": 90, "Charlie": 78}

stu = "Bob"
if stu in students:
    print(f"{stu} is in the class")
else:
    print(f"{stu} is not in the class")



#------------------------------------------------------------
# Practice Exercise 7: Iterating Through a Dictionary
# Print all student names and their grades.
students = {"Alice": 85, "Bob": 90, "Charlie": 78}

for stu, score in students.items(): # read the values
    print(f"{stu} scored {students[stu]}")
    

######
for stu in students: # stu is the key
    # print(stu) # key
    # print(students[stu]) # value from dictionary using key

    # print(f"{stu} scored {students[stu]}")
    students[stu] = students[stu] - 10
print(students)








#------------------------------------------------------------



###########################################################
# Part 2. IN-CLASS Practice Exercises

# In-Class Exercise 1: Student Grades Analysis
# Scenario: A teacher needs to analyze student performance.
# Create a dictionary with student names as keys and grades as values.
students = {
    'Ali': 88, 'Benny': 75, 'Chloe': 92, 'Diana': 85,
    'Ethan': 78, 'Farid': 81, 'Grace': 66, 'Haziq': 94,
    'Ivy': 71, 'Jun': 88, 'Ullas':45, 'Josephine':98,
    'Sor Lang': 23, 'Jimmy': 5, 'Borui': 78, 'Esther': 9}

# Task 1: Identify and print the name of the highest scoring student.
# [2,5,7,45,45,35,3413436,46,345,4356,4567]

# maxscore = 0
# maxname = ""

# for student, score in students.items():
#     print(student)
#     print(score)
#     if score > maxscore:
#         maxscore = score 
#         maxname = student

# print(f"{maxname} has the highest score of {maxscore}")

#------------------------------------------------------------
# Task 2: Calculate and display the number of students scoring above 80.



#------------------------------------------------------------
# Task 3: Update all grades by adding 5 points as a bonus.




#------------------------------------------------------------
# In-Class Exercise 2: Inventory Stock Management
# Scenario: A warehouse manager needs to manage product stock levels.
inventory = {"Apples": 50, "Bananas": 30, "Oranges": 20, "Grapes": 60}

# Task 1: Add a new product "Pineapples" with an initial stock of 40.




#------------------------------------------------------------
# Task 2: Find and print the total stock of all items combined.




#------------------------------------------------------------
# Task 3: Identify and remove any product with stock below 25.



#------------------------------------------------------------
# In-Class Exercise 3: Library Book Management
# Scenario: A librarian tracks the availability of books in a dictionary.
books = {
    "1984": {"status": "Available", "copies": 5},
    "Brave New World": {"status": "Checked Out", "copies": 0},
    "Fahrenheit 451": {"status": "Available", "copies": 2},
}

#------------------------------------------------------------
# Task 1: Add a new book "To Kill a Mockingbird" with 3 copies.



#------------------------------------------------------------
# Task 2: Update the status of "1984" to "Checked Out" if all copies are borrowed.




#------------------------------------------------------------
# Task 3: Print all books currently available along with their copy count.






#------------------------------------------------------------
# In-Class Exercise 4: Customer Orders Tracking
# Scenario: A store tracks orders with customers and the items they purchased.
orders = {
    "John": ["Apples", "Bananas"],
    "Mary": ["Oranges", "Grapes"],
    "Alice": ["Bananas", "Pineapples"],
}

# Task 1: Add a new order for "Mark" who purchased "Apples" and "Oranges".





#------------------------------------------------------------
# Task 2: Count and print the total number of unique items purchased by all customers.



#------------------------------------------------------------
# Task 3: Identify customers who purchased "Bananas".



#------------------------------------------------------------
