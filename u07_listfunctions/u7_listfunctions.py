# how to define a list - planets

# define a list
planets = ["mercury", "venus","earth", "mars", "jupiter","saturn", "uranus", "neptune"]

# retrieve the value from a list
print(planets[2]) # earth

# replace value in a list
planets[3] = "Denzelland"
print(planets) # to prove

# remove item from list # uranus
del planets[6]
print(planets) # to prove

# remove item using name
planets.remove("mercury")
print(planets) # to prove

# add to a list
planets.append("jiajieLand")
print(planets) # to prove

# how many items there are in the list
count = len(planets)
print(count)

# how to loop through a list
for i in planets:
    print(f"Someday I would like to visit {i}")




# write a program to ask for student's first name

# Assume you have 5 student

# add each name to the list

# loop through the list and make a greeting
# e.g. 
# Hello Deborah
# Hello Marcus
#.....


# Exercise 9: Summing Numbers in a List
# Write a program to calculate the sum of numbers in a list.
list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
         5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
         1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
         756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
         2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
         6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
         6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
         4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]

#### how to find the maximum number in the list without using max()
maxnum = list1[0]

for i in list1:
    if i > maxnum: # if the current num is bigger than my previous biggest
        maxnum = i # set biggest to the current num
        
print(maxnum)



# total sum of all the numbers
# total = sum(list1)

total = 0
for i in list1:
    total = total + i
print(total)

average = sum(list1) / len(list1)

maxnum = max(list1)

minnum = min(list1)




























# planets = ["mercury","venus","earth","mars","saturn"]

# # retrieve the value from the list
# # print(planets[3])

# # how to add items to the list .append(), .insert()
# planets.append("jupiter")
# planets.insert(0,"keijiland")

# # print(planets) # to prove

# # remove .remove(), del , pop()
# planets.remove("mars") # if you know the value to delete

# del(planets[0]) # delete the first item

# planets.pop() # remove the last item

# # print(planets)


# # change value of a list
# planets[3] = "elonmuskland"
# # print(planets)


# # print("A" in "planets")
# # isplanet = input("ENter a planet name: ")

# # if isplanet in planets:
# #     print(f"{isplanet} is a planet in the solar system.")
# # else:
# #     print(f"{isplanet} is not a planet in the solar system.")

# # for p in planets: # using list directly
# #     print(f"Someday i want to visit {p}")








# ###################################################
# # Part 1: Learning Exercises

# # Exercise 1: Accessing List Elements by Index
# # Write a program to access and print the first, second, and last 
# # elements of a list using indexing.
# fruits = ["apple", "banana", "cherry", "date","grape"]

# # print(fruits[0])
# # print(fruits[1])
# # print(fruits[-1]) # -1 is last from the back



# #------------------------------------------------------------
# # Exercise 2: Adding Elements to a List
# # Write a program to add an element to the end of a list using 
# # append(), and add another element at a specific index using 
# # insert().
# colors = ["red", "green", "blue"]

# colors.append("orange")
# colors.insert(2, "black")
# # print(colors)




# #------------------------------------------------------------
# # Exercise 3: Using del() to Remove an Element by Index
# # Write a program to delete an element at a specific index.
# # Example: Remove the second color.
# colors = ["red", "green", "blue", "yellow"]




# #------------------------------------------------------------
# # Exercise 4: Using remove() to Remove an Element by Value
# # Write a program to remove a specific element by its value.
# # Example: Remove "green" from the list.
# colors = ["red", "green", "blue", "yellow"]




# #------------------------------------------------------------
# # Exercise 5: Using pop() to Remove and Retrieve an Element
# # Write a program to remove the last element of a list using pop().
# # Example: Remove and print the last color.
# colors = ["red", "green", "blue", "yellow"]



# #------------------------------------------------------------
# # Exercise 6: Modifying Elements in a List
# # Write a program to change the second element in a list to "pink."
# colors = ["red", "green", "blue"]



# #------------------------------------------------------------
# # Exercise 7: Membership Check
# # Write a program to check if "blue" is in the list.
# colors = ["red", "green", "blue"]



# #------------------------------------------------------------
# # Exercise 8: Iterating Through a List
# # Write a program to print each fruit in a list using a for loop.
# fruits = ["apple", "banana", "cherry", "date"]



# #------------------------------------------------------------


# ###########################################################
# # Part 2. IN-CLASS Practice Exercises

# # Exercise 9: Summing Numbers in a List
# # Write a program to calculate the sum of numbers in a list.
# list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
#          5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
#          1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
#          756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
#          2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
#          6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
#          6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
#          4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
#          5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
#          4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]

# # thesum = sum(list1)
# # print(thesum)

# thesum = 0
# for i in list1:
#     thesum = thesum + i

# # print(thesum)


# #------------------------------------------------------------
# # Exercise 10: Finding the Maximum and Minimum
# # Write a program to find the largest and smallest numbers in 
# # a list using max() and min().
# list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
#          5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
#          1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
#          756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
#          2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
#          6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
#          6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
#          4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
#          5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
#          4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]

# # maxnum = max(list1)
# # minnum = min(list1)

# # print(maxnum)
# # print(minnum)

# # maxnum = list1[0]
# # for i in list1:
# #     if i > maxnum:
# #         maxnum = i
# # print(maxnum)


# #------------------------------------------------------------
# # Exercise 11: Iterating Through a List with Indices
# # Write a program to print each element in a list with its index.
# fruits = ["apple", "banana", "cherry"]

# # for i in range(len(fruits)):
# #     print(fruits[i])






