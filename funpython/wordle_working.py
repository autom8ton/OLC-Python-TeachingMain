with open("FiveLetterWords.txt") as fobj:
    read_words = fobj.read() # returns a string
words = read_words.split(',')

# print(words)

vowels = ['a', 'e', 'i','o','u']

vowel4 = [] # this list will store the 4 vowel words

for word in words: # loops through every single word...
    vcount = 0
    # print(word)
    for v in vowels: # loop through every single vowel
        if v in word:
            # print(word)
            vcount += 1

    # after this loop, you will know how many vowels this words has
    if vcount == 4:
        vowel4.append(word)
        # print(word)

# after looping through all 5000+ words, print the vowel4 list
print(vowel4)

