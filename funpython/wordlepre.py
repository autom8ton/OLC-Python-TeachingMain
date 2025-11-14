with open("ListOf5LetterWords.txt", "r") as fobj:
    contents = fobj.read()

    contents = contents.replace("\n", ",")

print(contents)

