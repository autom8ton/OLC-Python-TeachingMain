# G3 Computing Prelim Exam
# Python Development Question - Number Base Conversion Library (42 marks)
# You are to write a Python program to perform conversions 
# between binary, denary, and hexadecimal numbers.

# The program must be written using functions with return values, 
# where each function builds on earlier results.

# Your program must include appropriate input and output messages. 
# All variables must be appropriately named, and suitable comments 
# must be inserted to explain the algorithm. [4 marks]


# ________________________________________
# (a) check_valid_num(num, base) - Validate a number according to base [3]
# Purpose: Checks that the user’s input contains only characters allowed in the given base. 

# Write a function check_valid_num(num, base) that:
# Treats num as a string.
#     Returns True only if every character is valid for the given base:
# Base 2: only 0 and 1
# Base 10: only digits 0–9
# Base 16: only 0–9 and letters A–F (case-insensitive)
# Returns False otherwise.

# Task a
def check_valid_num(num, base):

    # change to string for checking
    num = str(num).upper()
    base = str(base)

    for i in num:
        if base == "2" and i not in "01":
            return False
        elif base == "10" and i not in "0123456789":
            return False
        elif base == "16" and i not in "0123456789ABCDEF":
            return False
    
    return True

# print(get_valid_base(15))

# print(check_valid_num("12345", 16))



# ________________________________________
# (b) Binary → Denary [5 marks]
# Write bin_to_den(binstring) that:
# •	Reverses the string so the least significant bit is processed first.
# •	Forms a place-value list [2**0, 2**1, …] matching the string length.
# •	Multiplies each bit by its positional weight and accumulates to a total.
# •	Returns the denary integer.

def bin_to_den(binstring):
    # Reverse the binary string to process least significant bit first
    flippedbin = binstring[::-1]

     # Generate the place-value list [2**0, 2**1, ...]
    place_values = []
    for i in range(len(binstring)):
        place_values.append(2**i)

    dennum = 0
    for i in range(len(flippedbin)):
        current_den = place_values[i] * int(flippedbin[i])
        dennum = dennum + current_den

    return dennum




# ________________________________________
# (c) Denary → Binary [5 marks]
# Write den_to_bin(den_num) that:
# •	Uses repeated division by 2.
# •	Collects remainders and prepends each remainder to build the binary string.
# •	Returns "0" if the input is 0.
# •	Assumes den_num is a non-negative integer.

def den_to_bin(den_num):
    if den_num == 0:
        return "0"
    
    binary_string = "" # temporary value
    num = int(den_num)

    while num > 0 : # keep dividing by 2 until quotient is zero
        remainder = num % 2 # find the remainder after division by 2
        binary_string = str(remainder) + binary_string # add remainder to string at front
        num = num // 2 # update remainder to num

    return binary_string

print(den_to_bin(231))


# ________________________________________
# (d) Denary → Hexadecimal [5 marks]
# Write den_to_hex(den_num) that:
# •	Uses repeated division by 16.
# •	Maps remainders 0..15 to digits using HEX_DIGITS.
# •	Prepends each mapped digit to form the hex string.
# •	Returns "0" if the input is 0.
# •	Assumes den_num is a non-negative integer.


def den_to_hex(dennum):
    if dennum == 0:
        return "0"
    else:
        dennum = int(dennum)
    
    hex_digits = "0123456789ABCDEF" # use this to map the den num to hex
    hexes = "" # this is the output result

    while dennum > 0: # keep looping until quotient = 0
        remainder = dennum % 16 # find remainder after divide by 16
        hexes = hex_digits[remainder] + hexes # add to the hexes hexadecimal
        dennum = dennum // 16 # floor divide to continue
    
    return hexes

print(den_to_hex(255))





# ________________________________________
# (e) Hexadecimal → Denary [8 marks]
# Write hex_to_den(hexstring) that:
# •	Converts input to uppercase.
# •	Reverses the string so the least significant digit is processed first.
# •	Forms a place-value list [16**0, 16**1, …].
# •	For each character, finds its decimal value via HEX_DIGITS, 
#   multiplies by its positional weight, and adds to a running total.
# •	Returns the denary integer.


