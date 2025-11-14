from random import randint

# To store the past guesses
past = []
results = []

# List of words
listWord = ""

with open("ex311_WordList.txt") as file:
	listWord = (file.read()).upper().split("\n")

# Function to get user's guess
def getWord(chance):
	# Repeatively asking for guess
	while True:
		print(f"Guess {chance} of 6", end="")
		ans = input(" >> ")
		
		# Check for just alphabet
		if ans.isalpha():
			# Check for length
			if len(ans) == 5:
				# Check if the word exists
				if ans.upper() in listWord:
					# Break out of the loop by returning the word
					return ans.upper()
				else:
					print("Please enter a valid word.\n")
			else:
				print("Please guess a 5 letter word.\n")
		else:
			print("Please do not enter any characters that is not alphabet.\n")

# Function to get solution characters count
def getSolnCount():
	global word
	ans = {}
	
	# Populate the counts
	for i in word:
		try:
			ans[i] += 1
		except:
			# the letter has not appear yet
			ans[i] = 1
	return ans

# Function to format the terminal screen
def formatScreen():
	global past
	global results

	# Reset the screen to make it like a "game console"
	print("\033c", end="")

	# Iterating through the pass result
	for i in range(len(past)):
		print(f"GUESS {i + 1} of 6 >> {past[i]}")
		print(f"        EVAL >> {results[i]}")

# Check if the user had found the word
found = False

# To generate the word
word = listWord[randint(0, len(listWord) - 1)]

# Repeat 6 times to say it's a try
for i in range(1, 7):
	guess = getWord(i)
	past.append(" ".join(list(guess)))
	solnCount = getSolnCount()
	resultsCounter = ["", "", "", "", ""]
	
	# Algorithms
	# Case 1: The user guess correctly!
	if guess == word:
		results.append("O O O O O")
		formatScreen()
		found = True
		break
	# Case 2: The user didn't guess correctly...
	else:
		# We need to loop through the guess to populate the result in the following order:
		# 1. Correct Position
		# 2. Wrong Position, but exists
		# 3. Didn't exists

		# Correct Position take precedence over the rest, with the rest can be done from left to right. Stacked Loop!

		# Case 1: Letter in the correct position
		for j in range(len(guess)):
			if guess[j] == word[j]:
				# Fill in the results
				resultsCounter[j] = "O"
				# Reduce the character count as it had been found.
				solnCount[guess[j]] -= 1

		# Case 2/3: Letter exists/doesn't exist
		for j in range(len(guess)):
			if resultsCounter[j] == "":
				# Using a try/except. If letter found → No error thrown.
				try:
					# Check if there exists remaining (for duplicate letters)
					if solnCount[guess[j]] > 0:
						# Case 2 found
						resultsCounter[j] = "#"
						solnCount[guess[j]] -= 1
					else:
						# Case 3 found, as guess > character cound
						resultsCounter[j] = "X"
				except:
					# Case 3 found as characters doesn't exists
						resultsCounter[j] = "X"
		
		# Feedback to the past results
		results.append(" ".join(resultsCounter))
		formatScreen()

# Game Conclusion
if found:
	print("Yay! You solved the puzzle")
else:
	print(f"Sorry. The correct word is ... {word}.")