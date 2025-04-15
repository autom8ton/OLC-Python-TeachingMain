# # File IO

# # r = read, w = write, a = append
# msg = ["hello 224", "how are you 324", "i am fine thank you 424"]

# # write a file 
# fobj = open("test222.txt", "a")

# # fobj.write("hello\n")
# # fobj.write("how are you\n")
# # fobj.write("i am fine thank you.\n")

# # .writelines() # takes a list as input
# # fobj.writelines(msg)

# for i in msg:
#     fobj.write(i + "\n")

# fobj.close() ### IMPORTANT 

# fobj = open("test222.txt", "a")
# with open("test222.txt", "a") as fobj:
#     fobj.write("something else \n")

    # do not need close()

####### OPEN A FILE AND RETRIEVE THE CONTENTS

# fobj = open("test222.txt", "r")

# # contents = fobj.read() # reads the entire content of the file into a string

# contentlist = fobj.readlines()

# print(contentlist)



with open("filename.txt", "r") as fobj:
    content = fobj.read()