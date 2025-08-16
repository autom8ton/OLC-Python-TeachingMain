
# caesar encryption - 
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# "ADVANCE" - DGYDQFH - ADVANCE # KEY = 3

letter = "J"
key = 3

# find the index of F in the alphabet
index = letters.find(letter)
# print(index)

# shift by 3 letters
newindex = index + 3 

# find the corresponding encrypted letter
encrypted_char = letters[newindex]

print(encrypted_char)


# ###################################################
# # Part 1: Learning Exercises

# # Exercise 1: Absolute Value of a Difference
# # Find the absolute difference between two numbers.
# # Example: Temperatures of two cities.

# temp1 = 30
# temp2 = 56

# difference = temp1 - temp2
# # print(abs(difference))




# # #------------------------------------------------------------
# # # Exercise 2: Convert Character to ASCII
# # # Convert a character to its ASCII code and back again.

# letter = "H"

# # find ordinal value (decimal value) from the ascii
# ordH = ord(letter) # ordinal
# # print(ordH) # retrieves the ordinal number of H from ascii table

# letterH = chr(72) # character
# # print(letterH)




# # #------------------------------------------------------------
# # # Exercise 3: Generating a Random Uppercase Letter
# # # Generate a random uppercase letter using ASCII values.
# # 65 - 90
# import random

# rannum = random.randint(65, 90)
# ranletter = chr(rannum)

# # print(ranletter)

# # GENERATE a string only containing upper case letters (min length = 8)

# # "".join()

# pw = ""
# for i in range(8):
#     rannum = random.randint(65, 90) # pick a random number between 65 to 90
#     ranletter = chr(rannum) # gets the ascii value from the table
#     pw = pw + ranletter

# # print(pw)



# # #------------------------------------------------------------
# # # Exercise 4: Generate ASCII Symbols
# # # Generate a random special character from ASCII values.

# # generate a password with 8 random special characters






# # #------------------------------------------------------------


# ### BONUS
# # Generate a password containing the following
# # 3 upper case letters
# # 3 lower case letters
# # 3 special characters
# # 3 numbers

# ## BONUS BONUS: randomize the position





# #########
# ## HANDLING UPPER CASE LETTERS
# key = 6

# MESSAGE = "TOMORROW I WANT TO EAT PIZZA"

# ## ENCRYPT BY SHIFTING TO THE RIGHT BY 6 (key)

# encmsg = ""
# # Loop through the message
# for letter in MESSAGE:
#     # find the ordinal value of this letter

#     num = ord(letter)

#     numplus = num + key

#     newchar = chr(numplus) # contains the encrypted letter

#     encmsg = encmsg + newchar

# print(encmsg)

# ########################

# encrypted = "L ORYH SLCCD GHDUOB DQG FRPSXWLQJ LV IXQ"


# for i in range(6):
#     decmsg = ""
#     for l in encrypted:
#         numminus = ord(l) - i
#         newchar = chr(numminus)
#         decmsg = decmsg + newchar
#     print(f"Key{i}: {decmsg} \n")

# ###########################################################
# # Part 2. IN-CLASS Practice Exercises

# # Exercise 6: Random Username Generator
# # The format is:
# # first 3 characters of first name
# # first 3 character of last name
# # plus 3 printable characters from ASCII
# # Scenario: Generate a random 9-character username using uppercase letters and digits.


# firstname = "ADAM"
# lastname = ""
# print(f"{firstname[:3]}{lastname[-3:]}{chr(random.randint(32, 126))}{chr(random.randint(32, 126))}{chr(random.randint(32, 126))}")