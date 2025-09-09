
# Exercise 0: Modulus and Floor Division
# Write a program to calculate the modulus and floor division
# of two numbers. Example: 17 divided by 5.
# num1 = 17
# num2 = 5
# modulus = num1 % num2
# floor_div = num1 // num2
# print("17 % 5 is:", modulus)
# print("17 // 5 is:", floor_div)

# print(157//2) # floor divide to find the quotient
# print(157%2) # modulus to find the remainder

#------------------------------------------------------------
# For Loops through List
#------------------------------------------------------------

# Exercise 1: Printing Items (Method 1)
# Given fruits = ["apple", "banana", "cherry"]
# Use a for loop to print each fruit directly.
# Output example:
# I like to eat apple.
# I like to eat banana.
# I like to eat cherry.

# for loop
# range(10)
# range(1, 10)
# range(1, 11, 1)
# list [1,2,3,4]
# string "SINGAPORE"
# dictionary

fruits = ["apple", "banana", "cherry"]

for i in fruits:
    print(i)




#------------------------------------------------------------
# Exercise 2: Printing Items (Method 2)
# Given the same fruits list
# Use for i in range(len(fruits)) to print the items.
# Output example:
# Fruit 1: apple
# Fruit 2: banana
# Fruit 3: cherry
fruits = ["apple", "banana", "cherry"]

# print(fruits[0]) # apple
# print(fruits[1]) # banana
# print(fruits[2]) # cherry

len(fruits) # return the count of how many items are in the list

# loop through a list using the index
for i in range(len(fruits)):
    print(fruits[i])



#------------------------------------------------------------
# Exercise 3: Numbers Greater than 50
# Given numbers = [12, 67, 45, 89, 23]
# Use a for loop to print only numbers greater than 50.
# Expected Output:
# 67
# 89






#------------------------------------------------------------
# Exercise 4: Mapping Students to Scores
# students = ["Ali", "Bala", "Cindy"]
# marks = [55, 80, 62]
# Use a for loop to combine them into a dictionary.
# Expected Output:
# {"Ali": 55, "Bala": 80, "Cindy": 62}

students = ["Ali", "Bala", "Cindy"]
marks = [55, 80, 62]

student_marks = {} # declare a empty dictionary

student_marks["John"] = 56
## add a key/ value manually 
# add to dictionary is dictionary[key] = value
print(student_marks)

# access items from both list using the index
for i in range(len(students)):
    current_student = students[i] # pulls out the current student e.g. Ali
    current_mark = marks[i] # pulls out the current mark e.g. 55

    student_marks[current_student] = current_mark
    ### ???

# print(student_marks)
#------------------------------------------------------------
# While Loop Validation
#------------------------------------------------------------

# Exercise 5: Length Check
# Keep asking user for a username until it has at least 5 characters.
# check to ensure that username is all alphabets
# while True:
#     username = input("What is the username: ")
#     if len(username) < 5:
#         print("Invalid. username must be at least 5 characters")
#     else:
#         break




# ----------------------------------------------------------------

# Exercise 6: Numbers Only
# Keep asking user to enter age until input contains digits only.





# ----------------------------------------------------------------

# Exercise 7: Uppercase Only
# Keep asking until user enters a code in uppercase letters only.





# ----------------------------------------------------------------

# Exercise 8: Lowercase Only
# Keep asking until user enters an email in lowercase only.





# ----------------------------------------------------------------

# Exercise 9: Password Validation
# Keep asking until user enters a password with length >= 8.






# (a) Input and validation [5 marks]
# Write a function get_valid_number(base) that:
# •	Accepts a parameter base which can be 2 or 10.
# •	Repeatedly asks the user to enter a number in that base until a valid number is provided.
# •	Checks that:
# o	For base 2: input only contains characters 0 and 1.
# o	For base 10: input only contains digits 0–9 (treat the value as a non-negative integer).
# •	Returns the number string (no leading/trailing spaces).
# Hint: Use .strip() and validate all characters before returning.
def get_valid_number(base):
    while True:
        number = input(f"Enter a number in base {base}: ")
        isValid = True # assume that this number is valid

        if base == "2":
            for i in number:
                if i not in "01":
                    isValid = False
        elif base == "10":
            for i in number:
                if int(i) <0 or int(i) > 9:
                    isValid = False
        else:
            isValid = False
            print("Number must be either 2 or 10.")
        
        if isValid:
            return number # acts like a break, it exits out of function
        else:
            print(f"{number} is not valid for base {base}")
            

# parameter = input("Enter a parameter base of 2 or 10: ")
# result =  get_valid_number("2") # 2 or 10

# print(result)




# ----------------------------------------------------------------
# (b) Binary → Denary [6 marks]
# Write a function bin_to_den(binstring) that:
# •	Reverses the string so the least significant bit is processed first,
# •	Forms a place-value list [2**0, 2**1, …] matching the string length,
# •	Multiplies each bit by its positional weight and accumulates the total,
# •	Returns the denary integer.
# Example: bin_to_den("11111011") should return 251.




# ----------------------------------------------------------------




