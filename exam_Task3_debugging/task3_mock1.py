### DO NOT CHANGE the first 3 lines of code.
books = {"1": "AVAILABLE", "2": "AVAILABLE", "3": "AVAILABLE", "4":"BORROWED"}
action = input("Enter 'B' to borrow a book or 'R' to return a book: ")
book_id = input("Enter the book ID: ")
### Make your code fixes after this

if action.lower() == "b": # 1. action = "b", # 2. missing colon # 9. change to lower
    if books[book_id] == "AVAILABLE": # value is in upper case
        books[book_id] = "BORROWED" # 10. books["B"] = "borrowed" 2 errors here
        print("You have borrowed the book.")
    else:
        print("The book is already borrowed.")
elif action.lower() == "r": # 3. elif action = "r" # double equal #10 change to lower
    if books[book_id] == "BORROWED": # 11. value is upper case
        books[book_id] = "AVAILABLE" # 4. books("R") dictionary is [] # 12 book_id # 13 upper case
        print("You have returned the book.") # 5. missing quotation
    else:
        print("The book is already available.") # 6. indentation error
else: # 7. indentation error. 
    print("Invalid action.") #8. missing quotation

print(books)

# A library program needs to keep track of books being 
# borrowed and returned. Each book has a unique ID 
# and a title. The program allows a user to input the 
# book ID and whether the book is being borrowed or returned.

# The program updates the status of the book accordingly 
# and displays a message. There are several syntax and 
# logic errors in the program.

### DO NOT CHANGE the first 3 lines of code.
books = {"1": "AVAILABLE", "2": "AVAILABLE", "3": "AVAILABLE", "4":"BORROWED"}
action = input("Enter 'B' to borrow a book or 'R' to return a book: ")
book_id = input("Enter the book ID: ")
### Make your code fixes after this

if action = "b"
    if books[book_id] == "Available":
        books["B"] = "borrowed"
        print("You have borrowed the book.")
    else:
        print("The book is already borrowed.")
elif action = "r":
    if books[book_id] == "borrowed":
        books("R") = "available"
        print(You have returned the book.")
    else:
    print("The book is already available.")
    else:
        print("Invalid action.)