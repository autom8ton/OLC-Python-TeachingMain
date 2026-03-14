# Task 2
# In Singapore, electronic road pricing (ERP) is implemented
# on various expressways to regulate traffic.
#
# Lately there has been a change in the ERP rates at 5 gantries across some expressways.

# The following program calculates the change in rates of these 5 gantries.

# for i in range(5):
#     expressway = input("Enter name of gantry:")
#     old = float(input("Enter old rate:"))
#     new = float(input("Enter new rate:"))
#     change = new - old
#     print("Change is",change)


###########################################################
# 6. Edit the program so that:
# a)    It works for any number of gantries.
#       The program must display a suitable input message. [1]
###########################################################
# Copy + Paste & Write your code here
# num_gantries = int(input("How many gantries? "))

# for i in range(num_gantries):
#     expressway = input("Enter name of gantry:")
#     old = float(input("Enter old rate:"))
#     new = float(input("Enter new rate:"))
#     change = new - old
#     print("Change is",change)


###########################################################
# b)    The name of gantry is accepted if it is made up of only
#       letters and is of a maximum length of 20.
#       A suitable error message must be displayed and the program
#       must loop until the name of the gantry is an input of a maximum of 20 letters. [4]
###########################################################
# Copy + Paste & Write your code here

# check for length ? >> len()
# check for letters >> .isalpha()
# while True validation

# num_gantries = int(input("How many gantries? "))

# for i in range(num_gantries):
    
#     while True:
#         expressway = input("Enter name of gantry:")

#         if len(expressway) > 20:
#             print("Expressway name cannot be more than 20.")
#         elif expressway.isalpha() == False:
#             print("Expressway name can only contain letters.")
#         else:
#             break
#     old = float(input("Enter old rate:"))
#     new = float(input("Enter new rate:"))
#     change = new - old
#     print("Change is",change)



###########################################################
# c)    The name of each gantry for which the ERP rate has
#       been increased is stored in a list and then displayed. [4]
###########################################################
# Copy + Paste & Write your code here

# gantry_increase = [] # empty list for gantries that increase price
# num_gantries = int(input("How many gantries? "))

# for i in range(num_gantries):
    
#     while True:
#         expressway = input("Enter name of gantry:")

#         if len(expressway) > 20:
#             print("Expressway name cannot be more than 20.")
#         elif expressway.isalpha() == False:
#             print("Expressway name can only contain letters.")
#         else:
#             break
#     old = float(input("Enter old rate:"))
#     new = float(input("Enter new rate:"))
#     change = new - old
#     print("Change is",change)

#     # check if price increased
#     if change > 0:
#         gantry_increase.append(expressway)

# for g in gantry_increase:
#     print(f"{g} increased in price.")
# # print(gantry_increase)


###########################################################
# d)    The total number of gantries which saw an increase
#       in the ERP rate is displayed. [1]
###########################################################
# Copy + Paste & Write your code here


gantry_increase = [] # empty list for gantries that increase price
num_gantries = int(input("How many gantries? "))

for i in range(num_gantries):
    
    while True:
        expressway = input("Enter name of gantry:")

        if len(expressway) > 20:
            print("Expressway name cannot be more than 20.")
        elif expressway.isalpha() == False:
            print("Expressway name can only contain letters.")
        else:
            break
    old = float(input("Enter old rate:"))
    new = float(input("Enter new rate:"))
    change = new - old
    print("Change is",change)

    # check if price increased
    if change > 0:
        gantry_increase.append(expressway)

for g in gantry_increase:
    print(f"{g} increased in price.")

print(f"{len(gantry_increase)} gantries increased in price. ")
# print(gantry_increase)