###################################################
# Part 1: Learning Exercises

# Exercise 1: Converting to Uppercase
# Write a program to convert a string to uppercase.
# Example: Input = "hello", Output = "HELLO".
# word = "i want to eat chicken rice."
# uppercase_word = word.upper()  # Convert to uppercase
# print("Uppercase: {}".format(uppercase_word))

# animal = input("Enter an animal: ").lower()
# if animal.lower() == "tiger":
#     print("User typed tiger")
# else:
#     print("User did not type tiger")


# #------------------------------------------------------------
# # Exercise 2: Converting to Lowercase
# # Write a program to convert a string to lowercase.
# # Example: Input = "HELLO", Output = "hello".
# word = "THIS IS A TIGER"
# lowercase_word = word.lower()  # Convert to lowercase
# print("Lowercase: {}".format(lowercase_word))




# #------------------------------------------------------------
# # Exercise 3: Checking if a String is Uppercase
# # Write a program to check if a string is fully uppercase.
# # Example: Input = "HELLO", Output = True.
# word = "Hello"
# is_upper = word.isupper()  # Check if uppercase
# print("Is '{}' uppercase? {}".format(word, is_upper))




# #------------------------------------------------------------
# # Exercise 4: Checking if a String is Lowercase
# # Write a program to check if a string is fully lowercase.
# # Example: Input = "hello", Output = True.
# word = "Hello"
# is_lower = word.islower()  # Check if lowercase
# print("Is '{}' lowercase? {}".format(word, is_lower))




# #------------------------------------------------------------
# # Exercise 5: Checking if a String is Alphanumeric
# # Write a program to check if a string contains only letters 
# # and numbers.
# # Example: Input = "Python123", Output = True.
# word = "%$#%$#"
# is_alnum = word.isalnum()  # Check if alphanumeric
# print("Is '{}' alphanumeric? {}".format(word, is_alnum))

# # ask user to enter a username
# while True:
#     uname = input("ENter a username: ")
#     if uname.isalnum():
#         print("Accepted")
#         break
#     else:
#         print("Must only contain alphabets or numbers")




# #------------------------------------------------------------
# # Exercise 6: Checking if a String is Alphabetic
# # Write a program to check if a string contains only letters.
# # Example: Input = "Python", Output = True.
# word = "Python1"
# is_alpha = word.isalpha()  # Check if alphabetic
# print("Is '{}' alphabetic? {}".format(word, is_alpha))

# while True:
#     name = input("Enter your name: ")
#     if name.isalpha():
#         print(f"Hello {name}")
#         break
#     else:
#         print("Name can only contain alphabet")


# #------------------------------------------------------------
# # Exercise 7: Checking if a String is Numeric
# # Write a program to check if a string contains only numbers.
# # Example: Input = "12345", Output = True.
# word = "12345"
# is_digit = word.isdigit()  # Check if numeric
# print("Is '{}' numeric? {}".format(word, is_digit))

# # while True:
# #     phone = input("Enter a 8 digit phone number: ")
# #     if phone.isdigit():
# #         print(f"{phone} is a valid number. ")
# #         break
# #     else:
# #         print("Can only contain numbers. ")

# while True:
#     number = input("Enter a number: ")

#     if number.isdigit():
#         number = int(number)

#         print(number * number)
#         break
#     else:
#         print("You must enter a number.")


# #------------------------------------------------------------
# # Exercise 8: Removing Extra Spaces
# # Write a program to remove leading and trailing spaces.
# # Example: Input = "  hello  ", Output = "hello".
# word = "  hello world    "
# stripped_word = word.strip()  # Remove spaces
# print("Stripped string: '{}'".format(stripped_word))




# #------------------------------------------------------------
# # Exercise 9: Length Validation
# # Write a program to validate that a string has at least 5 
# # characters. Prompt the user repeatedly until they enter a 
# # valid string.
# while True:
#     user_input = input("Enter a string with at least 5 characters: ")
#     if len(user_input) >= 5:
#         break  # Exit loop if valid
#     print("String too short. Try again.")
# print("Valid string: {}".format(user_input))




# #------------------------------------------------------------




###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 10: Validating Uppercase Input
# Scenario: You are entering product codes into a system, and 
# all codes must be in uppercase letters (e.g., "ABC123").

# codes = input("Enter product code: ")
# if codes.isupper():
#     print("pass")
# else:
#     print("Product code mst be in upper case")




#------------------------------------------------------------
# Exercise 11: Validating Alphanumeric Input
# Scenario: A username field only accepts alphanumeric characters
# (letters and numbers) without special symbols.






#------------------------------------------------------------
# Exercise 12: Validating Numeric Input
# Scenario: You are collecting a phone number that must contain 
# only numeric characters.






#------------------------------------------------------------
# Exercise 13: Checking for Substrings
# Scenario: You are searching for the word "Python" in user 
# feedback to categorize responses related to Python programming.






#------------------------------------------------------------
# Exercise 14: Replacing Parts of a String
# Scenario: A user entered their old email address, and you 
# need to replace it with a new domain (e.g., from "@old.com" to "@new.com").






#------------------------------------------------------------
# # Assignment 1: Password Validation
# Scenario: Validate a password to ensure it is at least 8 characters long and contains:
# # - At least one uppercase letter. .isupper()
# # - At least one lowercase letter. .islower()
# # - At least one digit.            .isdigit()
                                        #len()

# # Example:
# # Input: "Secure123"
# # Output: "Valid password"

# # Input: "password"
# # Output: "Invalid password: missing uppercase letter and digit"

# # Input: "PASSWORD123"
# # Output: "Invalid password: missing lowercase letter"







while True:
    password = input("Type a password: ")

    # setup some flags (boolean value)
    # lengthok = False

    upperok = False
    lowerok = False
    digitok = False

    # loop through all the characters in the given password
    for c in password:
        if c.isupper():
            upperok = True
        elif c.islower():
            lowerok = True
        elif c.isdigit():
            digitok = True

    if not upperok:
        print("Your password is missing upper case")
    if not lowerok:
        print("Your password is missing lower case")
    if not digitok:
        print("Your password is missing numbers")

    if upperok and lowerok and digitok and len(password)>8:
        print(f"{password} is valid. ")
        break
    else:
        print(f"{password} is not valid. ")



