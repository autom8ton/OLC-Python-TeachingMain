'''
Have you played Wordle before? Try it out here >> Wordle - The New York Times (nytimes.com)

In this assignment, you are given a text file containing 5757 5-letter words. 

In this assignment, your task is to find out, which letters in the alphabet will 
occur the most? These letters will help you as they give you a higher chance of getting the word correct.

For example, the letters that appear the least are:

('v', 309)

('x', 138)

('z', 121)

('j', 88)

('q', 53)

Write a python program to find the top 10 letters that occur most frequently.
'''
with open("FiveLetterWords.txt", "r") as f:

  words = f.read().split(",")
  #print(words)

  # objective - find the word with the most number of vowels a, e, i , o, u
  vowels = ["a", "e", "i", "o", "u"]
  letters = list("abcdefghijklmnopqrstuvwxyz")

  # arr_letters contains the count of each letter 
  arr_letters = []
  for i in range(26):
    arr_letters.append(0)

  # check which letters are the best in terms of occurence
  # using 2 lists if dictionary has not been taught
  for w in range(len(letters)):
    for word in words:
      if letters[w] in word:
        arr_letters[w] = arr_letters[w] + 1
      
  #bubble sort algorithm
  n = len(arr_letters)

  for i in range(n-1):
    for j in range(n-i-1):
      if arr_letters[j] < arr_letters[j+1]:
        arr_letters[j], arr_letters[j+1] = arr_letters[j+1], arr_letters[j]
        letters[j], letters[j+1] = letters[j+1], letters[j]
  
  for i in range(len(letters)):
    print("{} : {}".format(letters[i], arr_letters[i]) )

  # below uses dictionary approach (if dictionary already taught)
  # # check which letters are the best in terms of occurence
  # alpha_num={}
  # for w in letters:
  #   for word in words:
  #     if w in word:
  #       alpha_num[w] = alpha_num.get(w,0) +1
  # import operator

  # #alpha_nums = dict(sorted(alpha_num.items(), key=lambda item: item[1]))
  # alpha_nums = sorted(alpha_num.items(), key=operator.itemgetter(1))
  # alpha_nums.reverse()
  # for a in alpha_nums:
  #   print(a)