
# In [1]:    # Task 2.1
#           Program Code
#           Output:
# All code should have appropriate comments and all identifiers should be appropriately named. [4]

###############################################################
#### Note from T.DAVID - This sample question is from MOE for Y2025 Sample
#### Usually, you would use the ASCII table to do caesar encryption.
#### But since, details were not provided, we used a string instead
#### for translation.
###############################################################


# Task 5.1
# Write a shift() function that has the parameter char passed to it. 
# The function must shift a lower-case letter down the alphabet sequence 
# by one position (a → b ... → y → z → a) and do nothing to other characters.    
#[4]

####
# ASCII TABLE

# find the number for "a"

# This is the seCret me55age!
def shift(char):
    alpha = "abcdefghijklmnopqrstuvwxyz"

    # find the position of a character in the alpha string
    oidx = alpha.find(char) 

    newidx = (oidx + 1) % 26 # to shift 

    # find the new character
    newchar = alpha[newidx]

    # return this new char
    return newchar

print(shift("a"))





# Task 5.2
# Write a function encrypt() that has the parameters message and positions 
# passed to it. The function must use the shift() function to encrypt the
#  message argument by shifting all the lower-case letters in the message 
# down the alphabet sequence by the number of positions given in the positions argument. 
# The function should ignore all other characters.                     [7]

# assume the return is the encrypted message

def encrypt(message, positions):
    alpha = "abcdefghijklmnopqrstuvwxyz"

    ciphertext = "" # hold the eventual encrypted message

    # loop through every single character
    for c in message:
        if c in alpha:
            temp = c # temporary value before shift
            for i in range(positions):
                temp = shift(temp) # call the function 
            
            ciphertext += temp # concatenates back the encrypted character
        else:
            ciphertext += c # not a lowercase, i just add back
    
    return ciphertext # contain the encrypted message


print(encrypt("this is a message 55 !", 5))

# Task 5.3
# Write a function shift_up() that has the parameter char passed to it. 
# The function must shift a lower-case letter up the alphabet sequence by 
# one position (a ← b ... ← y ← z ← a) and do nothing to other characters.  
#[2]




def shift_up(char):

    # ASCII METHOD ord() chr()
    # need to offset the starting character from 97 to 0
    oidx = ord(char) - ord('a') # finds me the ordinal value of the character #97

    newindex = ord('a') + (oidx - 1 ) % 26  # finds the encrypted index

    newchar = chr(newindex) # find the corresponding char from ASCII

    return newchar

print(shift_up("a"))



# Task 5.4
# Write a function decrypt() that has the parameters ciphertext and 
# positions passed to it. The function must use the shift_up() function 
# to decrypt the ciphertext argument by shifting all the letters up the 
# alphabet sequence by the number of positions given in the positions argument. 
# The function should ignore all other characters.      [1]
def decrypt(message, positions):
    alpha = "abcdefghijklmnopqrstuvwxyz"

    msg = "" # hold the eventual encrypted message

    # loop through every single character
    for c in message:
        if c in alpha:
            temp = c # temporary value before shift
            for i in range(positions):
                temp = shift_up(temp) # call the function 
            
            msg += temp # concatenates back the decrypted character
        else:
            msg += c # not a lowercase, i just add back
    
    return msg # contain the decrypted message

print(decrypt("ccccc", 1))



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
while True:
    option = input("Enter E to encrypt, D to decrypt: ")

    # checking if it is E or D
    if option.lower() not in ['e', 'd']:
        print("You can only enter E or D")
    else:
        stringval = input("Enter the message to encrypt or ciphertext to decrypt: ")

        # validating for positions input
        while True:
            pos = input("Enter a number for positions to shift by: ")
            if pos.isdigit() and int(pos) > 0:
                pos = int(pos)
                break
            else:
                print("You can only enter a positive integer for positions. ")

        if option.lower() == 'e':
            output = encrypt(stringval, pos)

            # output a file encrypted.txt
            with open("encrypted.txt", "w") as fobj:
                fobj.write(output) # write the encrypted value to a file
        elif option.lower() == 'd':
            output = decrypt(stringval, pos)
        
        print(output)
