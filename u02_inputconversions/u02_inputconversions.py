
############################################################
# Part 1: Learning Exercises 
# input() and and .format()

# Exercise 1: Using input() for Text
# Write a program to ask the user for their favorite color and display it.
# Example: If the user enters "blue", the program should display
# "Your favorite color is blue."

# color = input("What color do you like: ")
# print("Your favourite color is " + color)

# var1 = 10 # this is integer
# var2 = 20 # this is integer
# var3 = var1 + var2 # + means to add
# # print(var3)

# var4 = "dog" # string
# var5 = "cat" # string
# var6 = var4 + var5 # plus on 2 strings, will join them
# # print(var6)

# var7 = "7"
# var8 = 7
# var9 = var7 * var8
# print(var9)

num1 = int(input("What is the first number? ")) # "10"
num2 = int(input("What is the second number? ")) # 20
answer = num1 + num2

# option 1 of concatenation
# print(str(num1) + " + " + str(num2) + " = " + str(answer))

# option 2 of concatenation, use comma, this only works within a print
# print(num1 , " + " ,num2 , " = " , answer)

# option 3 - .format()
# sentence = "{} + {} = {}".format(num1, num2, answer)
# print(sentence)

# option 4 - f-string
print(f"{num1} + {num2} = {answer}")

#------------------------------------------------------------
# Exercise 2: Understanding input() Behavior
# Write a program to ask the user for their age and display it.
# Example: If the user enters "15", display "Your age is 15."
# Note: Treat the input as a string for now.





#------------------------------------------------------------
# Exercise 3: Comparing String Formatting Methods
# Write a program to ask the user for their name and age and display it
# in three different ways. Example: Input name = "John", age = 15




#------------------------------------------------------------
# Exercise 4: Formatting a Message with .format()
# Write a program to display a sentence about favorite subjects.
# Example: Input subject = "Math", reason = "exciting"


#------------------------------------------------------------
# Exercise 5: Comparing .format() and f-strings for a Calculation
# Write a program to calculate the sum of two numbers and format the
# output in two ways: using .format() and f-strings.
