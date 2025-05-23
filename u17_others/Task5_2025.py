
# In [1]:    # Task 2.1
#           Program Code
#           Output:
# All code should have appropriate comments and all identifiers should be appropriately named. [4]

# Task 5.1
# Write a shift() function that has the parameter char passed to it. 
# The function must shift a lower-case letter down the alphabet sequence 
# by one position (a → b ... → y → z → a) and do nothing to other characters.    
#[4]

###############################################################
#### Note from T.DAVID - This sample question is from MOE for Y2025 Sample
#### Usually, you would use the ASCII table to do caesar encryption.
#### But since, details were not provided, we used a string instead
#### for translation.
###############################################################


def shift(char):
    # alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*() "
    oidx = alpha.find(char)

    newindex = (oidx + 1) % len(alpha) # shift by 1 letter, and handle wrap-around with modulus

    return alpha[newindex] # return the shifted character


# Task 5.2
# Write a function encrypt() that has the parameters message and positions 
# passed to it. The function must use the shift() function to encrypt the
#  message argument by shifting all the lower-case letters in the message 
# down the alphabet sequence by the number of positions given in the positions argument. 
# The function should ignore all other characters.                     [7]

# assume the return is the encrypted message
def encrypt(message, positions):
    cyphertext = ""

    # loop through every character
    for c in message:

        temp = c # using a temp variable to hold encrypted value for each character

        for i in range(positions): # looping through however many times according position parameter
            temp = shift(temp) # shifts 1 by 1 

        cyphertext += temp
    
    return cyphertext

print(encrypt("aaaaa", 5))

# Task 5.3
# Write a function shift_up() that has the parameter char passed to it. 
# The function must shift a lower-case letter up the alphabet sequence by 
# one position (a ← b ... ← y ← z ← a) and do nothing to other characters.  
#[2]

def shift_up(char):
    # alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*() "

    oidx = alpha.find(char)
    newidx = (oidx - 1) % len(alpha)

    return alpha[newidx]

print(shift_up("b"))

# Task 5.4
# Write a function decrypt() that has the parameters ciphertext and 
# positions passed to it. The function must use the shift_up() function 
# to decrypt the ciphertext argument by shifting all the letters up the 
# alphabet sequence by the number of positions given in the positions argument. 
# The function should ignore all other characters.      [1]

def decrypt(ciphertext, positions):
    message = ""

    # loop through every character
    for c in ciphertext:

        temp = c # using a temp variable to hold encrypted value for each character

        for i in range(positions): # looping through however many times according position parameter
            temp = shift_up(temp) # shifts 1 by 1 

        message += temp
    
    return message

print(decrypt("ccc", 1))

# Task 5.5
# Create a simple text-based user interface to:
# • request the user to enter ‘E’ to encrypt a message or ‘D’ to
#  decrypt a ciphertext (case insensitive) and to re-enter 
# if the input is not ‘E’, ‘D’, ‘e’ or ‘d’

# • request the user to enter the message or the ciphertext
# • request the user to enter the number of positions to shift the 
# letters and the user to re-enter the number if the input is not a positive integer

# • output the encrypted message and write the encrypted message to the file 
# encrypted.txt, if the user requested to encrypt a message

# • output the decrypted ciphertext if the user requested to decrypt a message.

# Your program should use the encrypt() and decrypt() functions. 
# Test your program with the following input:

#                         a, E, This is the seCret me55age!, -1, 12   

#  Save your JupyterLab notebook for Task 5 [7]

# infinite loop
while True:
    option = input("Input E to encrypt, or D to decrypt: ")
    if option not in ['E', 'e', 'D', 'd']:
        print("You must only enter E or D.")
    else:
        msg = input("What is the message or ciphertext: ")
        # validate for the positions, make sure it is a positive integer
        while True:
            pos = input("Enter the number of positions to shift by: ")
            if pos.isdigit() and int(pos) > 0:
                pos = int(pos)
                break
            else:
                print("Position must be a positive integer.")

        # the start of encrypting or decrypting
        if option.lower() == "e":
            output = encrypt(msg, pos)

            # output the encrypted message to a file encrypted.txt
            with open("encrypted.txt", "w") as fobj:
                fobj.write(output)

        elif option.lower() == "d":
            output = decrypt(msg, pos)

        print(output)

