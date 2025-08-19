# Task 4 
# You have been asked to write a program for a teacher to enter 
# the students' names and their respective test marks. 
# The test marks are whole numbers only. 

# The program must: 
# (1) allow the user to enter student's name and mark and store 
# the input in 2 different lists. 
# The program does not need to validate student's name. 
# However, it must ask for another mark each time 
# the user enters a mark that is not between 0 and 100 inclusive. 

# (2) ask the user if there are any more students' 
# details to be input. The program does not need to validate this input. 

# (3) calculate the average mark. 

# (4) calculate the name of the student with the highest score. 

################## Expected Output ##############
# When all the input has been entered, the program must display: 
# •	"There are [insert student count] students". 
#   o	The [insert student count] must be replaced with the number of students entered. 

# •	“The average mark is [insert average]”. 
#   o	The [insert average] must be replaced with the average mark, rounded to 1 decimal place. 

# •	[insert student name] scored the highest score of [insert highest score]
#   o	The [insert student name] is replaced with the name of the student 
#       with the highest score and [insert highest score] is replaced with the highest score.

# The program must include appropriate input and output messages. 
# All variables must be appropriately named and suitable comments 
# inserted to explain the algorithm. [4]

########################################################
# Task 4.1
# Write a program to meet the requirements. Save your program as 
# MARKS_2022_<your name>_<index number>.py [12] 
########################################################
# *** Write your code for Task 4.1 here ***


namelist = []
scorelist = []
totalsum = 0
average = 0
maxscore = 0
maxname = ""

while True:
    name = input("Enter the student's name: ")

    while True:
        score = input(f"Enter the score for {name}: ")
        if score.isdigit():
            score = int(score) # convert here so we can validate for number first
            if score >= 0 and score <= 100:
                break
            else:
                print(f"You entered {score}, but score must be between 0 and 100.")
        else:
            print(f"You entered {score}, but score must be a valid number.")
    
    # all valid, so add to list
    namelist.append(name)
    scorelist.append(score)
    print(f"{name} scored {score}")
    # print(namelist) # testing values
    # print(scorelist)

    #### calculating average and max
    totalsum = totalsum + score
    if score > maxscore:
        maxscore = score
        maxname = name

    proceed = input("Press y to continue or any other key to stop: ")
    if proceed.lower() != "y":
        print("Adding of score is done...")

        # showing required output messages
        # "There are [insert student count] students
        print(f"There are {len(namelist)} students.")

        # The average mark is [insert average]
        average = round(totalsum / len(namelist), 1)
        print(f"The average mark is {average}.")

        # 	[insert student name] scored the highest score of [insert highest score]
        print(f"{maxname} scored the highest score of {maxscore}")


        break
    else:
        print("\n" + "*"*15)
        print("Next student >> ")






########################################################
# Task 4.2
# Copy your program from Task 4.1 into another code cell. 
# A student who scored lower than the average mark (rounded down) 
# will need to attend remedial class. 
# The teacher wants to arrange these students into groups of three. 
# If the number of students is not a multiple of 3, 
# the last group will have fewer than 3 students. 
# Each group will then be assigned a peer tutor. 

# Extend your program to: 
# •	store the names and score of students who need to attend remedial class in a dictionary 
# •	include an appropriate output message and display the names of these students. 
# If no students have been identified, display "There are no students for remedial". 

# •	calculate and display with appropriate output message the number of peer tutors needed if there are students identified for remedial. 

# Save your program. [9] 
########################################################
# *** Copy your code from Task 4.1 here and continue *** 
import math

remedial_students = {}

# add to dictionary
for i in range(len(namelist)):
    # average has to be floored down
    if scorelist[i] < math.floor(average):
        rstudent = namelist[i]
        rscore = scorelist[i]

        remedial_students[rstudent] = rscore

total_remedial_students = len(remedial_students)

if total_remedial_students > 0:

    # loop through dictionary to display
    for student,score in remedial_students.items():
        print(f"{student} with score of {score} needs to attend remedial.")

    # use floor division to find number of full groups
    groups = total_remedial_students // 3
    print(f"There are {groups} full group of 3 students")

    # find any leftover students
    leftovers = len(remedial_students) % 3

    if leftovers > 0:
        print(f"There is 1 group with less than 3 students")
        groups += 1

    print(f"There is a total of {groups} groups, and {groups} peer tutors are needed.")

else:
    print("There are no students for remedial.")

