#Task 5.1
def shift(char):
    if not char.isalpha(): #Ignores non letters
        return char
    if not char == char.lower(): #Ignores non lower case
        return char
    
    if char == "z": #z loops back to a
        return "a"
    else:
        new_char = chr(ord(char) + 1) #shift the alphabet to the next character
        return new_char

print(shift("z"))

#Task 5.2
def encrypt(message, positions):
    message_list = []
    prev_list = []
    for char in message:
        message_list.append(char)

    while positions != 0: #loop for number of positions shifted
        prev_list = message_list
        message_list = []
        for char in prev_list:
            char = shift(char) #Shift the character and store in a list
            message_list.append(char)
        positions -= 1
    return ''.join(message_list)
print(encrypt("aa5A!aaa", 1))

print("0".isdigit())