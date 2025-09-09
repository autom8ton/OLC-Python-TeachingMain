# ________________________________________
# G3 Computing Prelim
# Python Development Question – Parity Bit Validation (25 marks)
# A parity bit is a simple form of error detection used in networking. 
# An extra bit (the parity bit) is added to a binary string so 
# that the total number of 1s (data + parity) is 
# even (EVEN parity) or odd (ODD parity).

# You will write a Python program that checks whether the 
# parity bit of an 8-bit binary string is correct. 
# Use functions with return values, where each function feeds into the next.


# (a) Code validate_parity_mode() [3 marks]
# Write a function validate_parity_mode() that keeps asking the 
# user to enter a parity mode until a valid one is provided.
# Validation rules:
# •	Input must be "ODD" or "EVEN" 
#      (case-insensitive, e.g. odd, Odd, ODD should all be accepted).
# •	The function should return the chosen parity mode in uppercase.

def validate_parity_mode():
    while True:
        parity_mode = input("Enter ODD or EVEN for the parity mode: ").upper()

        # check if it is one of 2 options
        if parity_mode not in ["ODD","EVEN"]:
            print("Parity mode must be either ODD or EVEN.")
        else:
            # return will exit the loop, so you can use it like a break
            return parity_mode






# ________________________________________
# (b) Code get_valid_binary_string() [7 marks]
# Write a function get_valid_binary_string() that keeps 
# asking the user to enter an 8-bit binary string until 
# a valid one is provided.

# Validation rules:
# •	Input length is exactly 8,
# •	Every character is '0' or '1'.
# Return the validated 8-character string.

def get_valid_binary_string():
    while True:
        testbin = input("Enter a 8-bit binary string: ")

        isValid = True
        for binnum in testbin:
            if binnum not in "10":
                isValid = False
                break
        
        if len(testbin) != 8:
            print("Binary string must be 8 characters long.")
        elif isValid == False:
            print("Binary string can only contain 0 or 1.")
        else:
            return testbin
    







# ________________________________________
# (c) Code count_ones(binary_str) [2 marks]
# Write a function count_ones(binary_str) that counts 
# and returns the number of '1' bits in the entire 8-bit string.

def count_ones(binary_str):
    counter = 0
    for i in binary_str:
        if i == "1":
            counter += 1
    
    return counter



# ________________________________________
# (d) Code calculate_expected_parity(binary_str, parity_type) [6 marks]

# Write a function calculate_expected_parity(binary_str, parity_type) that:
# •	Accepts the 8-bit string and a parity type string: "EVEN" or "ODD",

# •	Uses count_ones(...) to obtain the total number of 1s in 
# the data bits only (exclude the last digit on the right)

# •	Returns the expected parity bit as a character '0' or '1', such that:
#   	EVEN parity → total 1s (data + parity) is even,
#       ODD parity → total 1s (data + parity) is odd.


def calculate_expected_parity(binary_str, parity_type):
    data_bits = binary_str[:(len(binary_str) - 1)] # retrieve only data bits

    counts = count_ones(data_bits)

    if parity_type == "EVEN":
        if counts % 2 == 0:
            return '0'
        else:
            return '1'
    elif parity_type == "ODD":
        if counts % 2 == 0:
            return '1'
        else:
            return '0'






# ________________________________________
# (e) Code validate_parity(binary_str, parity_type) [3 marks]
# Write a function validate_parity(binary_str, parity_type) that:
# •	Calls calculate_expected_parity(...) to get the expected parity bit,
# •	Compares it with the actual parity bit (rightmost bit of binary_str),
# •	Returns True if they match, otherwise False.

def validate_parity(binary_str, parity_type):
    correct_parity = calculate_expected_parity(binary_str, parity_type)

    actual_parity = binary_str[-1]

    if correct_parity == actual_parity:
        return True
    else:
        return False





# ________________________________________
# Code the main program [2 marks]
# Your main program should:
# 1.	Ask the user to choose a parity mode ("EVEN" or "ODD"), reprompt until valid,
# 2.	In a loop:
# o	Call get_valid_binary_string() to obtain an 8-bit input,
# o	Call validate_parity(binary_str, parity_type) and display 
# clearly whether the parity is valid or invalid 
# (you may also display the expected parity bit),

# o	Ask if the user wants to check another byte; stop if the user enters N/n.
# ________________________________________
# Program quality [4 marks]
# Your program must include appropriate input and output messages.
# All variables must be appropriately named, and suitable comments 
# must be inserted to explain the algorithm. [4 marks]

# prompt for the mode before the loop. just need to do it once.
parity_mode = validate_parity_mode()

while True:

    binstring = get_valid_binary_string()

    isValidParity = validate_parity(binstring, parity_mode)

    if isValidParity:
        print(f"{binstring} is a valid binary string for {parity_mode} parity check.")
    else:
        print(f"{binstring} is not a valid binary string for {parity_mode} parity check.")

    proceed = input("Do you want to enter another binary string to check? Type N to stop: ").upper()

    if proceed == "N":
        print("Thank you for using parity checker. Bye.")
        break