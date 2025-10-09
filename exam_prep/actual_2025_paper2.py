# Task 2
word_list = ["apple", "window", "bend", "paper", "thought"]

#---------------------------------------
#Task 2.1
# new_word = input("Input a new word: ").lower()
# word_list.append(new_word)
#---------------------------------------

#---------------------------------------
# Task 2.2
# new_word = input("Input a new word: ").lower()
# word_list.append(new_word)

# countmore5 = 0
# for w in word_list:
#     if len(w) >= 5:
#         countmore5 += 1
#         print(f"{w} has 5 or more letters.")

# print(f"There are {countmore5} words with 5 or more letters.")
#---------------------------------------

#---------------------------------------
# Task 2.3
# new_word = input("Input a new word: ").lower()
# word_list.append(new_word)

# countmore5 = 0
# for w in word_list:
#     if len(w) >= 5:
#         countmore5 += 1
#         print(f"{w} has 5 or more letters.")

# print(f"There are {countmore5} words with 5 or more letters.")

# # Start of 2.3
# countsame = 0
# for w in word_list:
#     if w[0] == w[-1]:
#         countsame += 1
#         print(f"{w} begins and end with the same letter.")

# print(f"There are {countsame} words that begin and end with the same letter")
#---------------------------------------

##############################################################################
#Task 3

book_authors = {
    'Winnie the pooh': 'A. A. Milne',
    'The tale of peter rabbit': 'Beatrix Potter',
    'The wind in the willows': 'Kenneth Grahame',
    'The lion, the witch and the wardrobe': 'C. S. Lewis',
    'Charlie and the chocolate factory': 'Roald Dahl'
}

# book = input('Please enter the title of a book: ')
# add = input("Would you like to add a book> Y or N: ")
# amend = input("Would you like to change the author of a book? Y or N: ")

#---------------------------------------
# Task 3.1 
# book = input('Please enter the title of a book: ')

# # book = book.title() # easiest
# book = book[0].upper() + book[1:] # or this
# # print(book)

# add = input("Would you like to add a book> Y or N: ")
# amend = input("Would you like to change the author of a book? Y or N: ")

#---------------------------------------


#---------------------------------------
# Task 3.2
# book = input('Please enter the title of a book: ')

# # book = book.title() # easiest
# book = book[0].upper() + book[1:] # or this
# # print(book)

# if book in book_authors:
#     print(f"The author of {book} is {book_authors[book]}")
# else:
#     print(f"Book {book} is unknown.")

# add = input("Would you like to add a book> Y or N: ")
# amend = input("Would you like to change the author of a book? Y or N: ")
#---------------------------------------


#---------------------------------------
# Task 3.3
# add = input("Would you like to add a book> Y or N: ").upper()

# if add == "Y":
#     book = input('Please enter the title of a book: ')
#     # book = book[0].upper() + book[1:] # or this

#     author = input(f"Please enter the author for {book}: ")

#     book_authors[book] = author

# print(book_authors)

    # if book in book_authors:
    #     print(f"The author of {book} is {book_authors[book]}")
    # else:
    #     print(f"Book {book} is unknown.")

    # amend = input("Would you like to change the author of a book? Y or N: ")
#---------------------------------------



#---------------------------------------
# Task 3.4
# add = input("Would you like to add a book> Y or N: ").upper()

# if add == "Y":
#     book = input('Please enter the title of a book: ')
#     # book = book[0].upper() + book[1:] # or this

#     author = input(f"Please enter the author for {book}: ")
#     book_authors[book] = author

# print(book_authors)

# amend = input("Would you like to change the author of a book? Y or N: ").upper()
# if amend == "Y":
#     book = input('Please enter the title of a book: ')

#     while True:
#         new_author = input(f"Please enter the new author for {book}: ")

#         gotnum = False
#         for c in new_author:
#             if c.isdigit():
#                 gotnum = True
#                 break

#         if gotnum:
#             print("Numbers not allowed in author name. Try again.")
#         else:
#             book_authors[book] = new_author
#             break

#     print(book_authors)

#---------------------------------------

############################################################
# Task 4 Debugging
# group_1 = []
# group_2 = []
# group_3 = []
# flag = True
# while flag:
#     first_name = input("Please enter the child's name: ").upper()
#     first_name = first_name[1]
#     age = input("Please enter the child's age: ")
#     if first_letter >= "A" and first_letter <= "M" and age > 10:
#         group_1 = group_1 + [first_name]
#     elif first_letter >= "M" or age > 10:
#         group_2 = group_2 + [first_name]
#     elif age < 10:
#         group_3 = group_3 + [first_name]
#         count += 1
#     more = input("Do you have another child to enter, Y or N?: ")
#     if more == "Y":
#         flag = False

# print("You have entered the names of", flag, "children")
# print("The members of group 1 are", group_1)
# print("The members of group 2 are", group_2)
# print("The members of group 3 are", group_3)

############# ANSWER FOR 
# group_1 = []
# group_2 = []
# group_3 = []
# count = 0 # 4. set initial value of count to 0
# flag = True
# while flag:
#     first_name = input("Please enter the child's name: ").upper()
#     first_letter = first_name[0] # 1. should be first_letter not first_name, #2 should be index 0
#     age = int(input("Please enter the child's age: ")) #3. convert to int()
#     if first_letter >= "A" and first_letter <= "M" and age > 10:
#         group_1 = group_1 + [first_name]
#     elif first_letter > "M" and age > 10: # 8 should be > M, not >= M, 11. should be and condition
#         group_2 = group_2 + [first_name]
#     elif age <= 10: # 9 should be <= 10
#         group_3 = group_3 + [first_name]
#     count += 1 # 10. count should happen regardless of the groups
#     more = input("Do you have another child to enter, Y or N?: ").upper() #6. force to upper
#     if more == "N": # 5. should be N to stop loop
#         flag = False

# print("You have entered the names of", count, "children") # 7. should be count, not flag
# print("The members of group 1 are", group_1)
# print("The members of group 2 are", group_2)
# print("The members of group 3 are", group_3)



###################################################
# Task 5

# -------------------------------------------------
# Task 5.1
def total_cost(cost):
    tax = cost * 0.09 # calculate the tax of 9%
    total = cost + tax

    return total
# -------------------------------------------------

# -------------------------------------------------
# Task 5.2
def total_cost(cost):
    tax = cost * 0.09 # calculate the tax of 9%
    total = cost + tax

    return total

# start of 5.2 code
def discount(cost):

    if cost >= 50 and cost < 100:
        discount = 0.05 * cost
        
    elif cost >= 100:
        discount = 0.1 * cost
    else:
        discount = 0

    cost = cost - discount # apply the discount first

    cost = total_cost(cost) # calculate the tax

    return cost
# -------------------------------------------------


# -------------------------------------------------
# Task 5.3
def total_cost(cost):
    tax = cost * 0.09 # calculate the tax of 9%
    total = cost + tax

    return total

def discount(cost):

    if cost >= 50 and cost < 100:
        discount = 0.05 * cost
        
    elif cost >= 100:
        discount = 0.1 * cost
    else:
        discount = 0

    cost = cost - discount # apply the discount first

    cost = total_cost(cost) # calculate the tax

    return cost

# start of 5.3 code
# def reward_points()