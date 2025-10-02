conversion_factors = {
    "B": 1,
    "kB": 1000,
    "MB": 1000**2,
    "KiB": 1024,
    "MiB": 1024**2
}

conversion_factors["GB"] = 1000**3
conversion_factors["TB"] = 1000**4
conversion_factors["PB"] = 1000**5
conversion_factors["GiB"] = 1024**3
conversion_factors["TiB"] = 1024**4
conversion_factors["PiB"] = 1024**5
print(conversion_factors)
#4.2
def list_units():
    count = 1 
    for key in conversion_factors:
        print(f"{count}. {key}")
        count += 1
list_units() #need to call define function
#task 4.3
def is_valid_unit(unit):
    if unit in conversion_factors:
        return True
    else:
        return False
#task 4.4
def convert_storage(value, from_unit, to_unit):
    value = int(value)
    bytes = value * conversion_factors[from_unit]
    target = bytes / conversion_factors[to_units]
    return target
#task 4.5
print(list_units)
while True:
    number = int(input("Please input a number value"))
    if number > 0:
        continue
    else:
        break
while True:
    source_unit = input("Please input a source unit")
    if is_valid_unit(source_unit):
        continue
    else:
        break
while True:
    target_unit = input("Please input a target unit")
    if is_valid_unit(target_unit):
        continue
    else:
        break
return convert_storage
