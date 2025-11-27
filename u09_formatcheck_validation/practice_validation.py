'''
Question 1 (Length Check):
Write the input entry and validation code for a program that
needs to accept a 4-digit OTP (One-Time Password)
The OTP must be exactly 4 digits long

If the input is invalid, your code should keep trying
by asking for the input to be entered again.

#########################################

'''

# how to check for length

# pin = "123445394578247982347923479283498"
# print(len(pin))

# input validation
while True:
    otp = input("Enter a 4 digit OTP: ")

    # validation both for length and for numbers
    if not otp.isdigit():
        print("OTP must be a number!")
    elif len(otp) != 4:
        print("OTP must be 4 digits!")
    else:
        # means that OTP is valid
        # otp = int(otp)
        print("OTP is valid.")
    

## continue on with other code as required







# Scenario: Validate a password to ensure it is at least 8 characters long and contains:
# - At least one uppercase letter.
# - At least one lowercase letter.
# - At least one digit.

# Example:
# Input: "Secure123"
# Output: "Valid password"

# Input: "password"
# Output: "Invalid password"

## Bonus: Print out which of the requirement failed.
 

# testpw = "SEEEECURe1"
# print(testpw.isupper())
# print(testpw.isdigit())
# print(testpw.islower())

# # - At least one uppercase letter.
# # - At least one lowercase letter.
# # - At least one digit.

# while True:
#     # boolean flag
#     hasUpper = False 
#     hasLower = False
#     hasNumber = False

#     password = input("Enter a password: ")

#     # loop through every single character
#     for char in password:
#         if char.isupper():
#             hasUpper = True # found one upper case
#         elif char.islower():
#             hasLower = True # found one lower case
#         elif char.isdigit():
#             hasNumber = True # found one number

#     # check the flags
#     if hasUpper and hasLower and hasNumber and len(password) >= 8:
#         print(f"{password} is a valid password.")
#         break
#     else:
#         print(f"Please try again.")
#         if not hasUpper:
#             print(f"{password} is missing an upper case character.")
#         if not hasLower:
#             print(f"{password} is missing an upper case character.")   
#         if not hasNumber:
#             print(f"{password} is missing number.")         
#         if len(password) < 8:
#             print(f"Password should have at least 8 characters")              
        





# while True:
#     password = input("Enter your password: ")

#     if len(password) >= 8:
#         for char in password:
#             if char.isupper():
#                 print("valid password.")
#             elif char.isdigit():
#                 print("Valid password")
#             else: 
#                 print("Invalid password. Password must be one lowercase letter, one number and one uppercase letter")
#     else:
#        print("Invalid password. Password must be eight characters, one lowercase letter and one uppercase letter")

    


# Exercise 7: Extracting Middle Elements from a List
# Scenario: Extract the middle 3 elements from a list with an odd 
# # number of elements.
# numbers = [10, 20, 30, 40, 50, 60, 70]
# # 30, 40, 50

# # find the middle element
# middle = len(numbers) // 2 # floor division
# print(middle)

# print(numbers[middle-1])
# print(numbers[middle])
# print(numbers[middle+1])