# compare 2 numbers to see which one is bigger
# num1 = 8
# num2 = 10

# # use if condition
# if num1 > num2:
#     # if the above condition is true, run this code
#     print(f"{num1} is more than {num2}")  ### MORE THAN

# elif num1 == num2:
#     print(f"{num1} is equal to {num2}") ### EQUALS TO

# else:
#     # if the above condition is false, run this code
#     print(f"{num1} is not more than {num2}") #### LESS THAN

# PASSWORD PROGRAM

# password = "Password123"

# for i in range(3):
#     inputpassword = input("Enter a password: ") # ask user to enter a password

#     if inputpassword == password:
#         print("Access Granted")
#         break
#     else:
#         print("Access Denied")

# else:
#     print("Account Locked Out.")

# give 3 chances to enter the password.
# if correct password given within 3 chances, say "Access Granted" and program ends
# if incorrect password given 3 times, say "Account locked out" and program ends


### RANDOM NUMBERS
# import random # 

# for i in range(30):
# #     num1 = random.randint(20, 50) # generating a random number between 20 and 50
# #     print(num1)

# ### TASK: MAKE A MATH QUIZ
# marks = 0

# for i in range(10):

#     # generate 2 random numbers
#     num1 = random.randint(1, 10) # gen 1st random number #20
#     num2 = random.randint(1, 10) # gen 2nd random number #30

#     # ask the student to answer
#     # What is 20 + 30 ? 
#     answer = int(input(f"What is {num1} + {num2}? "))

#     # check if the student enter the correct answer
#     if answer == num1 + num2:
#         print("Correct.")
#         # marks = marks + 1
#         marks += 1 # increases the value of marks by 1
#     else:
#         print("Wrong.")

# # tell the student their marks
# print(f"You scored {marks} out of 10.")

# ###### if you fail, print "Go and see Principal"




###########################
# RANDOM NUMBER GUESSING PROGRAM

# # Generate a random number 1 to 100
# import random

# print("*"*50)
# print("Guess my number from 1 to 100!")
# rannum = random.randint(1, 100)

# print(rannum) # testing only, remove later

# # need to loop for 7 times
# for i in range(1, 8):
#     # input the number
#     print(f"This is guess #{i}")
#     guess = int(input("Guess a number: "))

#     if guess > rannum:
#         print(f"Your guess {guess} is too big.")
#     elif guess < rannum:
#         print(f"Your guess {guess} is too small.")
#     else:
#         print(f"{guess} is correct!")
#         break

# else: # note, is for the for loop
#     # if the loop completes naturally
#     print(f"You lost. The number was {rannum}")



# write a program to help categorise how much bus fare to pay

# ask user to input an age

# check if age is a valid number # <str>.isdigit()

# use if, elif and else
# age < 7, free
# between 7 to 12, $2.00
# between 13 to 21, $4.00
# between 22 to 60, $10.00
# 61 and above, $1.00

# Print out the correct fare according to the age.

while True:
    age = input("What is your age? ")
    if age.isdigit():
        age = int(age)

        if age < 7:
            print("Fare is free")
        elif age <= 12:
            print("Fare is $2.00")
        elif age <= 21:
            print("Fare is $4.00")
        elif age <= 60:
            print("Fare is $10.00")
        else:
            print("Fare is $1.00")











## double equal is to check for equality

# num1 = input("Enter first number: ") #10
# num2 = input("Enter second number: ") #10

# for, if, while

# # check if the number is equal, more than or less than

# hour = int(input("WHat hour is it? ")) # 24 - hour clock

# if hour < 7:
#     print("Get ready for school. ")
# elif hour < 8:
#     print("Assembly. ")
# elif hour < 9:
#     print("Math")
# elif hour < 10:
#     print("Recess")
# elif hour < 11:
#     print("Science")
# elif hour < 12:
#     print("Chinese")
# else:
#     print("Go home.")




# ###################################################
# # Part 1: Learning Exercises

