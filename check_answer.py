conversion_factors = {
    "B": 1,
    "kB": 1000,
    "KiB": 1024,
    "MB": 1000**2,
    "MiB": 1024**2,
    "GB" : 1000**3,
    "GiB" : 1024**3,
    "TB" : 1000**4,
    "TiB": 1024**4,  
    "PB" : 1000**5,
    "PiB" : 1024**5
    }
def is_valid_unit(unit): #MB
    if unit in conversion_factors:
        return True
    else:
        return False
print(is_valid_unit("kB"))

# ________________________________________
# Task 4.3 – Conversion Function [7 marks]
# Write a function named convert_storage(value, from_unit, to_unit) that:
# • Takes in three parameters:
# o value (a numeric value to convert)
# o from_unit (the current unit)
# o to_unit (the target unit)
# • Converts the value using the following steps:
# 1.    Multiply the value by the conversion factor of the source unit to get the number of bytes
# 2.    Divide the number of bytes by the conversion factor of the target unit to get the result
# • Returns the final result as a float
# Use the conversion_factors dictionary for all conversions.
# Do not perform any user input or output in this function.
# Do not use if or elif statements to check unit names.
# This function must correctly handle:
# • Conversion from a larger unit to a smaller unit (e.g. GB → MB)
# • Conversion from a smaller unit to a larger unit (e.g. KiB → GiB)
# def convert_storage(value, from_unit, to_unit):

# testing only
# value = 5000
# from_unit = "TB"
# to_unit = "PB"

def convert_storage(value, from_unit, to_unit):
    conversion_value = conversion_factors[from_unit] * value
    # print(conversion_value)
    output_unit = conversion_value / conversion_factors[to_unit]
    return output_unit
# testing
print(convert_storage(1000, "TB","PB"))

# # ________________________________________
# # Task 4.4 – User Interaction [8 marks]
# # Write the main program that:
# # •   Repeatedly prompts the user to input:
# # o   A numeric value
# # o   A source unit
# # o   A target unit
# # •   Validates that:
# # o   The numeric value is positive.
# # o   Both units are supported using the is_valid_unit() function
# # •   Calls the convert_storage() function to perform the conversion
# # •   Displays the result to 4 decimal places, e.g.:
# # •   10 MB is approximately 9.5367 MiB
# # •   Asks the user whether they want to convert another value
# # o   If the user enters "yes", repeat the process
# # o   If the user enters "no", end the program

def convert_storage(value, from_unit, to_unit):
    conversion_value = conversion_factors[from_unit] * value
    output_unit = conversion_value / conversion_factors[to_unit]
    return output_unit
#testing
print(convert_storage(1000, "MB","MiB"))
while True:
    valuenum = float(input("Enter a number to covert: "))
    # validate
    if valuenum > 0:
        print(f"{validnum} is valid")
        break
    else:
        print(f"{valuenum} is not valid. You must enter a positive number.")
    # check for valid unit
    while True:
        from_unit = input("Enter unit):
            print(f"{from_unit} is valid. ")
            if is_valid_unit(to_unit):
            output_val = convert_storage(value, from_unit, to_unit)
            output_val = round(output_val, 4)
            #testing
            # 1000 B = 1KB
            print(f"{valuenum} {from_unit} is (output_val) (to_unit)")
        else:
            print(f"{to_unit} is not valid. Try again")
    else:
        print(f"{to_unit} is not valid. Try again")