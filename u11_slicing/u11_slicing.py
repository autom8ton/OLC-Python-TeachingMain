# ###########################################################
# # Part 2: IN-CLASS Practice Exercises

# # Exercise 7: Extracting Middle Elements from a List
# # Scenario: Extract the middle 3 elements from a list with an odd 
# # number of elements.
# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]     

# midindex = len(numbers) // 2 # floor divide by 2 # gives you the center index

# print(numbers[midindex - 1: midindex + 2])



# # take/ slice parts of a string/ list out

# # word = "SINGAPORE" # a string is a list of characters

# # print(word[0]) # first character
# # print(word[-1])

# # ### slice
# # # [start : stop : step]

# # print(word[:4]) # start from beginning up to character 4

# # print(word[3:6])

# # print(word[-4:]) # start from -4 all the way to the end

# # numlist = [1,2,3,4,5,6,7,8,9]
# # print(numlist[:4])
# # print(numlist[3:6])
# # print(numlist[-4:])

# # word = "SINGAPORE" # a string is a list of characters
# # print(word[::2])

# # # PALINDROMES
# # # LEVEL, MADAM, RACECAR


# # word = "MADAM"
# # # To check if palindrome
# # # reverse the word and check if they are equal

# # revword = word[::-1]
# # print(revword)

# # if word == revword:
# #     print(f"{word} is a palindrome")
# # else:
# #     print(f"{word} is not a palindrome")


# # reverse the word
# # reverse = word[::-1]
# # print(reverse)

# # if word == word[::-1]:
# #     print(f"{word} is a palindrome")
# # else:
# #     print(f"{word} is not a palindrome")


# # # create a username based on first 3 characters of first name and last 3 characters of lastname + random number
# # # [start:stop:step]
# # fname = "DAVID"
# # lname = "BECKHAM"

# # first3 = fname[:3]
# # print(first3)

# # last3 = lname[-3:]
# # print(last3)
# # import random
# # username = first3 + last3 + str(random.randint(100,999))
# # print(username)

# # check for palindrome
# #level madam

# # word[start: stop: step]




# ###################################################
# # Part 1: Learning Exercises

# # # Exercise 1: Simple List Slicing
# # # Write a program to extract the first 3 elements from a list.
# # numbers = [10, 20, 30, 40, 50]
# # sliced_numbers = numbers[:3]  # Extract elements from index 0 to 2
# # print("First 3 elements: {}".format(sliced_numbers))





# # #------------------------------------------------------------
# # # Exercise 2: Negative Indexing
# # # Write a program to extract the last 2 elements from a list 
# # # using negative indexing.
# # numbers = [10, 20, 30, 40, 50]
# # last_two = numbers[-2:]  # Extract last 2 elements
# # print("Last 2 elements: {}".format(last_two))




# # #------------------------------------------------------------
# # # Exercise 3: Skipping Elements in a List
# # # Write a program to extract every other element from a list.

# # # slice[0:5:2] # range()
# # numbers = [10, 20, 30, 40, 50, 60]
# # skipped_numbers = numbers[::2]  # Skip every second element
# # print("Every other element: {}".format(skipped_numbers))




# # #------------------------------------------------------------
# # # Exercise 4: Reversing a List Using Slicing
# # # Write a program to reverse a list using slicing.
# # numbers = [10, 20, 30, 40, 50]
# # reversed_numbers = numbers[::-1]  # Reverse the list
# # print("Reversed list: {}".format(reversed_numbers))

# # # palindrome LEVEL MADAM



# # #------------------------------------------------------------
# # # Exercise 5: Simple String Slicing
# # # Write a program to extract the first 5 characters from a string.
# # text = "Hello, world!"
# # sliced_text = text[:5]  # Extract characters from index 0 to 4
# # print("First 5 characters: {}".format(sliced_text))




# # #------------------------------------------------------------
# # # Exercise 6: String Slicing with Steps
# # # Write a program to extract every second character from a string.
# # text = "abcdefg"
# # skipped_chars = text[::2]  # Skip every second character
# # print("Every second character: {}".format(skipped_chars))




# # #------------------------------------------------------------



# ### LIST AND STRING
# word = "SINGAPORE"

# # word[0] # retrieving the first character
# # word[-1]

# # [start:stop:step]

# # newword = word[3:6]
# # print(newword)


# ###########################################################
# # Part 2. IN-CLASS Practice Exercises

# # Exercise 7: Extracting Middle Elements from a List
# # Scenario: Extract the middle 3 elements from a list with an odd 
# # number of elements.

# # this code must work regardless of how many items they are in the list
# # numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# # ### need to know what is the index right at the middle
# # midindex = len(numbers) // 2 # 

# # print(numbers[midindex - 1 : midindex + 2])







# # '''
# # Question 5: Slice a list into halves.
# # Divide a list into two equal halves and returns both halves.
# # You may assume that the list has an even number of items
# # Example Input: [1, 2, 3, 4, 5, 6]
# # Example Output: [1, 2, 3]  [4, 5, 6]
# # '''
# nums = [1, 2, 3, 4, 5, 6, 7, 8]



# # '''
# # Question 7: Remove the first and last elements of a list using slicing.
# # Create a function that takes a list and returns it without 
# # the first and last elements.
# # Example Input: [0, 1, 2, 3, 4]
# # Example Output: [1, 2, 3]
# # '''



# # '''
# # Question 8: Create a function to reverse the order of elements in a 
# # list only from the second to the last but one.
# # Example Input: [1, 2, 3, 4, 5, 6]
# # Example Output: [1, 5, 4, 3, 2, 6]
# # '''




# # '''
# # # Question 13: 
# # # Write a function called mid3(instring)
# # # Extract the middle three characters from a string
# # # Check that the incoming string must be an odd length, 
# # # Test case 1: example input: abcdefg, example output: cde
# # # Test case 2: example input: helloworld, example output: Invalid, Even length
# # '''




# # # Exercise 9: Reversing Words in a Sentence
# # # Scenario: Reverse the words in a sentence manually.
# # sentence = "Python is fun to learn."

# # ### learn to fun is Python

# # # split a string into a list
# # sentence_list = sentence.split(" ") # ['Python', 'is', 'fun', 'to', 'learn.']
# # print(sentence_list)

# # print(" ".join(sentence_list[::-1]))



# # Exercise 1: Extracting Initials from a Name
# # Scenario: A company wants to display initials for employees on ID cards.
# # Given a full name, extract the initials.

# # Example:
# # Input: "John Michael Smith"
# # Output: "J.M.S"

# # Input: "Alice Bob"
# # # Output: "A.B"

# # # ask the person's name
# # name = input("What is your full name? ").upper()

# # # split this into a list (so that you can loop through it)
# # namewords = name.split(" ")

# # # extract out the first character from each word # loop through
# # initials = ""
# # for word in namewords:
# #     initials = initials + word[0] + "."


# # # add a dot
# # print(initials[:-1])


# # def nameoffunction(nric):

# #     # do what ever code to validate
# #     # return true or false
# #     pass

# # checknric = input("enter nric: ")

# # if nameoffunction(checknric):


students = {"Alice": 85, "Bob": 78, "Charlie": 92, "Diana": 88, "Eve": 76}
# Task 2: Create a new dictionary with students categorized as "Pass" or "Fail".
# Assume a passing grade is 80 or above. 

{"Alice": "Pass",
 "Bob": "Fail"}

result_students = {} # empty dictionary

for name, score in students.items():
    if score >= 
