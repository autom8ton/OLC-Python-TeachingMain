

####################################################################################
def Power_NRICCheck(usernric):
    
    checksum_table_ST = { 10 : "A", 9 : "B", 8 : "C", 7 : "D", 6 : "E", 5 : "F", 
                           4 : "G", 3 : "H", 2 : "I", 1 : "Z", 0 : "J"}
    
    checksum_table_FG = { 10 : "K", 9 : "L",8 : "M", 7 : "N", 6 : "P", 5 : "Q",
                          4 : "R", 3 : "T", 2 : "U", 1 : "W", 0 : "X"}
    
    weights = [2,7,6,5,4,3,2]

    usernric = usernric.upper()

    # check for length
    if len(usernric) != 9:
        print("NRIC must be 9 digits. ")
        return False

    # check that first character is valid 
    elif not usernric[0].isalpha() or usernric[0] not in ['S','T', 'F', 'G']:
        print("A valid NRIC must start with S, T, F, G. ")
        return False

    # check that last character is an alphabet
    elif not usernric[-1].isalpha():
        print("NRIC must end with a alphabet. ")
        return False

    # check that in between are 7 numbers
    elif not usernric[1:8].isdigit():
        print("NRIC must contain 7 digits.")
        return False

    else:
        # preliminary check done and start validation for checksum
        icdigits = usernric[1:8]
        total = 0

        # calculate the weights of each number and sum up
        for i in range(len(icdigits)):
            total = total + (int(icdigits[i]) * weights[i])

        # if prefix is T or G add 4
        if usernric[0] in ['T','G']:
            total = total + 4            
        
        remainder = total % 11 # calculate the remainder

        # read different dictionary based on first character
        if usernric[0] in ['S','T']:
            expected = checksum_table_ST[remainder]
        elif usernric[0] in ['F','G']:
            expected = checksum_table_FG[remainder]

        # checking last character matches value calculated from table
        if expected == usernric[-1]:
            print(f"Last character is valid. Checksum is correct.")
            return True
        else:
            print(f"Last character is invalid. Checksum is not correct.")
            return False


# Call the function                
while True:
    nric = input("Enter an NRIC to check validity: ")
    if Power_NRICCheck(nric):
        print(f"{nric} is a valid NRIC")
    else:
        print(f"{nric} is not a valid NRIC")
    
    proceed = input("Press 'enter' to continue, or n to stop:")
    if proceed.lower() == "n":
        print("Exiting...")
        break






############################################################