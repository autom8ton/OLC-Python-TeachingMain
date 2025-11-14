'''
Have you played Wordle before? Try it out here >> Wordle - The New York Times (nytimes.com)

In this assignment, you are given a text file containing 5757 5-letter words. 

In this assignment, your task is to create a program that works like wordle. Your program will:

1. Choose a random word from the list

2. Allow you to input a 5-letter word

3. Validate if you have you have the letter in the correct position, correct letter but in the wrong position, or the wrong letter.

4. You can use the console output to print out the statements
'''
import random

# function for validation
def getWord(wordlist):
  while True:
    word = input("\nType a 5 letter word >> ")

    if word.isalpha(): # check if letters

      if len(word) == 5:
        if word not in wordlist: #the \n is a hack, no time to fix yet
          print("Hello, please enter a real word.")
        else:
          return word
      else:
        print("You must enter a 5-letter word lah. Type again.")
    else:
      print("There are no numbers! You don't know ABC ah.")

# open the file
with open("FiveLetterWords.txt", "r") as f:
  words = f.read().split(",")
  cword = random.choice(words).strip().upper()

  #print(cword) #comment off when done

  # Give chances
  for chance in range(1, 7):
    print("\nGuess number #{} of 6.".format(chance))

    guess = getWord(words)
    guess = guess.upper()

    curr_guess = ""
    display = ""

    # loop through the letter in word
    for i in range(len(guess)):
      if guess[i] == cword[i]:
        curr_guess = curr_guess + " " + guess[i] + " "
      elif guess[i] in cword:
        curr_guess = curr_guess + " ? "
      else:
        curr_guess = curr_guess + " # "
    
    # format the display
    for i in guess:
      display = display + " " + i + " "
    
    print("Your Guess >> " + display)
    print("Eval       >> " + curr_guess)
    print("\n? = letter exists, but wrong place")
    print("# = letter does not exist")
    print("*"*20)

    if guess == cword:
      print("Well done!")
      break
  else:
    print("You ran out of chances")
    print("The word is " + cword)