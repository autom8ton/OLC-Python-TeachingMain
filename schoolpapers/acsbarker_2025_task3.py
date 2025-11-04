character_power = {
    'mario':50,
    'luigi':45,
    'bowser':80,
    'peach':40,
    'yoshi':55,
    'toad':30,
    'wario':70,
    'daisy':42,
    'waluigi':65,
    'donkey kong':75,
}

character = input("Please enter the character name: ").lower()
# seach character in dictionary
if character in character_power:
    power = character_power[character]
    print(f"The Power of {character} is {power}.")
else:
    print(f"{character} not found in database.")

add = input("Would you like to add any of the entries (Y or N): ")

# Task 3.2
# check if add is equal to Y
if add.upper() == "Y":

    while True:
        # ask for an input for new character, to lower case
        new = input("Enter a new character: ")

        # check if exist, if exist then reprompt >>>> while Loop
        if new in character_power:
            print(f"{new} exists, pls add another.")
        else:
            break
    
    # ask for a number between 1 to 100
    # keep asking until valid number from 1 to 100
    while True:
        power_num = int(input("Enter a number from 1 to 100: "))
        if power_num < 1 or power_num > 100:
            print("You must enter a number from 1 to 100.")
        else:
            break

    # add to dictionary
    character_power[new] = power_num

    # output dictionary
    print(character_power)