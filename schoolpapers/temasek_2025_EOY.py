# Your program code and output for each of Tasks 1 to 5 should be saved In a
# single.ipynb file using Jupylerlab. For example, your program code and output
# for Task 1 should be saved as:
# TASKl_<your name>_<your class> <index number>.ipynb - -
# Make sure that each of your .ipynb files shows the required output in JupyterLab.

##########################################
# Task 1
# Alex is_ helping Temasek school bookshop to manage Its product price list that is
# stored in a file called PRODUCT.csv. Each line in lhe file conlalns a product name
# and its price, separated by a comma.
# Open an empty file PRODUCT_PRICE.ipynb from lhe lhumb drive and save the file
# as:
# TASKl_<your name>_<your_class>_<index_number>.ipynb

# The task is to write a program code so that it:

##--------------------------------------------------------
# (a) [1]reads and displays all products and its prices 
# from the CSV file named PRODUCT.csv . 

# Expected output:
# pen,$1.80
# ruler,$0.50
# eraser,$0.20
##--------------------------------------------------------
# Write your code here

##--------------------------------------------------------
# (b) [1] allows the user to enter a new product name and price. 
##--------------------------------------------------------
# Write your code here

##--------------------------------------------------------
# (c) [2] adds the new product to the CSV file and displays message "new product added" 

# Example input and output:
# Enter a new product: glue
# Enter the new product price: $1.50
# new product added
##--------------------------------------------------------
# Write your code here


##--------------------------------------------------------
# (d) [3] prevents adding duplicate product and displays message "duplicate product"]
# Example input and output :
# Enter a new product: pen
# duplicate product
##--------------------------------------------------------
# Write your code here


##--------------------------------------------------------
# (e) [2] displays the updated product list in the format shown below.
# Expected output:
# Product  Price:
# Pen      $1.80
# Ruler    $0.50
# Eraser   $0.20
# glue     $1.50
##--------------------------------------------------------
# Write your code here

##--------------------------------------------------------
# (f) [1] closes the file properly after each operation
##--------------------------------------------------------
# Write your code here

# All inputs and outputs must have suitable messages.

# Save your Jupyterlab notebook for Task 1.

# END OF TASK 1 #####################################################
#####################################################################


##########################################
# Task 4
# Open a now Jupyterlab notebook and save the file as:
# TASK4_<your_name>_<your_class>_<index_number>.ipynb

# The task is to write a function remove_word(phrase) that removes
# consecutive repeated words in a phrase. The program:

# >> allows the user to input a phrase and convert to lower case [1]

# >> converts the phrase into a list of words. 
#     Do this without the help of the builtin
#     strings function such as str.split() [3]

# >> removes consecutive repeated words from the list [3]

# >> converts the list back into a new phrase. 
#      Do this without the help of the built-in
#     string functions such as str.join() [2]

# >> returns and displays the new phrase. [1]

# Save your Jupyterlab notebook for Task 4.

# Sample Output 1:
# Enter a phrase: Im a big big girl in a big big world
# New phrase: im a big girl in a big world

# Sample Output 2:
# Enter a phrase: Sorry sorry sorry sorry sorry naega naega
# New phrase: sorry naega


# im a big big girl in a big big world
["im","a","big","big","girl"]


def remove_word(phrase):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # converts the phrase into a list of words.  [3] 

    # Code to split a string into a list without using .split()
    ### SIMPLE ENOUGH CODE - BUT DOES NOT CATCH SOME SCENARIOS
    wordlist = []

    # loop through every character in the sentence (phrase)
    for char in phrase:
        if char == " ":
            wordlist.append(thisword) 
            thisword = ""
        else:
            thisword = thisword + char
    wordlist.append(thisword) # for the last word
    print(wordlist)

    #### COMPLEX CODE - BUT BETTER
    # separator = " "         # what separates one word from the next
    # position_separator = 0     # current position of delimiter
    # previous_position = 0         # position
    # wordlist = []              # list to hold the final output

    # while True: # while because you do not know how long this phrase is.
    #     # find the position of the " " separator from previous position
    #     position_separator = phrase.find(separator, previous_position)

    #     # if no separator found, means its the last word.
    #     if position_separator == -1:
    #         wordlist.append(phrase[previous_position:])
    #         break

    #     # slice the word from previous position, to the next separator
    #     wordpart = phrase[previous_position:position_separator]

    #     wordlist.append(wordpart) # append the sliced word

    #     # advance the previous position to next letter
    #     previous_position = position_separator + len(separator)
    
    # print(wordlist) # testing only

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # removes consecutive repeated words from the list [3]
    clean_wordlist = []

    #im a big big girl in a big big world

    for i in range(len(wordlist)):
        # handle first word, and add first word by default
        if i == 0:
            clean_wordlist.append(wordlist[i])
            continue
        
        # check if current word is the same as previous word
        if wordlist[i] != wordlist[i-1]:
            clean_wordlist.append(wordlist[i])
    
    # print(clean_wordlist) # testing only

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # converts the list back into a new phrase. [2]
    sentence = ""
    for w in clean_wordlist:
        sentence = sentence + w + " "

    # print(sentence) # testing only

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # returns and displays the new phrase. [1]
    return sentence


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # allows the user to input a phrase and convert to lower case [1]
# phrase = input("Enter a phrase").lower()
phrase = "Im a big big girl in a big big world".lower()
# phrase = "Sorry sorry sorry sorry sorry naega naega".lower()
cleaned = remove_word(phrase)
print(cleaned) # testing only



# 


# phrase = "im a big big girl in a big big world"
# wordlist = [] 
# thisword = ""

# # loop through every character in the sentence (phrase)
# for char in phrase:
#     if char == " ":
#         wordlist.append(thisword) 
#         thisword = ""
#     else:
#         thisword = thisword + char
# wordlist.append(thisword) # for the last word
# print(wordlist)


