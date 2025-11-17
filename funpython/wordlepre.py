# open the file and read the contents
with open("FiveLetterWords.txt", "r") as fobj:

    # read the contents of the file
    contents = fobj.read().split(",")

    print(contents)
    
fourletterwords = [] # need empty list to store 
vowels = ["a", "e", "i", "o", "u"]

# loop through all the words in the list
for word in contents:
    vowelcount = 0 # reset vowelcount to zero for every word
    # count the number of unique vowels by doing the below
    # loop through all possible vowels a, e, i, o, u
    for v in vowels:
        # check if this current vowel e.g. a is in the word
        if v in word:
            vowelcount += 1

    # if the number of vowels is 4 add to fourletterwords list
    if vowelcount == 4:
        fourletterwords.append(word)

print(fourletterwords)


# with open("FiveLetterWords.txt","r") as f:
#     contents = f.read().split(",")
#     # print(contents)
# empty = []
# vowels = ["a","e","i","o","u"]
# # letters = []

# for word in contents:
#     vowel = 0 # reset the vowel count for every word
#     for v in vowels:
#         if v in word:
#             vowel += 1 
#     if vowel >= 4:
#         empty += [word]
# print(empty)


















# with open("ListOf5LetterWords.txt", "r") as fobj:
#     contents = fobj.read()

#     contents = contents.replace("\n", ",")

# print(contents)

