# read and open files

# open a file
# reading from the file / writing to the file

### WRITING TO A FILE
# msgs = ["hello\n","how are you\n","today is a happy day\n"]

# fobj = open("test123.txt","w")

# fobj.write("test123\n")
# fobj.writelines(msgs) # takes as input a list 

# with open("test123.txt", "w") as fobj:
#     fobj.writelines(msgs)

# fobj.close()

# READ FROM A FILE
# fobj = open("test123.txt", "r")

# # contents = fobj.read() # reads the entire contents into a string
# contentlist = fobj.readlines()

# # print(contents)

# print(contentlist)

# r - read
# w - write
# a - append
# with open("test123.txt", "r") as fobj:
#     # content = fobj.read() # store the contenst of the file as a single string
#     contentlist = fobj.readlines()

# # print(contentlist)

# for i in range(len(contentlist)):
#     contentlist[i] = f"{i+1}. {contentlist[i]}"

# print(contentlist)

# with open("test123.txt","w") as fobj:
#     fobj.writelines(contentlist)

# with open("test123.txt", "a") as fobj:

#     for i in range(5):
#         task = input("Input a task: ")
#         fobj.write(f"{task}")


# how to open a file, for read, write, append

# .read() , readlines()
# .write(), writelines()

#### to open a file and write to a file

words = [
    "level", "racecar", "orange", "radar", "banana", "civic", "refer",
    "apple", "madam", "kayak", "robot", "reviver", "noon", "pop", "deed",
    "book", "wow", "mirror", "eye", "nope", "rotor", "stats", "hello", 
    "toot", "peep", "school", "mum", "dad", "gig", "noon",
    "python", "coding", "class", "student", "lesson", "computer", "keyboard",
    "monitor", "window", "projector", "teacher", "laptop", "science", "library",
    "pencil", "marker", "whiteboard", "homework", "question", "answer"
]

# fobj = open("somefile.txt","w") #r - read, w - write, a - append
# fobj.writelines(words)
# # fobj.write("Hello 1\n")
# # fobj.write("Hello 2\n")
# # fobj.write("Hello 3\n")
# # fobj.write("Hello 4\n")

# fobj.close() # saves and closes

with open("plaintext.txt","r") as fobj:
    # read the contents
    contents = fobj.read()

print(contents)



##### read the file somefile.txt
# fobj = open("somefile.txt", "r")

# contents = fobj.read() # store into a string
# print(contents)