
while True:
   
    while True:
        value = float(input("Enter a number to convert: "))

        if value > 0:
            print(f"{value} is valid")
            break
        else:
            print(f"{value} is not valid. Enter a positive number")

    while True:
        from_unit = input("Enter a unit to convert from: ")
        if is_valid_unit(from_unit):
            print(f"{from_unit} is valid.")
            to_unit = input("Enter a unit to convert: ")
            if is_valid_unit(to_unit):
                output_val = convert_storage(value, from_unit, to_unit)
                output_val = round(output_val, 4)

                print(f"{value} {from_unit} is {output_val} {to_unit}")
                break
            else:
                print(f"{to_unit} is not valid")

        else:
            print(f"{from_unit} is not valid. Try again")
    proceed = input("Do you want to continue(Y/N)? ")
    if proceed == "N":
        break