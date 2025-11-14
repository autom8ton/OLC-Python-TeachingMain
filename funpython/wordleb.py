'''
Have you played Wordle before? Try it out here >> Wordle - The New York Times (nytimes.com)

In this assignment, you are given a text file containing 5757 5-letter words. 

In the previous assignment, you have to find the word(s) with the highest number of vowels. 

In this assignment, your task is to find out, for each vowel, 
which position in the word will it occur most often?

For example, for the vowel u, it occurs most frequently as the second letter. 
So if you know there is the letter "u" in the word. 
You can try forming a word with "u" in the second position for a better chance.

Example output : u is [75, 534, 313, 154, 13]

** Bonus: Once you have this algorithm, you can run it for every single letter in the alphabet **
'''

with open("FiveLetterWords.txt", "r") as f:

  words = f.read().split(",")
  #print(words)

  # objective - find the word with the most number of vowels a, e, i , o, u
  vowels = ["a", "e", "i", "o", "u"]
  letters = list("abcdefghijklmnopqrstuvwxyz")

  #check for each vowel, which position is the best
  for v in letters:
    lstCount = [0,0,0,0,0]
    for word in words:
      
      for i in range(len(word)):
        if v == word[i]:
          lstCount[i] = lstCount[i] + 1
    print("{} is {}".format(v, lstCount))