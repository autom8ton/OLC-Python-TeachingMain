
###################################################
# Part 1: Learning Exercises


# Exercise 1: Finding the Maximum Without Built-In Functions
# Write a program to find the largest number in a list without 
# using max().

list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
         5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
         1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
         756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
         2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880]
bignum = max(list1)
print(bignum)

smallnum = min(list1)
print(smallnum)




#------------------------------------------------------------
# Exercise 2: Calculating the Sum Without Built-In Functions
# Write a program to calculate the sum of numbers in a list 
# without using sum().
# find the position of the biggest and slowest
maxnum = list1[0]
minnum = list1[0]

bigpos = 0
smallpos = 0
count = 0

for i in list1:
    if i >maxnum:
        maxnum = i
        bigpos = count

    if i <minnum:
        minnum = i
        smallpos = count

    count = count+ 1

print(f"the biggest is {maxnum} and it is at {bigpos} ")
print(f"the smallest is {minnum} and it is at {smallpos} ")



# The school's swimming coach has recorded the 50m freestyle 
# swim times (in seconds) for 15 swimmers. 
# Using the list provided, find and display the fastest and slowest swim times, 
# along with their swim lane position in the list.

# Assume that the first item in the list is swim lane position 1.
#####################################################
swim_times = [32.5, 30.1, 33.8, 29.6, 31.2, 34.0, 28.9, 
              30.4, 38.1, 27.5, 35.6, 31.8, 29.2, 33.0, 30.5]
# # Answer for here
fasttime = swim_times[0]
slowtime = swim_times[0]


fastlane = 0
slowlane = 0
count = 0

for i in swim_times:
    if i <fasttime:
        fasttime = i
        fastlane = count

    if i >slowtime:
        slowtime = i
        slowlane = count

    count =count +1        

print(f"the fastest time is {fasttime} and it is at {fastlane} ")
print(f"the slowest time is {slowtime} and it is at {slowlane} ")
   


#------------------------------------------------------------
# Exercise 3: Calculating the Average of a List
# Write a program to calculate the average of numbers in a list.
# Example: Input = [4, 8, 12, 16, 20], Output = 12.




#------------------------------------------------------------
# Exercise 4: Validating List Length
# Write a program to ensure a list contains at least 5 elements.
# Prompt the user to add more values until the condition is met.




#------------------------------------------------------------
# Exercise 5: Validating Range of Input
# Write a program to ensure a user enters a number between 1 and 
# 100. Repeat until a valid input is given.




#------------------------------------------------------------
# Exercise 6: Validating Presence in a List
# Write a program to ensure a specific value exists in a list.
# Prompt the user until they enter a value present in the list.




#------------------------------------------------------------
# Exercise 7: Validating Non-Empty Input
# Write a program to ensure the user enters a non-empty value.
# Prompt the user until they enter a valid input.


#------------------------------------------------------------
