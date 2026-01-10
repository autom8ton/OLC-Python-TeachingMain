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

wrong_letter = "#"
wrong_letter_position = "?"

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

def evaluate_guess(guess, answer):
    result = [wrong_letter] * 5

    # count letter in answer and put into dictionary
    letter_count = {}
    for char in answer:
        if char in letter_count:
            letter_count[char] = letter_count[char] + 1
        else:
            letter_count[char] = 1

    #Pass 1 check for correct 
    for i in range(5):
        if guess[i] == answer[i]:
            result[i] = guess[i]
            letter_count[guess[i]] -= 1 # reduce the count for correct letter

    # Pass 2: check correct letter but wrong position, also to check duplicates
    for i in range(5):
        # If this position was already correct in Pass 1, skip it
        if result[i] == guess[i]:
            continue
        thischar = guess[i]

        if thischar in letter_count:
            # count so that we show exact number of correct letters... e.g. carry and type rarer > ?  A  R  #  #
            if letter_count[thischar] > 0:
                result[i] = wrong_letter_position
                letter_count[thischar] -= 1 

    return result
 
  
# open the file
with open("FiveLetterWords.txt", "r") as f:
    words = f.read().split(",")
    cword = random.choice(words).strip().upper()
    # cword = "CARRY"

    #print(cword) #comment off when done

    # Give chances
    for chance in range(1, 7):
        print("\nGuess number #{} of 6.".format(chance))

        guess = getWord(words)
        guess = guess.upper()

        curr_guess = ""
        display = ""

        # call function to evaluate and output the symbols 
        symbols = evaluate_guess(guess, cword)
        for s in symbols:
            curr_guess += " " + s + " "
        
        # format the display
        for i in guess:
            display = display + " " + i + " "
        
        print("Your Guess >> " + display)
        print("Eval       >> " + curr_guess)
        print(f"\n{wrong_letter_position} = letter exists, but wrong place")
        print(f"{wrong_letter} = letter does not exist")
        print("*"*20)

        if guess == cword:
            print("Well done!")
            break
    else:
        print("You ran out of chances")
        print("The word is " + cword)