# Task 4 - Development of a Unit Converter (25 marks)
# You are developing a Python program to convert 
# digital storage values between SI units (e.g. MB, GB) 
# and binary units (e.g. MiB, GiB).

# The following global dictionary is provided to you. 
# Do not amend or remove this code.
conversion_factors = {
    "B": 1,
    "kB": 1000,
    "MB": 1000**2,
    "KiB": 1024,
    "MiB": 1024**2
}


# ________________________________________
# Code Quality [4 marks]
# Your program must:
# •	Use meaningful and consistent variable and function names.
# •	Be structured using appropriate function decomposition.
# •	Include inline comments that explain important parts of the logic.
# ________________________________________
# Task 4.1 - Complete the Dictionary [2 marks]
# Extend the conversion_factors dictionary to include the following units:
# •	SI units: "GB", "TB", "PB" (use powers of 1000)
# •	Binary units: "GiB", "TiB", "PiB" (use powers of 1024)








# ________________________________________
# Task 4.2 - Display Available Units [3 marks]
# Write a function named list_units() that:
# •	Loops through the keys of the conversion_factors dictionary.
# •	Prints out all the unit names in a numbered list (one per line).
# •	Allows the user to see which units are supported before making a choice.
# Expected output:
# Available Units:
# 1: B
# 2: kB
# 3: MB
# 4: KiB
# 5: MiB
# 6: GB
# 7: TB
# 8: PB
# 9: GiB
# 10: TiB
# 11: PiB








# ________________________________________
# Task 4.3 - Validation Function [2 marks]
# Write a function named is_valid_unit(unit) that:
# •	Takes in a string unit.
# •	Returns True if the unit is a valid key in conversion_factors.
# •	Returns False otherwise.
# This function will be used to check whether the user has entered a supported unit.








# ________________________________________
# Task 4.4 - Conversion Function [4 marks]
# Write a function named convert_storage(value, from_unit, to_unit) that:
# 1.	Multiplies the value by the conversion factor of 
#       the source unit to get the number of bytes.
# 2.	Divides the number of bytes by the conversion factor of the target unit.
# 3.	Returns the result as a float.

# Example: Convert 2 GB into MB.
# •	Step 1: 2 x conversion_factors["GB"] = 
#           2 x 1000^3 = 2,000,000,000 bytes
# •	Step 2: 2,000,000,000 ÷ conversion_factors["MB"] = 
#           2,000,000,000 ÷ 1000^2 = 2000.0
# •	Final result: 2 GB = 2000.0 MB







# ________________________________________
# Task 4.5 - User Interaction [10 marks]
# Write the main program that:
# 1.	Repeatedly prompts the user to input:
# o	A numeric value
# o	A source unit
# o	A target unit
# 2.	Validates that:
# o	The numeric value is a valid positive number.
# o	Both units are supported (using the is_valid_unit() function).
# 3.	Calls the convert_storage() function to perform the conversion.
# 4.	Displays the result to 4 decimal places, e.g.:
# 10 MB is approximately 9.5367 MiB
# 5.	Asks the user whether they want to convert another value.
# o	If the user enters "no", end the program with a farewell message.
# ________________________________________




























###########################################################
# ANSWER BELOW ############################################
###########################################################

# Task 4 - Development of a Unit Converter (25 marks)
# You are developing a Python program to convert 
# digital storage values between SI units (e.g. MB, GB) 
# and binary units (e.g. MiB, GiB).

# The following global dictionary is provided to you. 
# Do not amend or remove this code.
conversion_factors = {
    "B": 1,
    "kB": 1000,
    "MB": 1000**2,
    "KiB": 1024,
    "MiB": 1024**2
}


# ________________________________________
# Code Quality [4 marks]
# Your program must:
# •	Use meaningful and consistent variable and function names.
# •	Be structured using appropriate function decomposition.
# •	Include inline comments that explain important parts of the logic.


# ________________________________________
# Task 4.1 - Complete the Dictionary [2 marks]
# Extend the conversion_factors dictionary to include the following units:
# •	SI units: "GB", "TB", "PB" (use powers of 1000)
# •	Binary units: "GiB", "TiB", "PiB" (use powers of 1024)

