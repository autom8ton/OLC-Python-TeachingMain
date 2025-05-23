# colour_list = ["red", "green", "blue", "orange", "purple", "yellow"]
# colour_to_find = input("Which colour would you like to search for? ")
# items = len(colour_list)  # fixed len of colour list 
# item_number = 0
# colour_found = False 
# while colour_found == False: # change to False
#     # print("sfsdf")
#     while item_number < items: # testing with less than
#         # print("lalala")
#         if colour_list[item_number] == colour_to_find: # fixed missing double equal and colon
#             # print(f"First {item_number}")
#             # fixed item to items
#             print("There are " + str(items) + " colours in the list, " + colour_to_find + " is item " + str(item_number + 1) + " in the list.") # fixed item_number - 1, becos zero based.
#             colour_found = True
#             item_number = items # should be items (len of list)
#         elif item_number == items - 1:
#             # print(f"Second {item_number}")
#             print("The colour is not in the list.")
#             colour_found = False
#             item_number = items
#         else:
#             # print(f"Third {item_number}")
#             # item_number = items # should be increment item_number value
#             item_number += 1# testing increment item number

# colour_list = ["red", "green", "blue", "orange", "purple", "yellow"]
# colour_to_find = input("Which colour would you like to search for? ")
# items = len(colour_to_find)
# item_number = 0
# colour_found = False
# while colour_found == True:
#     while item_number > items:
#         if colour_list[item_number] = colour_to_find
#             print("There are " + str(item) + " colours in the list, " + colour_to_find + " is item " + str(item_number - 1) + " in the list.")
#             colour_found = True
#             item_number = item_number
#         elif item_number == items - 1:
#             print("The colour is not in the list.")
#             colour_found = False
#             item_number = items
#         else:
#             item_number = items


# def record(name, cca):
#     f = open('cca.txt','a')     # 'a' means append to the last line of the file   
#     f.write(name)
#     f.write("\n")               # take note that I changed "," to "\n" so that each \n create a new line
#     f.write(cca)                
#     f.write("\n")               # each new line will be considered as an element in a list of you use readlines()
#     f.close()   

# name = input("Enter student's name: ")
# cca = input("Enter his/her cca: ")

# record(name, cca)

# with open('cca.txt', 'r') as fobj:
#     x = fobj.readlines() 
# print(x)


# namelist = ["John","Malcolm","William"]
# agelist = [34,56,23]

# num = int(input("How many staff to enter? "))

# for staff in range(num):
#     name = input("What is the name of the staff? ")
#     age = int(input("What is the age of the staff? "))

#     namelist.append(name)
#     agelist.append(age)

# print(namelist)
# print(agelist)


# changedindex = namelist.index("Malcolm") # find the index of a particular item
# namelist[changedindex] = "Samson" # change the value of the index in the list
# print(namelist)
    
#david.lee@computhink.com.sg



# #         Example 02
# # Modify the program below to extracts letters from the 
# # given string and prints out the remainder.
# from random import randint as num

# rando_str = "" # initialisation of string
# for i in range(num(10,20)) : # random length between 10 - 20

#     rando_str+=chr(num(32,90)) # adding random characters to the string
# print(rando_str)


# # loop through each character in rando_str
# tempstring = ""

# for c in rando_str:
#     if c.isalpha():
#         tempstring += c
#         # tempstring = tempstring + c

# print(tempstring)

# for loop - finite loop

# while loop - do not know how many times loop

# for i in range(10):
#     print(i)

# count = 0
# while count < 10:
#     print(count)
#     count = count + 1

# while loop is good for validations




######################################################
# Question 2:
# The school's swimming coach has recorded the 50m freestyle 
# swim times (in seconds) for 15 swimmers. 
# Using the list provided, find and display the fastest and slowest swim times, 
# along with their swim lane position in the list.

# Assume that the first item in the list is swim lane position 1.
# #####################################################
# swim_times = [32.5, 30.1, 33.8, 29.6, 31.2, 34.0, 28.9, 
#               30.4, 32.1, 27.5, 35.6, 31.8, 29.2, 33.0, 30.5]
# # Answer for Question 2 here

# fasttime = swim_times[0]
# slowtime = swim_times[0]

# fastposition = 0
# slowposition = 0

# # for i in swim_times:
# for i in range(len(swim_times)):
#     if swim_times[i] < fasttime:
#         fasttime = swim_times[i]
#         fastposition = i
#     if swim_times[i] > slowtime:
#         slowtime = swim_times[i]
#         slowposition = i

# print(f"Fastest: Lane {fastposition + 1}, Time: {fasttime}s")
# print(f"Slowest: Lane {slowposition + 1}, Time: {slowtime}s")


# [start:stop:step]

# generation of username
# check for palindrome

# generate a username: 
# first 3 characters of first name
# last 3 characters of last name
# + a 3-digit random number 100 - 999
# Assume name is only 2 words, Michael Tan >>> mictan568

name = input("What is your name? ")

# 1 function
# ask how many lockers

# generate 5 random pin (1000-9999)

# return a list of pins

# function
# student needs to know the pin and locker number
# 3 tries to get pin correct, then locker assigned to him (using dictionary)
# return the locker number

# main code
# ask the student's name
# store dictionary student and locker number (start from 1)
# Student can only have 1 locker