# #------------------------------------------------------------
# # Exercise 12: Reversing a List
# # Write a program to reverse the order of elements in a list.
# cities = ["New York", "London", "Paris", "Tokyo"]

# # cities.reverse() #### reverse the original list

# # print(cities)

# # cities2 = []
# # for c in cities:
# #     cities2.insert(0, c)



# #------------------------------------------------------------
# # Exercise 13: Sorting a List
# # Write a program to sort a list of numbers in ascending order.
# list1 = [2944,4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
#          5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
#          4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]

# list1 = sorted(list1, reverse = True)

# # print(list1)


# #------------------------------------------------------------
# # Exercise 14: Removing Specific Index with del()
# # Write a program to remove the third element in a list using del.
# # Then print the updated list.
# list1 = [2944,4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
#          5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
#          4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]

# del(list1[2])
# # print(list1)



# #------------------------------------------------------------










# # Task 4: List Reverser

# # Ask the user to enter a list of 5 numbers (one by one)
# # Stores them in a list
# # Reverses the list manually (without using reverse() or slice)
# # Prints the reversed list

# # numbers = [4,6,8,9,10]

# # # reverse1 = numbers[::-1] # slicing (direct way to reverse)
# # # print(reverse1)

# # # reverse2 = numbers.reverse()
# # # print(numbers)

# # reverse_list = []

# # for num in numbers:
# #     reverse_list.insert(0, num)

# # print(reverse_list)

# # # palindrome 

# # # LEVEL 
# # # MADAM
# # # RACECAR

# # # word 



# # #### LIST ALGORITHM

# # # REVERSAL OF LIST


# # # MAX IN A LIST
# # list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
# #          5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
# #          1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
# #          756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
# #          2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
# #          6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
# #          6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
# #          4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
# #          5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
# #          4183, 2463, 9562, 8137, 5101, 397, 6966, 99927, 7473, 4105]

# # maxnum = max(list1)
# # print(maxnum)

# # minnum = min(list1)
# # print(minnum)



# # SUM OF A LIST

# # AVERAGE OF A LIST



# # What is my Chinese Zodiac sign?
# # In not more than 10 lines of code, write a program 
# # to calculate the Chinese Zodiac sign based on a 
# # user's year of birth. (hint: it can be done in 5 lines)

# # The most common method depends on Chinese New Year, 
# # which is considered as the division of two animal years. 
# # When a lunar year comes to an end, the animal will shift to next one. 
# # Chinese people’s animal signs are marked by this method.

# # How to Calculate Your Chinese zodiac sign mathematically?
# # Divide your year of birth by 12 and get the remainder. 
# # Each remainder corresponds to an animal sign below.

# # 0: Monkey 1: Rooster 2: Dog 3: Pig 4: Rat 5: Ox 6: Tiger 
# # 7: Rabbit 8: Dragon 9: Snake 10: Horse 11: Goat

# # Sample Output
# # Enter your birth year: 1977
# # Your Chinese zodiac sign is: Snake
# '''

# zodiac_animals = ['monkey','rooster','dog','pig','rat','ox',
#                   'tiger''rabbit','dragon','snake','horse','goat']

# birth_year = int(input("Enter your birth year: "))

# remainder = birth_year % 12

# zodiac_sign = zodiac_animals[remainder-1]

# print(f"Your Chinese zodiac sign is: {zodiac_sign}")

# '''

# # Ask how many times to roll a six-sided dice
# # update the number rolled in a list

# # repeat this process 100 times
# # print out the number of times each number was rolled
# # Enter the number of times to roll the die:10
# # Number 1 appears 0 times.
# # Number 2 appears 2 times.
# # Number 3 appears 2 times.
# # Number 4 appears 2 times.
# # Number 5 appears 0 times.
# # Number 6 appears 4 times.


# # # assume we roll a six sided dice 100 times
# # import random

# # rolls_per_session = int(input("How many times should I roll the six-sided dice each session? "))

# # # possible dice numbers is 1,2,3,4,5,6

# # roll_counts = [0] * 6 # [0,0,0,0,0,0] # generates the basic list for counting

# # for session in range(100):
# #     for _ in range(rolls_per_session):
# #         roll = random.randint(1, 6) # generate the random number

# #         # roll_counts[roll-1] = roll_counts[roll-1] + 1 

# #         roll_counts[roll - 1] += 1 # if 6, increase the count of 6 by 1


# # print("\nResults after 100 sessions:")
# # for i in range(6):
# #     print(f"Number {i + 1} was rolled {roll_counts[i]} times.")



# # check that the user only inputs numbers
# # and must be more than zero

# while True:
#     age = input("What is your age? ")

#     # check if you input numbers
#     if age.isdigit():
#         age = int(age) 
     
#         print(f"Your age is {age}")
#         break
#     else:
#         print("You can only input numbers. ")

# # Exercise 9: Counting Occurrences of a Value
# # Write a program to count how many times a specific number 
# # appears in a list.
# # Example: Input = [1, 2, 2, 3], Check for 2.
# numbers = [1, 2, 2, 3, 2, 4, 2, 5, 2]

# count = 0
# for n in numbers:
#     if n == 2: # if number is 2
#         count += 1 # change count by 1

# print(count)



# #------------------------------------------------------------
# # Exercise 11: Ensuring All Numbers Are Positive
# # Write a program to check that all numbers in a list are 
# # positive. If any number is negative, remove it and print the 
# # updated list.
# numbers = [10, -5, 20, -15, 30, -25]
# n2 = []

# for n in numbers:
#     if n >= 0:
#         n2.append(n)

# print(n2)