# Task 1

# The task is to edit program code that allows the user to enter and 
# edit the names and heights of team members.

# The following program allows the user to enter the names of the 
# 5 members of a team and stores them in a list. 

# The list is to be sorted and processed in each sub-task.
# This program allows the user to enter five names and
# stores the names in a list for further processing
# variables
# names = []
# # Enter name
# for i in range(5):
#     name = input('Please enter the name: ')
#     names.append(name)
# # Processing
# print (names)


# Edit the program so that it:
# (a) creates a new list to store the collection of height data 
# for the corresponding names input.
# (b) allows the user to enter height data.
# (c) identifies the tallest and shortest height (not the person) 
#     among the entered data.
# Save your program.
# [4]
#--------------------------------------------



#--------------------------------------------
# Task 1.2
# Copy and paste your program from sub-task 1.1.
# Edit the program to perform presence check and type check data 
# validation on the input for height data.
# Save your program.
# [3]
#--------------------------------------------




#--------------------------------------------
# Task 1.3
# Copy and paste your program from sub-task 1.2
# Edit the program so that it prints out:
# (a) the tallest and the shortest person from the entered data.
# (b) the average of the heights of the entered data.
# (c) the range of the heights data.
# Save your JupyterLab notebook for Task 1.
# [4]
#--------------------------------------------





##########################################
# ANSWER BELOW
###########################################

# Task 1

# The task is to edit program code that allows the user to enter and 
# edit the names and heights of team members.

# The following program allows the user to enter the names of the 
# 5 members of a team and stores them in a list. 

# The list is to be sorted and processed in each sub-task.
# This program allows the user to enter five names and
# stores the names in a list for further processing
# variables
# names = []
# # Enter name
# for i in range(5):
#     name = input('Please enter the name: ')
#     names.append(name)
# # Processing
# print (names)


# Edit the program so that it:
# (a) creates a new list to store the collection of height data 
# for the corresponding names input.
# (b) allows the user to enter height data.
# (c) identifies the tallest and shortest height (not the person) 
#     among the entered data.
# Save your program.
# [4]
#--------------------------------------------
names = []
heights = []
# Enter name
for i in range(5):
    name = input('Please enter the name: ')
    height = input(f"Please enter the height for {name}")
    names.append(name)
    heights.append(height)
# Processing
print (names)
maxheight = max(heights)
minheight = min(heights)
print(f"The tallest height is {maxheight}")
print(f"The shortest height is {minheight}")



#--------------------------------------------
# Task 1.2
# Copy and paste your program from sub-task 1.1.
# Edit the program to perform presence check and type check data 
# validation on the input for height data.
# Save your program.
# [3]
#--------------------------------------------

names = []
heights = []
# Enter name
for i in range(5):
    name = input('Please enter the name: ')

    # start 1.2
    while True:
        height = input(f"Please enter the height for {name}: ")
        if height == "":
            print("You must enter a value for height. ")
        elif not height.isdigit():
            print("Height must be a number.")
        else:
            break

    names.append(name)
    heights.append(height)
# Processing
print (names)
maxheight = max(heights)
minheight = min(heights)
print(f"The tallest height is {maxheight}")
print(f"The shortest height is {minheight}")





#--------------------------------------------
# Task 1.3
# Copy and paste your program from sub-task 1.2
# Edit the program so that it prints out:
# (a) the tallest and the shortest person from the entered data.
# (b) the average of the heights of the entered data.
# (c) the range of the heights data.
# Save your JupyterLab notebook for Task 1.
# [4]
#--------------------------------------------


names = []
heights = []
# Enter name
for i in range(5):
    name = input('Please enter the name: ')

    # start 1.2
    while True:
        height = input(f"Please enter the height for {name}: ")
        if height == "":
            print("You must enter a value for height. ")
        elif not height.isdigit():
            print("Height must be a number.")
        else:
            break

    names.append(name)
    heights.append(height)
# Processing
print (names)
maxheight = max(heights)
minheight = min(heights)
print(f"The tallest height is {maxheight}")
print(f"The shortest height is {minheight}")

# Task 1.3
nummax = heights.index(maxheight)
nummin = heights.index(minheight)

tallest_name = names[nummax]
shortest_name = names[nummin]
print(f"The tallest person is {tallest_name}")
print(f"The shortest person is {shortest_name}")

average = sum(heights) / len(heights)
print(f"The average height is {average}")

print(f"There are {len(heights)} height recorded.")
print(f"The range is from {minheight} to {maxheight}")