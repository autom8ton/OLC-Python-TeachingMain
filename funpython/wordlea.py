'''
Have you played Wordle before? Try it out here >> Wordle - The New York Times (nytimes.com)

In this assignment, you are given a text file containing 5757 5-letter words. 
When you play this game, your starting word often determines how successful you are. 
Having a word with the most number of vowels can be a good starting strategy.

Your task is to write a python program to find the words that contain the most number of vowels.
'''
with open("FiveLetterWords.txt", "r") as f:

  words = f.read().split(",")
  #print(words)

  # objective - find the word with the most number of vowels a, e, i , o, u
  vowels = ["a", "e", "i", "o", "u"]
  letters = list("abcdefghijklmnopqrstuvwxyz")
  vowel1 = []
  vowel2 = []
  vowel3 = []
  vowel4 = []
  vowel5 = []

  for word in words:
    # check which word has most vowels
    count = 0
    for v in vowels:
      if v in word:
        count += 1
   
    if count >= 5:
      vowel5.append(word)
    elif count >= 4:
      vowel4.append(word)
    elif count >= 3:
      vowel3.append(word)
    elif count >= 2:
      vowel2.append(word)
    else:
      vowel1.append(word)
  
  for word in vowel4:
    print(word)