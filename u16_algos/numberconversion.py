# ________________________________________
# Task 4 – Development of a Digital Storage Unit Converter (25 marks)
# You are developing a Python program to convert digital storage values between SI units (e.g. MB, GB) and binary units (e.g. MiB, GiB).
# All conversions must be done using bytes as an intermediate unit.
# The following partial dictionary is provided to you:
conversion_factors = {
    "B": 1,
    "kB": 1000,
    "MB": 1000**2,
    "KiB": 1024,
    "MiB": 1024**2
}
# ________________________________________
# Task 4.1 – Complete the Dictionary [2 marks]
# Extend the conversion_factors dictionary to include the following units:
# •	SI units: "GB", "TB", "PB"
# •	Binary units: "GiB", "TiB", "PiB"
# Use the appropriate powers of 1000 for SI units and 1024 for binary units.
conversion_factors = {
    "B": 1,
    "kB": 1000,
    "MB": 1000**2,
    "GB": 1000**3,
    "TB": 1000**4,
    "PB": 1000**5,
    "KiB": 1024,
    "MiB": 1024**2,
    "GiB": 1024**3,
    "TiB": 1024**4,
    "PiB": 1024**5
}
# ________________________________________

# Task 4.2 – Validation Function [4 marks]
# Write a function named is_valid_unit(unit) that:
# •	Takes in a string unit
# •	Returns True if the unit is a valid key in the conversion_factors dictionary
# •	Returns False otherwise
# This function will be used to check whether the user has entered a supported unit.
def is_valid_unit(unit):
    if unit in conversion_factors:
        return True
    else:
        return False

print(is_valid_unit("MB"))
# ________________________________________
# Task 4.3 – Conversion Function [7 marks]
# Write a function named convert_storage(value, from_unit, to_unit) that:
# •	Takes in three parameters:
# o	value (a numeric value to convert)
# o	from_unit (the current unit)
# o	to_unit (the target unit)
# •	Converts the value using the following steps:
# 1.	Multiply the value by the conversion factor of the source unit to get the number of bytes
# 2.	Divide the number of bytes by the conversion factor of the target unit to get the result
# •	Returns the final result as a float
# Use the conversion_factors dictionary for all conversions.
# Do not perform any user input or output in this function.
# Do not use if or elif statements to check unit names.
# This function must correctly handle:
# •	Conversion from a larger unit to a smaller unit (e.g. GB → MB)
# •	Conversion from a smaller unit to a larger unit (e.g. KiB → GiB)
def convert_storage(value, from_unit, to_unit):
    # calculate in bytes
    bytes_value = value * conversion_factors[from_unit]

    # from bytes convert it back up
    converted_value = bytes_value / conversion_factors[to_unit]

    return converted_value

print(convert_storage(48000, "MB", "GB"))
print(convert_storage(3.2, "TB", "GB"))
print(convert_storage(16, "GB", "MB"))
print(convert_storage(1, "KiB", "kB"))


# # Example: Convert 10 MB to MiB
# result = convert_storage(10, 'MB', 'MiB')
# print(f"10 MB is approximately {result:.4f} MiB")

# ________________________________________
# Task 4.4 – User Interaction [8 marks]
# Write the main program that:
# •	Repeatedly prompts the user to input:
# o	A numeric value
# o	A source unit
# o	A target unit
# •	Validates that:
# o	The numeric value is positive. 
# o	Both units are supported using the is_valid_unit() function
# •	Calls the convert_storage() function to perform the conversion
# •	Displays the result to 4 decimal places, e.g.:
# •	10 MB is approximately 9.5367 MiB
# •	Asks the user whether they want to convert another value
# o	If the user enters "yes", repeat the process
# o	If the user enters "no", end the program

def is_valid_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
while True:
    inputnum = float(input("Input a number for conversion: "))
    if inputnum > 0 :
        break
    else:
        print("Invalid number, must be a number more than 0")

while True:
    from_unit = input("What is the source unit? ")
    if is_valid_unit(from_unit):

        to_unit = input("What is the target unit? ")
        if is_valid_unit(to_unit):
            outputNum = convert_storage(inputnum, from_unit, to_unit)
            outputNum = round(outputNum, 4)
            print(f"{inputnum} {from_unit} is approximately {outputNum}{to_unit}.")
        else:
            print("Invalid target unit. Try again")
    else:
        print("Invalid source unit. Try again")

# ________________________________________
# Task 4.5 – Code Quality [4 marks]
# Ensure that your code:
# •	Uses meaningful and consistent variable and function names
# •	Is structured using appropriate function decomposition
# •	Includes inline comments that explain important parts of the logic

# ________________________________________

