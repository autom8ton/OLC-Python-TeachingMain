# ________________________________________
# G3 Computing Prelim Exam
# Python Development Question - NRIC Checksum Validation (25 marks)
# You are to write a Python program to check whether 
# a Singapore NRIC entered by the user is valid.

# The program must be written using functions with return values, 
# where each function builds on the results of the previous one.
# At the top of your program, declare the following constants:

# # Lookup tables for checksum
CHECKSUM_TABLE_ST = {10:"A", 9:"B", 8:"C", 7:"D", 6:"E", 5:"F", 4:"G", 3:"H", 2:"I", 1:"Z", 0:"J"}

CHECKSUM_TABLE_FG = {10:"K", 9:"L", 8:"M", 7:"N", 6:"P", 5:"Q", 4:"R", 3:"T", 2:"U", 1:"W", 0:"X"}

# # Weights for each digit
WEIGHTS = [2, 7, 6, 5, 4, 3, 2]


# Your program must include appropriate input and output messages.
# All variables must be appropriately named, and suitable comments
#  must be inserted to explain the algorithm. [4 marks]
# ________________________________________
# (a) Input and validation [5 marks]
# Write a function get_valid_nric() that keeps asking the user to enter an NRIC until a valid NRIC is provided.
# The function should check that:
# -The NRIC has exactly 9 characters,
# -The first character is S, T, F, or G,
# -The last character is an alphabet,
# -The middle 7 characters are digits.
# The function should only return the NRIC string (in uppercase) once all the checks have passed.

def get_valid_nric():
    while True:
    # code to get and check valid nric

    # once check pass, return the valid nric.
    pass

nric = get_valid_nric()





# ________________________________________
# (b) Weighted sum calculation [5 marks]
# Write a function calculate_weighted_sum(nric) that:
# -Extracts the 7 digits in the middle of the NRIC,
# -Multiplies each digit by its corresponding weight in WEIGHTS,
# -Adds the results together,
# -If the prefix is T or G, adds 4 to the total.
# The function should return the weighted sum.






# ________________________________________
# (c) Determine expected checksum letter [3 marks]
# Write a function calculate_checksum_letter(nric, total) that:
# -Calculates remainder = total % 11,
# -Uses the correct dictionary (CHECKSUM_TABLE_ST or 
# CHECKSUM_TABLE_FG) depending on the first character of the NRIC,
# -Returns the expected checksum letter.
# -Note that total is the weighted sum from the output 
# of the function calculate_weighted_sum(nric)






# ________________________________________
# (d) Validate the NRIC [3 marks]
# Write a function validate_nric(nric) that:
# -Calls calculate_weighted_sum(nric) to get the total,
# -Calls calculate_checksum_letter(nric, total) to find the expected letter,
# -Compares the expected letter with the last character of the NRIC,
# -Returns True if valid, False otherwise.




# ________________________________________

# (e) Code the main program [5 marks]
# The main program should:
# 1.	Repeatedly call get_valid_nric() to obtain a valid NRIC from the user.
# 2.	Pass the returned NRIC to the function validate_nric().
# 3.	Display a clear message to indicate whether the NRIC is valid or invalid.
# 4.	After each check, ask the user if they want to continue.
#       If the user enters N (or n), the program should stop and display a closing message.
#       Otherwise, the program should continue and prompt for another NRIC.







# ________________________________________


########### ANSWER BELOW #################


# ________________________________________
# G3 Computing Prelim Exam
# Python Development Question - NRIC Checksum Validation (25 marks)
# You are to write a Python program to check whether 
# a Singapore NRIC entered by the user is valid.

# The program must be written using functions with return values, 
# where each function builds on the results of the previous one.
# At the top of your program, declare the following constants:

# # Lookup tables for checksum
CHECKSUM_TABLE_ST = {10:"A", 9:"B", 8:"C", 7:"D", 6:"E", 5:"F", 4:"G", 3:"H", 2:"I", 1:"Z", 0:"J"}

CHECKSUM_TABLE_FG = {10:"K", 9:"L", 8:"M", 7:"N", 6:"P", 5:"Q", 4:"R", 3:"T", 2:"U", 1:"W", 0:"X"}

# # Weights for each digit
WEIGHTS = [2, 7, 6, 5, 4, 3, 2]