conversion_factors['GB'] = 1000**3
conversion_factors['TB'] = 1000**4
conversion_factors['PB'] = 1000**5

conversion_factors['GiB'] = 1024**3
conversion_factors['TiB'] = 1024**4
conversion_factors['PiB'] = 1024**5





# ________________________________________
# Task 4.2 - Display Available Units [3 marks]
# Write a function named list_units() that:
# •	Loops through the keys of the conversion_factors dictionary.
# •	Prints out all the unit names in a numbered list (one per line).
# •	Allows the user to see which units are supported before making a choice.
# Expected output:
# Available Units:
# 1: B
# 2: kB
# 3: MB
# 4: KiB
# 5: MiB
# 6: GB
# 7: TB
# 8: PB
# 9: GiB
# 10: TiB
# 11: PiB

def list_units():

    count = 1 # usedd for showing counts
    print("Available Units:")
    for unit in conversion_factors:
        print(f"{count}: {unit}")
        count += 1





# ________________________________________
# Task 4.3 - Validation Function [2 marks]
# Write a function named is_valid_unit(unit) that:
# •	Takes in a string unit.
# •	Returns True if the unit is a valid key in conversion_factors.
# •	Returns False otherwise.
# This function will be used to check whether the user has entered a supported unit.


def is_valid_unit(unit):
    # check if unit is inside the conversion_factors dictionary
    if unit in conversion_factors:
        return True
    else:
        return False





# ________________________________________
# Task 4.4 - Conversion Function [4 marks]
# Write a function named convert_storage(value, from_unit, to_unit) that:
# 1.	Multiplies the value by the conversion factor of 
#       the source unit to get the number of bytes.
# 2.	Divides the number of bytes by the conversion factor of the target unit.
# 3.	Returns the result as a float.

# Example: Convert 2 GB into MB.
# •	Step 1: 2 x conversion_factors["GB"] = 
#           2 x 1000^3 = 2,000,000,000 bytes
# •	Step 2: 2,000,000,000 ÷ conversion_factors["MB"] = 
#           2,000,000,000 ÷ 1000^2 = 2000.0
# •	Final result: 2 GB = 2000.0 MB


def convert_storage(value, from_unit, to_unit):
    value = int(value) # convert to integer.

    # get the from unit factor for conversion
    from_factor = conversion_factors[from_unit]

    # get the to unit factor for conversion
    to_factor = conversion_factors[to_unit]

    value = value * from_factor

    value = value / to_factor

    return value




# ________________________________________
# Task 4.5 - User Interaction [10 marks]
# Write the main program that:
# 1.	Repeatedly prompts the user to input:
# o	A numeric value
# o	A source unit
# o	A target unit
# 2.	Validates that:
# o	The numeric value is a valid positive number.
# o	Both units are supported (using the is_valid_unit() function).
# 3.	Calls the convert_storage() function to perform the conversion.
# 4.	Displays the result to 4 decimal places, e.g.:
# 10 MB is approximately 9.5367 MiB
# 5.	Asks the user whether they want to convert another value.
# o	If the user enters "no", end the program with a farewell message.
# ________________________________________

while True: 
    list_units()
    # The numeric value is valid positive number.

    # validate for a valid positive digit
    while True:
        number = input("Enter a number to convert: ")
        if not number.isdigit():
            print("You must enter a valid number.")
        elif int(number) < 1:
            print("You must enter a valid positive number.")
        else:
            break

    # validate for a proper unit from the dictionary
    while True:
        from_unit = input("Enter the from unit to convert from: ")
        if is_valid_unit(from_unit):
            break
        else:
            print(f"{from_unit} is not a valid unit. ")

    # validate for a proper unit from the dictionary
    while True:
        to_unit = input("Enter the to unit to convert to: ")
        if is_valid_unit(to_unit):
            break
        else:
            print(f"{to_unit} is not a valid unit. ")

    # call the function to convert and output.
    converted = convert_storage(number, from_unit, to_unit)
    print(f"{number} {from_unit} is {round(converted,4)} {to_unit}")

    proceed = input("Do you want to continue? Type 'no' to end the program or any key to continue: ").lower()
    if proceed == "no":
        print("Exiting program... Bye.")
        break