def hex_to_den(hexstring):
    decnum = 0  # this variable holds the final result
    length = len(hexstring)  # length of the hex string
    hexstring = hexstring.upper() # Convert to upper case as hexa is upper case

    # form the list containing the denary map values
    place_values = []
    for i in range(length):
        place_values.append(16**i)

    flippedhexstring = hexstring[::-1]  # reverse string for easier processing

    # list of valid hex digits
    hex_digits = "0123456789ABCDEF"

    for i in range(length):
        # find decimal value of the current hex digit
        current_val = flippedhexstring[i] #
        
        # need to map this to a number as the digit could be F
        current_val = hex_digits.find(current_val) # e.g. find the position of F, which will be 15

        # multiply by positional weight from valuemap
        decnum = decnum + (current_val * place_values[i])

    return decnum

print(hex_to_den("FF"))  # expected 255
print(hex_to_den("1A3")) # expected 419





# ________________________________________
# (f) Binary → Hexadecimal (bridge via denary) [2 marks]
# Write bin_to_hex(binstring) that:
# •	Validates the binary string (you may reuse checks from part (a) 
#    or assume it has already been validated).
# •	Converts it to denary using your bin_to_den().
# •	Converts that denary value to hexadecimal using your den_to_hex().
# •	Returns the hexadecimal string in uppercase without leading spaces.
# note: This function demonstrates decomposition and reuse (bridge via denary) 
#       rather than re-implementing the grouping algorithm.

def bin_to_hex(binstring):
    den_num = bin_to_den(binstring)

    hex_num = den_to_hex(den_num)

    return hex_num

print(bin_to_hex("1011111"))

# ________________________________________
# (g) Hexadecimal → Binary (bridge via denary) [2 marks]
# Write hex_to_bin(hexstring) that:
# •	Validates the hex string (reuse from (a) or assume already validated); convert to uppercase.
# •	Converts it to denary using your hex_to_den.
# •	Converts that denary value to binary using your den_to_bin.
# •	Returns the binary string (no leading zeros unless the value is zero).

def hex_to_bin(hexstring):
    # call function to conver hex to denary number first
    den_num = hex_to_den(hexstring)

    # call function to convert denary to binary number
    bin_num = den_to_bin(den_num)

    return bin_num


print(hex_to_bin("1FFD"))



# ________________________________________
# (h) Main program [12 marks]
# Write a menu-driven main program that:
# 1.	Displays the following options:
# o	(1) Binary → Denary
# o	(2) Denary → Binary
# o	(3) Denary → Hexadecimal
# o	(4) Hexadecimal → Denary
# o	(5) Binary → Hexadecimal
# o	(6) Hexadecimal → Binary
# o	(7) Exit
# 2.	For the chosen option, calls get_valid_number with the appropriate base 
#       and then the relevant conversion function(s).
# 3.	Displays results clearly, e.g.:
# o	Binary 11111011 = Denary 251
# o	Denary 255 = Hexadecimal FF
# o	Hexadecimal 7B = Binary 1111011
# 4.	Repeats until the user chooses Exit, then prints a closing message.

