
# Scenario 1: Palindrome Checker

# Task
# (1) Ask the user to input a word.
# (2) Your code should work regardless of capitalisation.
    # e.g. Level, LEVEL, level are palindromes
# (3) Check if it is a palindrome.

# Expected output:
# The word [level] is a palindrome

# write your code here

# word = "MADAM"

# if word == word[::-1]:
#     print(f"{word} is a palindrome")





# word = input("Input a word: ")

# if word.isalpha():
#     wordlow = word.lower() # note that the original word is not changed.

#     if wordlow == wordlow[::-1]: # use slicing method to reverse
#         print(f"{word} is a palindrome.")
#     else:
#         print(f"{word} is not a palindrome.")

# alternative method to reverse (if cannot use slicing)

# word = "abcdef"

# reversed = ""

# for char in word:
#     reversed = char + reversed # add the character at beginning of word

# print(f"{reversed} is the reverse of {word}")


###########################################################
# Scenario 2: Palindrome Word Challenge (with Word List)

# A language teacher is preparing a classroom game. 
# Students must find palindromic words from a given list. 
# You're writing a program to help the teacher check '
# 'which words are palindromes.

# Task
# (1) Use the list below.
# (2) Loop through all the words.
# (3) Print only the words that are palindromes.
# ** BONUS: write a function to check if a word is a palindrome.

words = [
    "level", "racecar", "orange", "radar", "banana", "civic", "refer",
    "apple", "madam", "kayak", "robot", "reviver", "noon", "pop", "deed",
    "book", "wow", "mirror", "eye", "nope", "rotor", "stats", "hello", 
    "toot", "peep", "school", "mum", "dad", "gig", "noon",
    "python", "coding", "class", "student", "lesson", "computer", "keyboard",
    "monitor", "window", "projector", "teacher", "laptop", "science", "library",
    "pencil", "marker", "whiteboard", "homework", "question", "answer"
]






###########################################################