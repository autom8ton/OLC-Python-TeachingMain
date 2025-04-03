###################################################
# Part 1: Learning Exercises

# Exercise 1: Simple If Condition
# Write a program to check if a number is positive.
# If the number is positive, print "The number is positive."
number = 5
if number > 0:
    print("The number is positive.")


#------------------------------------------------------------
# Exercise 2: If-Else Condition
# Write a program to check if a number is positive or negative.
# Example: If the number is -3, print "The number is negative."
number = -3
if number >= 0:
    print("The number is positive.")
else:
    print("The number is negative.")


#------------------------------------------------------------
# Exercise 3: Using Relational Operators
# Write a program to compare two numbers and print which is 
# larger. Example: Input = 5, 10. Output = "10 is larger."
num1 = 5
num2 = 10
if num1 > num2:
    print("{} is larger.".format(num1))
else:
    print("{} is larger.".format(num2))


#------------------------------------------------------------
# Exercise 4: Multi-Way Selection with If-Elif-Else
# Write a program to check if a number is positive, zero, or 
# negative. Example: Input = 0. Output = "The number is zero."
number = 0
if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")


#------------------------------------------------------------
# Exercise 5: Using Logical Operators (and)
# Write a program to check if a number is divisible by both 3 
# and 5. Example: Input = 15. Output = "Divisible by both."
number = 15
if number % 3 == 0 and number % 5 == 0:
    print("Divisible by both 3 and 5.")
else:
    print("Not divisible by both.")


#------------------------------------------------------------
# Exercise 6: Using Logical Operators (or)
# Write a program to check if a number is divisible by 3 or 5.
# Example: Input = 9. Output = "Divisible by 3 or 5."
number = 9
if number % 3 == 0 or number % 5 == 0:
    print("Divisible by 3 or 5.")
else:
    print("Not divisible by 3 or 5.")


#------------------------------------------------------------
# Exercise 7: Using Logical Operators (not)
# Write a program to check if a number is not divisible by 2.
# Example: Input = 7. Output = "The number is not divisible by 2."
number = 7
if not (number % 2 == 0):
    print("The number is not divisible by 2.")
else:
    print("The number is divisible by 2.")


#------------------------------------------------------------
# Exercise 8: Combining Logical Operators
# Write a program to check if a number is divisible by 2 and 
# not divisible by 3. Example: Input = 10.
# Output = "Divisible by 2 but not divisible by 3."
number = 10
if number % 2 == 0 and not (number % 3 == 0):
    print("Divisible by 2 but not divisible by 3.")
else:
    print("Does not meet the condition.")