while True:
    print("(1) Binary to Denary")
    print("(2) Denary to Binary")
    print("(3) Denary to Hexadecimal")
    print("(4) Hexadecimal to Denary")
    print("(5) Binary to Hexadecimal")
    print("(6) Hexadecimal to Binary")
    print("(7) Exit")

    option = input("Choose an option from 1 to 7: ")

    # Continue your code from here.
    if option not in "1234567":
        print("Choose an option from 1 to 7.")
    else:
        if option == "1":
            while True:
                binstring = input("Enter a binary number: ")
                if check_valid_num(binstring, "2"):

                    den_num = bin_to_den(binstring)
                    print(f"Binary {binstring} = Denary {den_num}")
                    break
                else:
                    print(f"{binstring} is not a valid binary number.")

        elif option == "2":
            while True:
                denstring = input("Enter a denary number: ")
                if check_valid_num(denstring, "10"):
                    binnum = den_to_bin(denstring)
                    print(f"Denary {denstring} = Binary {binnum}")
                    break

                else:
                    print(f"{denstring} is not a valid denary number.")

        elif option == "3":
            while True:
                denstring = input("Enter a denary number: ")
                if check_valid_num(denstring, "10"):
                    hexnum = den_to_hex(denstring)
                    print(f"Denary {denstring} = Hexadecimal {hexnum}")
                    break

                else:
                    print(f"{denstring} is not a valid denary number.")

        # (4) Hexadecimal → Denary
        elif option == "4":
            while True:
                hexstring = input("Enter a hexadecimal number: ")
                if check_valid_num(hexstring, "16"):
                    dennum = hex_to_den(hexstring)
                    print(f"Hexadecimal {hexstring} = Denary {dennum}")
                    break

                else:
                    print(f"{hexstring} is not a valid hexadecimal number.")

        # (5) Binary to Hexadecimal
        elif option == "5":
            while True:
                binstring = input("Enter a binary number: ")
                if check_valid_num(binstring, "2"):
                    hexnum = bin_to_hex(binstring)
                    print(f"Binary {binstring} = Hexadecimal {hexnum}")
                    break

                else:
                    print(f"{binstring} is not a valid binary number.")

        # (6) Hexadecimal to Binary
        elif option == "6":
            while True:
                hexstring = input("Enter a hexadecimal number: ")
                if check_valid_num(hexstring, "16"):
                    binnum = hex_to_bin(hexstring)
                    print(f"Hexadecimal {hexstring} = Binary {binnum}")
                    break

                else:
                    print(f"{hexstring} is not a valid hexadecimal number.")

        elif option == "7":
            print(f"You have chosen (7) Exit. Bye.")
            break






















# '''
# Write a program to do number conversion

# a) Convert from denary to binary
# b) Convert from binary to denary
# c) Convert from denary to hexadecimal
# e) Convert from hexadecimal to denary
# '''
# #Write and test your code here



# # -------------------------------------------------------------------------
# # a) Convert from denary to binary
# def den_to_bin(num):
#     binary_digit = "" # temporary value

#     while num > 0 : # keep dividing by 2 until quotient is zero
#         remainder = num % 2 # find the remainder after division by 2
#         binary_digit = str(remainder) + binary_digit # add remainder to string at front
#         num = num // 2 # update remainder to num

#     return binary_digit

# print(den_to_bin(231))
# # -------------------------------------------------------------------------

# # b) Convert from binary to denary

# def bin_to_den(binstring):
#     decnum = 0 # this variable holds the end result
#     length = len(binstring) # find the length of string binary string

#     # form the list containing the denary map values
#     valuemap = []
#     for i in range(length):
#         valuemap.append(2**i)

#     flippedbinstring = binstring[::-1] # flipped 

#     for i in range(length):
#         current_denary = int(flippedbinstring[i]) * valuemap[i]
#         decnum = decnum + current_denary

#     return decnum

# print(bin_to_den("11111011"))

# # -------------------------------------------------------------------------
# # c) Convert from denary to hexadecimal
# def den_to_hex(dennum):
    
#     hex_digits = "0123456789ABCDEF" # use this to map the den num to hex
#     hexes = "" # this is the output result

#     while dennum > 0: # keep looping until quotient = 0
#         remainder = dennum % 16 # find remainder after divide by 16
#         hexes = hex_digits[remainder] + hexes # add to the hexes hexadecimal
#         dennum = dennum // 16 # floor divide to continue
    
#     return hexes

# print(den_to_hex(255))

# # -------------------------------------------------------------------------
# # e) Convert from hexadecimal to denary

# def hex_to_den(hexstring):
#     decnum = 0  # this variable holds the final result
#     length = len(hexstring)  # length of the hex string
#     hexstring = hexstring.upper() # Convert to upper case as hexa is upper case

#     # form the list containing the denary map values
#     valuemap = []
#     for i in range(length):
#         valuemap.append(16**i)

#     flippedhexstring = hexstring[::-1]  # reverse string for easier processing

#     # list of valid hex digits
#     hex_digits = "0123456789ABCDEF"

#     for i in range(length):
#         # find decimal value of the current hex digit
#         current_val = flippedhexstring[i] #
        
#         # need to map this to a number as the digit could be F
#         current_val = hex_digits.find(current_val) # e.g. find the position of F, which will be 15

#         # multiply by positional weight from valuemap
#         decnum = decnum + (current_val * valuemap[i])

#     return decnum

# print(hex_to_den("FF"))  # expected 255
# print(hex_to_den("1A3")) # expected 419

# # -------------------------------------------------------------------------