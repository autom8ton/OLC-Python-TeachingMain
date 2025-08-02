# 3 modes, r, w, a

# write mode
# if files does not exist, it will create it
# if file exists, it will overwrite it

# # create a file
# fobj = open('filename.txt', 'a')

# # to write to a file
# fobj.write("\nnext next year will be the best")

# # close the file/ flushes the memory
# fobj.close()

# open a file and read it
# fobj = open('filename.txt', 'r')
# with open('filename.txt', 'r') as fobj:
#     content = fobj.read() # content is a string

#     print(content)

# # read the contents
# # count how many letter a there is in your file

# # use a for loop to loop through the string
# counta = 0
# for c in content:
#     if c.lower() == 'a':
#         counta = counta + 1 # counta += 1

# print(f"THere are {counta} A in the file")


####################
# .readlines()

#choose a random day of the week
# import random
# with open('filename.txt', 'r') as fobj:
#     # read the contents of the file into a list
#     daylist = fobj.readlines() 
#     # print(daylist)

#     for day in daylist:
#         print(day)

# randay = random.choice(daylist)
# print(f"Random day: {randay}")

# .write(), .read(), .readlines(), .writelines()

planetslist = ["mercury\n", "venus\n","earth\n", "mars\n", 
               "jupiter\n", "saturn\n", "uranus\n"]
with open("planets.txt", "w") as fobj:
    fobj.writelines(planetslist)



# challenge: create a task planner
# Part 1
# This program will ask you to input what you want to do
# keep asking until the user say "no"
# save this task list into a file called task.txt

# Part 2:
# open the file and print out the task you have to do today

# tasklist = [] # creating an empty list
# while True:
#     task = input("What do you have to do today? ")
#     tasklist.append(task + "\n")

#     proceed = input("Type N to stop").upper()
#     if proceed == "N":
#         ## write to the file here...
#         with open('task.txt', 'a') as fobj:
#             fobj.writelines(tasklist)

#         break

#################################################
# A text file shapes.txt stores a list of shapes with a 
# comma between each value.  

# The current contents of shapes.txt are: 
# star,sphere,square,triangle 

# A text file colours.txt stores a list of colours 
# with a comma between each value.  

# The current contents of colours.txt are: 
# red,yellow,green,blue 

# A program reads the data from each file and creates a dictionary of the values 
# so that each shape has an associated colour. 
# The first value in each file will be joined, for example, star and red. 

# The data is stored in a global dictionary with the identifier data_stored. 

data_stored = {} # empty dictionary

# read the shapes.txt store it as a list

# read the colours.txt store it as a list