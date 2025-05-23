
###################################################
# Part 1: Learning Exercises

# Exercise 1: Basic While Loop
# Write a program to print numbers from 1 to 5 using a while loop.
# Example: Output = 1, 2, 3, 4, 5.
i = 1
while i <= 5:
    print("Number: {}".format(i))
    i += 1  # Increment i by 1



#------------------------------------------------------------
# Exercise 2: Counting Down with While
# Write a program to print numbers from 5 to 1 using a while loop.
# Example: Output = 5, 4, 3, 2, 1.
i = 5
while i >= 1:
    print("Countdown: {}".format(i))
    i -= 1  # Decrement i by 1



#------------------------------------------------------------
# Exercise 3: Summing Numbers
# Write a program to calculate the sum of numbers from 1 to 10.
# Example: Output = 55.
i = 1
total = 0
while i <= 10:
    total += i  # Add i to total
    i += 1
print("The total sum is: {}".format(total))



#------------------------------------------------------------
# Exercise 4: Repeating User Input
# Write a program that repeatedly asks the user to input a word
# until the user types "stop".
word = ""
while word.lower() != "stop":  # Repeat until "stop" is typed
    word = input("Enter a word (type 'stop' to exit): ")
    print("You entered: {}".format(word))



#------------------------------------------------------------
# Exercise 5: Validating Input
# Write a program to ensure a user enters a number between 1 and 10.
# If the user enters an invalid number, prompt again.
number = int(input("Enter a number between 1 and 10: "))
while number < 1 or number > 10:  # Repeat until valid
    print("Invalid input.")
    number = int(input("Enter a number between 1 and 10: "))
print("You entered: {}".format(number))



#------------------------------------------------------------
# Exercise 6: Using While True for Validation
# Write a program to ensure the user enters a password at least 
# 8 characters long. Use while True to validate the input.
while True:  # Infinite loop for validation
    password = input("Enter a password (at least 8 characters): ")
    if len(password) >= 8:  # Validation condition
        break  # Exit the loop if valid
    print("Password too short. Try again.")
print("Password accepted!")