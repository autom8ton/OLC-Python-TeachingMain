# firstname = input("Please enter your first name: ").lower()
# lastname = input("Please enter your last name: ").lower()
# email_id = firstname[:3] + lastname + "@example.com"
# print("Your email ID is " + email_id)


# Task 2.1 [2 mark]
# Edit the program to ensure that the email ID is 
# created using the first letter of the first name 
# and the last three characters of the last name. 
# Assume that the last name will always have at least 3 characters.
#[start: stop: step]

#################################
# # Task 2.1 
firstname = input("Please enter your first name: ").lower()
lastname = input("Please enter your last name: ").lower()
#  first letter of the first name last three characters of the last name. 
# email_id = firstname[:3] + lastname + "@example.com"
email_id = firstname[0] + lastname[-3:] + "@example.com"
print("Your email ID is " + email_id)

# word = "SINGAPORE"
# print(word[0:-3]) # [start: stop: step]


# print(word[-4:]) #[start from -3]

#################################

# Task 2.2 [3 marks]

# After generating the email ID, ask the user to 
# retype the email address to confirm they have 
# noted it down correctly. Edit the program to:

# ·        Ask the user to re-enter the generated email address.
# ·        Check that the entered email contains the '@' symbol and at least 1 dot.
# ·        If the input does not contain '@', display an error message and prompt the user again.
# ·        Check that the input email is the same as generated email.
# ·        Repeat this until a valid format is entered.
# email_id = "jick@example.com"
# print(email_id.find("!"))

while True:
    checkemail = input("Enter your email id again to confirm: ")
    # if find returns -1, means cannot find.
    if checkemail.find("@") == -1:
        print("Symbol '@' missing from email. ")
    elif checkemail.find(".") == -1:
        print("Symbol '.' missing from email. ")
    elif checkemail != email_id:
        print(f"Input email {checkemail} does not match generated email {email_id}")
    else:
        print(f"Email {checkemail} is valid.")
        break

# Task 2.3 [5 marks]

# Edit the program to generate a random password 
# for the user after confirming the email. The password must:
# Be exactly 8 characters long
# Contain at least one uppercase letter (ASCII codes 65 to 90)
# Contain at least one lowercase letter (ASCII codes 97 to 122)
# Contain at least one digit (ASCII codes 48 to 57)
# Display the generated password to the user after it is created.

# ord() chr()


# name = "MARK"
# sentence = "{} is a good guy".format(name)


# generate a random number between the range they specify
# import random
# rannum = random.randint(65, 90)
# char = chr(rannum)
# # print(char)
# import random


# var1= chr(random.randint(48,57))
# print(var1)

import random

password = "" # empty string at the start
password += chr(random.randint(65,90)) # ensure 1 upper
password += chr(random.randint(97,122)) # ensure 1 lower
password += chr(random.randint(48,57)) # ensure 1 digit

# print(password)
# # remaining characters
for i in range(5):
    ranchoice = random.randint(1,3)
    if ranchoice == 1:
        nextchar = chr(random.randint(65,90))
    elif ranchoice == 2:
        nextchar = chr(random.randint(97,122))
    elif ranchoice == 3:
        nextchar = chr(random.randint(48,57))

    password += nextchar
print(password)
# # optional to ensure randomness
listpw = list(password) # change to a list so can use shuffle
random.shuffle(listpw) # shuffle the list items

password = "" # resetting back to empty to build back
for c in listpw:
    password += c
### End optional ################

print(f"Your password is {password}")


