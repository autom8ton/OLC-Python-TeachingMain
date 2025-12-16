# Task 3.1
# Edit the program so that it converts the first letter of the first word
#  of the book title input for book to upper case.
# Save your program. [1]

book_authors = {
    'Winnie the pooh': 'A. A. Milne',
    'The tale of peter rabbit': 'Beatrix Potter',
    'The wind in the willows': 'Kenneth Grahame',
    'The lion, the witch and the wardrobe': 'C. S. Lewis',
    'Charlie and the chocolate factory': 'Roald Dahl'
}

book = input('Please enter the title of a book: ')
add = input("Would you like to add a book> Y or N: ")
amend = input("Would you like to change the author of a book? Y or N: ")




#--------------------------------------------------
# Task 3.2

# Copy and paste your program from sub-task 3.1.

# Edit your program so that it outputs the author of the book that is input. 
# A suitable output message must be used.

# Save your program. [2]
#------------------------------------------------





#------------------------------------------------
# Task 3.3
# Copy and paste your program from sub-task 3.2.

# Edit your program so that if the user 
# enters the value 'Y' when the user is asked about adding a book, it:

# > asks the user for the title of the book to be added
# >  takes the title of the book as input
# >  asks the user for the author of the book to be added
# >  takes the author of the book as input
# >  adds the title and its author to the dictionary in the format title:author
# >  outputs the dictionary at the end of the program.

# You do not need to consider any validation for the input of the book title and the author. 
# You do not need to convert the first letter of the first word of the book title to upper case.

# Save your program. [4]
#------------------------------------------------





##########################################

# book_authors = {
#     'Winnie the pooh': 'A. A. Milne',
#     'The tale of peter rabbit': 'Beatrix Potter',
#     'The wind in the willows': 'Kenneth Grahame',
#     'The lion, the witch and the wardrobe': 'C. S. Lewis',
#     'Charlie and the chocolate factory': 'Roald Dahl'
# }

# book = input('Please enter the title of a book: ')
# # Task 3.1 

# # using slicing
# book = book[0].upper() + book[1:]

# # Task 3.2 start
# author = book_authors[book]
# print(f"The author of {book} is {author}")

# add = input("Would you like to add a book> Y or N: ")
# # Task 3.3 start
# if add.upper() == "Y":
#     addbook = input("What is the title of the new book? ")
#     addauthor = input(f"What is the author of {addbook}? ")

#     # add to dictionary
#     book_authors[addbook] = addauthor

#     print(book_authors)


# amend = input("Would you like to change the author of a book? Y or N: ")

##---------------------------------------------------------------

# Task 3.4

# Copy and paste your program from sub-task 3.3.

# Edit your program so that if the user enters 
# the value 'Y' when the user is asked about 
# changing the author for a book, it:

# >> asks the user for the title of the book
# >> takes the title of the book as input
# >> asks the user for the new author to replace the current author
# >> takes the new author of the book as input
# >> validates the author name to make sure it does not 
#       contain any numeric values, repeating until the input is valid
# >> changes the author in the dictionary for the title of the book input.

# You do not need to convert the first letter of the 
# first word of the book title to upper case.

# Save your JupyterLab notebook for Task 3.
# [3]

# print("1111A".isdigit())


book_authors = {
    'Winnie the pooh': 'A. A. Milne',
    'The tale of peter rabbit': 'Beatrix Potter',
    'The wind in the willows': 'Kenneth Grahame',
    'The lion, the witch and the wardrobe': 'C. S. Lewis',
    'Charlie and the chocolate factory': 'Roald Dahl'
}

book = input('Please enter the title of a book: ')
# Task 3.1 

# using slicing
book = book[0].upper() + book[1:]

# Task 3.2 start
author = book_authors[book]
print(f"The author of {book} is {author}")

add = input("Would you like to add a book> Y or N: ")
# Task 3.3 start
if add.upper() == "Y":
    addbook = input("What is the title of the new book? ")
    addauthor = input(f"What is the author of {addbook}? ")

    # add to dictionary
    book_authors[addbook] = addauthor

    print(book_authors)


amend = input("Would you like to change the author of a book? Y or N: ")
# Task 3.4
if amend.upper() == "Y":
    amendbook = input("What book's author would you like to change? ")

    # need to validate that author does not contain numeric
    while True:
        amendauthor = input("What is the new author's name? ")
        isnumeric = False
        for c in amendauthor:
            if c.isdigit():
                isnumeric = True
                break
        
        if isnumeric:
            print("You cannot enter numbers for author name.")
        else:
            break # means no numerics detected
    
    print(book_authors) # testing to see that it changes correctly
