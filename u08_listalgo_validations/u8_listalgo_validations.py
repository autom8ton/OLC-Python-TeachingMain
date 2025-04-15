fruits = ['apple', 'orange', 'grape'] 

# how to access items from a list
print(fruits[2])

# change the value of orange to durian
fruits[1] = "durian"
print(fruits)

# add a new fruit to this list watermelon
fruits.append("watermelon")
print(fruits)

fruits.insert(1, "rambutan")
print(fruits)

# remove grape from the list
fruits.remove("grape")
print(fruits)

# remove second position in the list
del fruits[1]
print(fruits)

# remove the last value and assign to a variable
fruits.pop()
print(fruits)

###################################################
# Part 1: Learning Exercises


# # Exercise 1: Finding the Maximum Without Built-In Functions
# # Write a program to find the largest number in a list without 
# # using max().
# numbers = [12, 45, 67, 23, 89, 34, 78, 56]
# largest = numbers[0]  # Assume the first number is the largest
# for num in numbers:
#     if num > largest:  # Compare each number
#         largest = num
# print("The largest number is: {}".format(largest))





# #------------------------------------------------------------
# # Exercise 2: Calculating the Sum Without Built-In Functions
# # Write a program to calculate the sum of numbers in a list 
# # without using sum().
# numbers = [5, 10, 15, 20, 25, 30, 35]
# total = 0
# for num in numbers:
#     total += num  # Add each number to the total
# print("The total sum is: {}".format(total))




# #------------------------------------------------------------
# # Exercise 3: Calculating the Average of a List
# # Write a program to calculate the average of numbers in a list.
# # Example: Input = [4, 8, 12, 16, 20], Output = 12.
# numbers = [4, 8, 12, 16, 20, 24, 28, 32]
# total = 0
# for num in numbers:
#     total += num
# average = total / len(numbers)  # Calculate average
# print("The average is: {}".format(average))




# #------------------------------------------------------------
# # Exercise 4: Validating List Length
# # Write a program to ensure a list contains at least 5 elements.
# # Prompt the user to add more values until the condition is met.
# my_list = [1, 2]
# while len(my_list) < 5:
#     new_value = int(input("Enter a number to add to the list: "))
#     my_list.append(new_value)
# print("Final list: {}".format(my_list))




# #------------------------------------------------------------
# # Exercise 5: Validating Range of Input
# # Write a program to ensure a user enters a number between 1 and 
# # 100. Repeat until a valid input is given.
# while True:
#     number = int(input("Enter a number between 1 and 100: "))
#     if 1 <= number <= 100:  # Check range
#         break  # Exit loop if valid
#     print("Invalid input. Try again.")
# print("You entered: {}".format(number))




# #------------------------------------------------------------
# # Exercise 6: Validating Presence in a List
# # Write a program to ensure a specific value exists in a list.
# # Prompt the user until they enter a value present in the list.
# my_list = ["apple", "banana", "cherry", "date", "elderberry"]
# while True:
#     user_input = input("Enter a fruit (apple, banana, cherry, date, elderberry): ")
#     if user_input in my_list:
#         break  # Exit loop if valid
#     print("That fruit is not in the list. Try again.")
# print("You entered: {}".format(user_input))




# #------------------------------------------------------------
# # Exercise 7: Validating Non-Empty Input
# # Write a program to ensure the user enters a non-empty value.
# # Prompt the user until they enter a valid input.
# while True:
#     user_input = input("Enter a non-empty string: ")
#     if user_input.strip():  # Check for non-empty input
#         break  # Exit loop if valid
#     print("Input cannot be empty. Try again.")
# print("You entered: {}".format(user_input))



# #------------------------------------------------------------