with open("FiveLetterWords.txt", "r") as fobj:
    contents = fobj.read()
    # print(contents)

listofwords = contents.split(",")


# #wordle strategy

# one_vowel = []
# two_vowel = []
# three_vowel = []
# four_vowel = []
# five_vowel = []

# vowels = ["a", "e", "i", "o", "u"]

# for i in listofwords:
#     vowel_count = 0
#     for v in vowels:
#         if v in i:
#             vowel_count += 1
#     if vowel_count == 1:
#         one_vowel += [i]
#     elif vowel_count == 2:
#         two_vowel += [i]
#     elif vowel_count == 3:
#         three_vowel += [i]
#     elif vowel_count == 4:
#         four_vowel += [i]
#     elif vowel_count == 5:
#         five_vowel += [i]

# print(four_vowel)

# #wordle position

# #a
# listcounter = [0, 0, 0, 0, 0]



# for i in listofwords:
#     if i[0] == "a":
#         listcounter[0] += 1
#     if i[1] == "a":
#         listcounter[1] += 1
#     if i[2] == "a":
#         listcounter[2] += 1
#     if i[3] == "a":
#         listcounter[3] += 1
#     if i[4] == "a":
#         listcounter[4] += 1

# print(listcounter)

# letterusage = {"a" : 0,
# "b" : 0,
# "c" : 0,
# "d" : 0,
# "e" : 0,
# "f" : 0,
# "g" : 0,
# "h" : 0,
# "i" : 0,
# "j" : 0,
# "k" : 0,
# "l" : 0,
# "m" : 0,
# "n" : 0,
# "o" : 0,
# "p" : 0,
# "q" : 0,
# "r" : 0,
# "s" : 0,
# "t" : 0,
# "u" : 0,
# "v" : 0,
# "w" : 0,
# "x" : 0,
# "y" : 0,
# "z" : 0}


# for i in listofwords:
#     for j in letterusage:
#         if j in i:
#             letterusage[j] += 1
# print(letterusage)


#choose random word
import random

#correctword = listofwords[random.randint(0, 5757)].upper()
correctword = "CARRY"

count = 0
while count < 6:
    guess = input("Guess a 5-letter word: ").upper()

    count += 1
    
    print("""
    ⬛ = letter is not in word
    🟨 = letter is in word, but wrong position
    🟩 = letter is in word and correct position    """)

    feedback = ""

    for i in guess:
        if correctword.find(i) == -1:
            feedback += "⬛"
        elif correctword.find(i) != guess.find(i):
            feedback += "🟨"
        elif correctword.find(i) == guess.find(i):
            feedback += "🟩"
    print(feedback)