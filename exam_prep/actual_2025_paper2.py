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
book = input('Please enter the title of a book: ')

# book = book.title() # easiest
book = book[0].upper() + book[1:] # or this
# print(book)

if book in book_authors:
    print(f"The author of {book} is {book_authors[book]}")
else:
    print(f"Book {book} is unknown.")

add = input("Would you like to add a book> Y or N: ")
amend = input("Would you like to change the author of a book? Y or N: ")
#---------------------------------------


#---------------------------------------
# Task 3.3
add = input("Would you like to add a book> Y or N: ").upper()

if add == "Y":
    book = input('Please enter the title of a book: ')
    book = book[0].upper() + book[1:] # or this

    author = input(f"Please enter the author for {book}")
    


    if book in book_authors:
        print(f"The author of {book} is {book_authors[book]}")
    else:
        print(f"Book {book} is unknown.")


    amend = input("Would you like to change the author of a book? Y or N: ")
#---------------------------------------