# Task 3
# The task is to edit program code so that countries and their capital 
# cities can be added to or removed from a dictionary.

# The following program has a dictionary that contains countries 
# and their capital cities. The program allows the user to:

# • input a country
# • input whether they want to remove a country and 
#    its capital city from the dictionary
# • input whether they want to add a country and its 
#    capital city to the dictionary.


capital_cities = {
    'singapore':'Singapore',
    'japan':'Tokyo', 'australia':'Canberra',
    'england':'London',
    'france':'Paris',
    'germany':'Berlin'
}

country = input("Please enter the name of a country: ")
remove = input("Would you like to remove any of the entries? (Y or N): ")
add = input("Would you like to add a new entry? (Y or N): ")


# For all sub-tasks, you can assume that all user input is valid.
#  All countries input to be searched or removed are found in the dictionary.

# Task 3.1
# Edit the program so that it:
# • converts the input for country to lower case
# • searches the dictionary for the country input and outputs the capital city of that country.
# Save your program.    [3]

# Task 3.2
# Copy and paste your program from sub-task 3.1.
# Edit the program so that if the user enters the value ‘Y’ for remove, the program:
# • allows the user to input a country they want to remove from the dictionary
# • converts the country input to lower case
# • removes the country from the dictionary that is input by the user.

# Save your program.   [3]

# Task 3.3
# Copy and paste your program from sub-task 3.2 .
# Edit the program so that if the user enters the value ‘Y’ for add, the program:
# • allows the user to input a country they want to add to the diction nary
# • allows the user to input the capital city for the country they want to add
# • adds the country and its capital city to the dictionary in the format country:capital
# • outputs the dictionary at the end of the program.

# [4]