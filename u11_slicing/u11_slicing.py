word = "MADAM"

# reverse the word
reverse = word[::-1]
print(reverse)

if word == word[::-1]:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")


# create a username based on first 3 characters of first name and last 3 characters of lastname + random number
# [start:stop:step]
fname = "DAVID"
lname = "BECKHAM"

first3 = fname[:3]
print(first3)

last3 = lname[-3:]
print(last3)
import random
username = first3 + last3 + str(random.randint(100,999))
print(username)

# check for palindrome
#level madam

# word[start: stop: step]




###################################################
# Part 1: Learning Exercises

# # Exercise 1: Simple List Slicing
# # Write a program to extract the first 3 elements from a list.
# numbers = [10, 20, 30, 40, 50]
# sliced_numbers = numbers[:3]  # Extract elements from index 0 to 2
# print("First 3 elements: {}".format(sliced_numbers))





# #------------------------------------------------------------
# # Exercise 2: Negative Indexing
# # Write a program to extract the last 2 elements from a list 
# # using negative indexing.
# numbers = [10, 20, 30, 40, 50]
# last_two = numbers[-2:]  # Extract last 2 elements
# print("Last 2 elements: {}".format(last_two))




# #------------------------------------------------------------
# # Exercise 3: Skipping Elements in a List
# # Write a program to extract every other element from a list.

# # slice[0:5:2] # range()
# numbers = [10, 20, 30, 40, 50, 60]
# skipped_numbers = numbers[::2]  # Skip every second element
# print("Every other element: {}".format(skipped_numbers))




# #------------------------------------------------------------
# # Exercise 4: Reversing a List Using Slicing
# # Write a program to reverse a list using slicing.
# numbers = [10, 20, 30, 40, 50]
# reversed_numbers = numbers[::-1]  # Reverse the list
# print("Reversed list: {}".format(reversed_numbers))

# # palindrome LEVEL MADAM



# #------------------------------------------------------------
# # Exercise 5: Simple String Slicing
# # Write a program to extract the first 5 characters from a string.
# text = "Hello, world!"
# sliced_text = text[:5]  # Extract characters from index 0 to 4
# print("First 5 characters: {}".format(sliced_text))




# #------------------------------------------------------------
# # Exercise 6: String Slicing with Steps
# # Write a program to extract every second character from a string.
# text = "abcdefg"
# skipped_chars = text[::2]  # Skip every second character
# print("Every second character: {}".format(skipped_chars))




# #------------------------------------------------------------
