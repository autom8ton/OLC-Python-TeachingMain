'''
Write a program to do number conversion

a) Convert from denary to binary
b) Convert from binary to denary
c) Convert from denary to hexadecimal
e) Convert from hexadecimal to denary
'''
#Write and test your code here



# -------------------------------------------------------------------------
# a) Convert from denary to binary
def den_to_bin(num):
    binary_digit = "" # temporary value

    while num > 0 : # keep dividing by 2 until quotient is zero
        remainder = num % 2 # find the remainder after division by 2
        binary_digit = str(remainder) + binary_digit # add remainder to string at front
        num = num // 2 # update remainder to num

    return binary_digit

print(den_to_bin(231))
# -------------------------------------------------------------------------

# b) Convert from binary to denary

def bin_to_den(binstring):
    decnum = 0 # this variable holds the end result
    length = len(binstring) # find the length of string binary string

    # form the list containing the denary map values
    valuemap = []
    for i in range(length):
        valuemap.append(2**i)

    flippedbinstring = binstring[::-1] # flipped 

    for i in range(length):
        current_denary = int(flippedbinstring[i]) * valuemap[i]
        decnum = decnum + current_denary

    return decnum

print(bin_to_den("11111011"))

# -------------------------------------------------------------------------
# c) Convert from denary to hexadecimal
def den_to_hex(dennum):
    
    hex_digits = "0123456789ABCDEF" # use this to map the den num to hex
    hexes = "" # this is the output result

    while dennum > 0: # keep looping until quotient = 0
        remainder = dennum % 16 # find remainder after divide by 16
        hexes = hex_digits[remainder] + hexes # add to the hexes hexadecimal
        dennum = dennum // 16 # floor divide to continue
    
    return hexes

print(den_to_hex(255))

# -------------------------------------------------------------------------
# e) Convert from hexadecimal to denary

def hex_to_den(hexstring):
    decnum = 0  # this variable holds the final result
    length = len(hexstring)  # length of the hex string
    hexstring = hexstring.upper() # Convert to upper case as hexa is upper case

    # form the list containing the denary map values
    valuemap = []
    for i in range(length):
        valuemap.append(16**i)

    flippedhexstring = hexstring[::-1]  # reverse string for easier processing

    # list of valid hex digits
    hex_digits = "0123456789ABCDEF"

    for i in range(length):
        # find decimal value of the current hex digit
        current_val = flippedhexstring[i] #
        
        # need to map this to a number as the digit could be F
        current_val = hex_digits.find(current_val) # e.g. find the position of F, which will be 15

        # multiply by positional weight from valuemap
        decnum = decnum + (current_val * valuemap[i])

    return decnum

print(hex_to_den("FF"))  # expected 255
print(hex_to_den("1A3")) # expected 419

# -------------------------------------------------------------------------