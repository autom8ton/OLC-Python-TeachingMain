# with open("ListOf5LetterWords.txt", "r") as fileobj:
#     contents = fileobj.read()

# print(contents)

# use write mode
with open("sample2.txt", "a") as fileobj:
    # write a few lines of text into this file
    fileobj.write("This is my 6 sentence\n")
    fileobj.write("This is my 7 sentence\n")
    fileobj.write("This is my 8 sentence\n")
    fileobj.write("This is my 9 sentence\n")
    fileobj.write("This is my 10 sentence\n")

