def valid_password(password):

    # flags to check if meet criteria
    lengthok = False
    letterok = False
    numberok = False

    # at least 8 char at most 12 char
    if len(password) >= 8 and len(password) <= 12:
        lengthok = True
    
    # loop through every single char
    for i in password:

        if i.isalpha():
            letterok = True
        elif i.isdigit():
            numberok = True

    if lengthok and letterok and numberok:
        return True
    else:
        return False

######### function to check digit
def gen_checkdigit(password):
    # convert all letters to ASCII
    weight_list = []

    # loop through every single character in password
    for i in password:
        if i.isalpha():
            weight_list.append(ord(i))
        elif i.isdigit():
            weight_list.append(0)
    
    total = 0
    # sum of all characters multiplied by weights
    for j in range(len(password)):
        pos = j + 1  # 1 based index
        currentweight = weight_list[j] # zero based

        sumweight = pos * currentweight
        total = total + sumweight
    
    #calculate checkdigit 
    remainder = total % len(password)

    return remainder

# Task 4.3
password = input("Please key in your password: ")

if valid_password(password):
    checkdigit = gen_checkdigit(password)
    print(f"The check digit for {password} is {checkdigit}.")
else:
    print(f"{password} is an invalid password.")

print(valid_password(password))

print(gen_checkdigit(password)) #iLovecom3

print(chr(65)) # rerturn character based on number
print(ord('A')) # returns number based on character

# print(help(chr))