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

# read the value from a dictionary
val_yoshi = character_power['yoshi']
print(val_yoshi)

# read the value of donkey kong, waluigi

# make another dictionary of of 3 countries and their capital
# read the value of one of the countries

# add/ change to dictionary - exactly the same
character_power['shy guy'] = 45 ## Adding, if key does not exist, it will add
print(character_power)

character_power['shy guy'] = 88 ## CHANGE
print(character_power)

### add another country: capital 

# how to loop through a dictionary

# for key in character_power: # without .items()
#     print(key) ### prints the key from dictionary

#     print(character_power[key]) # pull the value from the key

for key,value in character_power.items():
    print(key)
    print(value)