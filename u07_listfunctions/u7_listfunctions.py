# Task 4: List Reverser

# Ask the user to enter a list of 5 numbers (one by one)
# Stores them in a list
# Reverses the list manually (without using reverse() or slice)
# Prints the reversed list

numbers = [4,6,8,9,10]

# reverse1 = numbers[::-1] # slicing (direct way to reverse)
# print(reverse1)

# reverse2 = numbers.reverse()
# print(numbers)

reverse_list = []

for num in numbers:
    reverse_list.insert(0, num)

print(reverse_list)

# palindrome 

# LEVEL 
# MADAM
# RACECAR

# word 



#### LIST ALGORITHM

# REVERSAL OF LIST


# MAX IN A LIST
list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
         5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
         1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
         756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
         2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
         6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
         6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
         4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 99927, 7473, 4105]

maxnum = max(list1)
print(maxnum)

minnum = min(list1)
print(minnum)



# SUM OF A LIST

# AVERAGE OF A LIST



# What is my Chinese Zodiac sign?
# In not more than 10 lines of code, write a program 
# to calculate the Chinese Zodiac sign based on a 
# user's year of birth. (hint: it can be done in 5 lines)

# The most common method depends on Chinese New Year, 
# which is considered as the division of two animal years. 
# When a lunar year comes to an end, the animal will shift to next one. 
# Chinese people’s animal signs are marked by this method.

# How to Calculate Your Chinese zodiac sign mathematically?
# Divide your year of birth by 12 and get the remainder. 
# Each remainder corresponds to an animal sign below.

# 0: Monkey 1: Rooster 2: Dog 3: Pig 4: Rat 5: Ox 6: Tiger 
# 7: Rabbit 8: Dragon 9: Snake 10: Horse 11: Goat

# Sample Output
# Enter your birth year: 1977
# Your Chinese zodiac sign is: Snake
'''

zodiac_animals = ['monkey','rooster','dog','pig','rat','ox',
                  'tiger''rabbit','dragon','snake','horse','goat']

birth_year = int(input("Enter your birth year: "))

remainder = birth_year % 12

zodiac_sign = zodiac_animals[remainder-1]

print(f"Your Chinese zodiac sign is: {zodiac_sign}")

'''

# Ask how many times to roll a six-sided dice
# update the number rolled in a list

# repeat this process 100 times
# print out the number of times each number was rolled
# Enter the number of times to roll the die:10
# Number 1 appears 0 times.
# Number 2 appears 2 times.
# Number 3 appears 2 times.
# Number 4 appears 2 times.
# Number 5 appears 0 times.
# Number 6 appears 4 times.


# assume we roll a six sided dice 100 times
import random

rolls_per_session = int(input("How many times should I roll the six-sided dice each session? "))

# possible dice numbers is 1,2,3,4,5,6

roll_counts = [0] * 6 # [0,0,0,0,0,0] # generates the basic list for counting

for session in range(100):
    for _ in range(rolls_per_session):
        roll = random.randint(1, 6) # generate the random number

        # roll_counts[roll-1] = roll_counts[roll-1] + 1 

        roll_counts[roll - 1] += 1 # if 6, increase the count of 6 by 1


print("\nResults after 100 sessions:")
for i in range(6):
    print(f"Number {i + 1} was rolled {roll_counts[i]} times.")