# # Exercise 1: Simple If Condition
# # Write a program to check if a number is positive.
# # If the number is positive, print "The number is positive."
# number = 5
# if number > 0:
#     print("The number is positive.")


# #------------------------------------------------------------
# # Exercise 2: If-Else Condition
# # Write a program to check if a number is positive or negative.
# # Example: If the number is -3, print "The number is negative."
# number = -3
# if number >= 0:
#     print("The number is positive.")
# else:
#     print("The number is negative.")


# #------------------------------------------------------------
# # Exercise 3: Using Relational Operators
# # Write a program to compare two numbers and print which is 
# # larger. Example: Input = 5, 10. Output = "10 is larger."
# num1 = 5
# num2 = 10
# if num1 > num2:
#     print("{} is larger.".format(num1))
# else:
#     print("{} is larger.".format(num2))


# #------------------------------------------------------------
# # Exercise 4: Multi-Way Selection with If-Elif-Else
# # Write a program to check if a number is positive, zero, or 
# # negative. Example: Input = 0. Output = "The number is zero."
# number = 0
# if number > 0:
#     print("The number is positive.")
# elif number == 0:
#     print("The number is zero.")
# else:
#     print("The number is negative.")


# #------------------------------------------------------------
# # Exercise 5: Using Logical Operators (and)
# # Write a program to check if a number is divisible by both 3 
# # and 5. Example: Input = 15. Output = "Divisible by both."
# number = 15
# if number % 3 == 0 and number % 5 == 0:
#     print("Divisible by both 3 and 5.")
# else:
#     print("Not divisible by both.")


# #------------------------------------------------------------
# # Exercise 6: Using Logical Operators (or)
# # Write a program to check if a number is divisible by 3 or 5.
# # Example: Input = 9. Output = "Divisible by 3 or 5."
# number = 9
# if number % 3 == 0 or number % 5 == 0:
#     print("Divisible by 3 or 5.")
# else:
#     print("Not divisible by 3 or 5.")


# #------------------------------------------------------------
# # Exercise 7: Using Logical Operators (not)
# # Write a program to check if a number is not divisible by 2.
# # Example: Input = 7. Output = "The number is not divisible by 2."
# number = 7
# if not (number % 2 == 0):
#     print("The number is not divisible by 2.")
# else:
#     print("The number is divisible by 2.")


# #------------------------------------------------------------
# # Exercise 8: Combining Logical Operators
# # Write a program to check if a number is divisible by 2 and 
# # not divisible by 3. Example: Input = 10.
# # Output = "Divisible by 2 but not divisible by 3."
# number = 10
# if number % 2 == 0 and not (number % 3 == 0):
#     print("Divisible by 2 but not divisible by 3.")
# else:
#     print("Does not meet the condition.")






# # get computer to think of a random number 1 - 100
# import random # random library
# rannum = random.randint(1, 100)
# print(rannum)

# for i in range(7):

#     # computer ask me to guess
#     guess = int(input("Guess my number (1 - 100): "))

#     # check if number is more than
#     if guess > rannum:
#         print(f"{guess} is too big. try again.")

#     # check if number is less than
#     elif guess < rannum:
#         print(f"{guess} is too small. try again.")

#     # check if number is equal to
#     else:
#         print(f"{guess} is correct!")
#         break

# ##### code execution - after the loop
# if guess != rannum: #else
#     print("YOu did not guess it.")
#     print(f"The number was {rannum}")


####### i need to repeat this 7 times


# boolean values >>> True / False
# if conditions

# compare 2 numbers
# import random
# random.randint(1, 10)

# num1 = 50 # single equal, value assignment
# num2 = 20

# # > , <, >=, <=, ==
# # print(5 == 5) # value equality

# if num1 > num2: # only when this condition is true
#     # run the code inside
#     print(f"{num1} is bigger than {num2}")
# else:
#     print(f"{num1} is not bigger than {num2}")

