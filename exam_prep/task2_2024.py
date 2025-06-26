# number >>>> .isdigit() Can only check 1 character
# special characters # existence check in a list
# 8 character long len()

list_usernames = ["StudentNo1", "JaneJones", "ABC123"]
new_username = False # To checks if new username is keyed in
while True:
    username = input("Please enter a username: ")
    if username not in list_usernames: # checks if username not in list
        list_usernames.append(username) # add the username
        break
    print(f"{username} already exists. Enter a new username. ") # show error message

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
        break
    else:
        print("Your password must include 1 digit, 1 special character and at least 8 characters long. Please try again.")