# Your program must include appropriate input and output messages.
# All variables must be appropriately named, and suitable comments
#  must be inserted to explain the algorithm. [4 marks]
# ________________________________________
# (a) Input and validation [5 marks]
# Write a function get_valid_nric() that keeps asking the user to enter an NRIC until a valid NRIC is provided.
# The function should check that:
# -The NRIC has exactly 9 characters,
# -The first character is S, T, F, or G,
# -The last character is an alphabet,
# -The middle 7 characters are digits.
# The function should only return the NRIC string (in uppercase) once all the checks have passed.


def get_valid_nric():

    while True:
        nric = input("Enter an NRIC: ").upper()

        if len(nric) != 9: # check for length
            print(f"NRIC must be exactly 9 characters long. Your input [{nric}]")

        elif nric[0] not in "STFG": # check first letter is S,T,F,G
            print(f"NRIC must start with S, T, F or G. Your input [{nric}]")

        elif not nric[-1].isalpha(): # check last letter is alphabet
            print(f"NRIC must end with an alphabet. Your input [{nric}]")

        elif not nric[1:8].isdigit(): # check middle 7 are numbers
            print(f"NRIC must have 7 digits. Your input [{nric}]")
            
        else:
            # if code gets here, the above checks have passed.
            print(f"NRIC {nric} format is correct.")
            return nric

# ________________________________________
# (b) Weighted sum calculation [5 marks]
# Write a function calculate_weighted_sum(nric) that:
# -Extracts the 7 digits in the middle of the NRIC,

# - Multiplies each digit by its corresponding weight in WEIGHTS [2, 7, 6, 5, 4, 3, 2],
# o	For example, if your NRIC is S1111111Z, then the calculation will be
#  (1x2) + (1x7) + (1x6) + (1 x 5) + (1 x 4) + (1 x 3) + (1 x 2)

# -Adds the results together,
# -If the prefix is T or G, adds 4 to the total.
# The function should return the weighted sum.

def calculate_weighted_sum(nric):

    weighted_sum = 0

    digits = nric[1:8]

    # loop through both the digits and the weights to multiply
    for i in range(len(digits)):
        digitsum = int(digits[i]) * WEIGHTS[i]
        weighted_sum = weighted_sum + digitsum

    # add 4 if T or G
    if nric[0] in "TG":
        weighted_sum = weighted_sum + 4
    
    return weighted_sum




# ________________________________________
# (c) Determine expected checksum letter [3 marks]
# Write a function calculate_checksum_letter(nric, total) that:
# -Calculates remainder = total % 11,
# -Uses the correct dictionary (CHECKSUM_TABLE_ST or 
# CHECKSUM_TABLE_FG) depending on the first character of the NRIC,
# -Returns the expected checksum letter.
# -Note that total is the weighted sum from the output 
# of the function calculate_weighted_sum(nric)


def calculate_checksum_letter(nric, total):
    remainder = total % 11

    if nric[0] in "ST":
        checksum_letter = CHECKSUM_TABLE_ST[remainder]

    elif nric[0] in "FG":
        checksum_letter = CHECKSUM_TABLE_FG[remainder]

    return checksum_letter



# ________________________________________
# (d) Validate the NRIC [3 marks]
# Write a function validate_nric(nric) that:
# -Calls calculate_weighted_sum(nric) to get the total,
# -Calls calculate_checksum_letter(nric, total) to find the expected letter,
# -Compares the expected letter with the last character of the NRIC,
# -Returns True if valid, False otherwise.


def validate_nric(nric):
    total = calculate_weighted_sum(nric)

    checksum = calculate_checksum_letter(nric, total)

    if checksum == nric[-1]:
        return True
    else:
        return False

# ________________________________________

# (e) Code the main program [5 marks]
# The main program should:
# 1.	Repeatedly call get_valid_nric() to obtain a valid NRIC from the user.
# 2.	Pass the returned NRIC to the function validate_nric().
# 3.	Display a clear message to indicate whether the NRIC is valid or invalid.
# 4.	After each check, ask the user if they want to continue.
#       If the user enters N (or n), the program should stop and display a closing message.
#       Otherwise, the program should continue and prompt for another NRIC.

while True:
    nric = get_valid_nric()

    isvalid = validate_nric(nric)

    if isvalid:
        print(f"{nric} is a valid NRIC.")
    else:
        print(f"{nric} is not a valid NRIC.")

    proceed = input("Do you want to continue? Type N to stop: ").upper()

    if proceed == "N":
        print("Thank you for using NRIC validator. Bye.")
        break
    else:
        print("Continuing on to next NRIC.. ")






# ________________________________________

