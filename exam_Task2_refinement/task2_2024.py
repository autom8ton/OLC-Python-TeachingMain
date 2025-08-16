# A school has a new computer network. 
# The following program allows students to create 
# a username and password to log onto the network.

list_username = ["StudentNo1", "JaneJones", "ABC123"]
username = input("Please enter a username: ")
password = input("Please enter a password: ")

# Task 1.1
# Edit the program so that it checks to see 
# if the username entered exists in the list.
# If it does not exist in the list, it must store the username in the list.
# If it does exist in the list, the program must loop 
# until a username is entered that does not already exist in the list.
# [4]

list_usernames = ["StudentNo1", "JaneJones", "ABC123"]

while True:
    username = input("Please enter a username: ")
    if username not in list_usernames: # checks if username not in list
        list_usernames.append(username) # add the username
        break
    print(f"{username} already exists. Enter a new username. ") # show error message

password = input("Please enter a password: ")

# Edit your program so that it checks if the password:
# ·        contains at least one numerical character
# ·        contains at least one special character from: @ ! / ?
# ·        is at least 8 characters in length

# The program should loop until the password 
# fulfils all the three requirements.

# Use suitable input and output messages.
# [6]

special_chars = ['@', '!', '/', '?'] # Specified Special Characters

while True: 
    password = input("Please enter a password: ")

    # Reset checks for each password
    has_number = False
    has_special = False
    is_long_enough = False

    # Check length
    if len(password) >= 8:
        is_long_enough = True

    # Check for number and special char
    for char in password:
        if char.isdigit():
            has_number = True
        elif char in special_chars:
            has_special = True
            
    # Only if all checks pass, the loop will be stopped
    if has_number and has_special and is_long_enough:
        print(f"Password [{password}] is valid")
        break
    else:
        print("Your password must include 1 digit, 1 special character and at least 8 characters long. Please try again.")






