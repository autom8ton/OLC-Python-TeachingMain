# Task 4
# The task is to write a program that computes the aggregate score of all the 
# subject grade points achieved by the students in an examination.
# The final examination score for every subject taken by a student is 
# classified according to the following grading system:

# All codes should have appropriate comments and all identifiers should be appropriately
# named. [2]

# Task 4.1
# Write a function getgradepoint ( ) that has a parameter mark passed to it. The
# function must return the grade point for the mark based on the grading system. [4]
# Grade	Marks	Grade Point
# A1	    75-100	1
# A2	    70-74	2
# B3	    65-69	3
# B4	    60-64	4
# C5	    55-59	5
# C6	    50-54	6
# D7	    45-49	7
# E8	    40-44	8
# F9	    0-39	9
#------------------------------------------------------------




# Task 4.2
# Write a function calL1R5( ) that takes the result as a parameter. The function
# must make use of the getgradepoint ( ) function to calculate the 
# grade points of each subject in the result.

# Your function needs to
# • either compute English or Higher Chinese as a L1 subject, whichever grade
# point is lower
# • compute the remaining subjects as the R5 subjects
# • add the grade points of the L1 and R5 subjects as the L1 R5 score [3]
#------------------------------------------------------------






# Task 4.3
# Your main program should use the calL1R5( ) function and display the L1R5
# aggregate score.						[2]
# Test your program with the following input:
# Subjects	Marks
# English	71
# Higher Chinese	80
# Chemistry	63
# Geography	72
# Mathematics	60
# Physics	66
# Computing	70
#------------------------------------------------------------


#########################################################################
# Answer Below

# Task 4
# The task is to write a program that computes the aggregate score of all the 
# subject grade points achieved by the students in an examination.
# The final examination score for every subject taken by a student is 
# classified according to the following grading system:

# All codes should have appropriate comments and all identifiers should be appropriately
# named. [2]

# Task 4.1
# Write a function getgradepoint ( ) that has a parameter mark passed to it. The
# function must return the grade point for the mark based on the grading system. [4]
# Grade	Marks	Grade Point
# A1	    75-100	1
# A2	    70-74	2
# B3	    65-69	3
# B4	    60-64	4
# C5	    55-59	5
# C6	    50-54	6
# D7	    45-49	7
# E8	    40-44	8
# F9	    0-39	9

#------------------------------------------------------------
def getgradepoint(mark):
    mark = int(mark)
    
    if mark >= 75:
        return 1
    elif mark >= 70:
        return 2
    elif mark >= 65:
        return 3
    elif mark >= 60:
        return 4
    elif mark >= 55:
        return 5
    elif mark >= 50:
        return 6
    elif mark >= 45:
        return 7
    elif mark >= 40:
        return 8
    else:
        return 9



# def calL1R5(result):

# Task 4.2
# Write a function calL1R5( ) that takes the result as a parameter. 
# result is a dictionary with the key being the subject, and the value being the score. 
# Here is a sample dictionary format:
# {"English":71, "Higher Chinese":71, "Chemistry":71, "Geography":71, 
#  "Mathematics":71, "Physics":71,"Computing":71}


# Your function needs to
# • either compute English or Higher Chinese as a L1 subject, whichever grade
# point is lower
# • compute the remaining subjects as the R5 subjects
# • add the grade points of the L1 and R5 subjects as the L1 R5 score [3]
#------------------------------------------------------------



def call1r5(result):
    l1 = 0
    r5 = 0

    eng = result["English"]
    hchin = result["Higher Chinese"]
    if eng > hchin or eng == hchin:
        l1 = getgradepoint(result["English"])
    else:
        l1 = getgradepoint(result["Higher Chinese"])

    for sub, grade in result.items():
        if sub == "English" or sub == "Higher Chinese":
            continue
        else:
            r5 = r5 + getgradepoint(grade)
    
    return l1 + r5

# test = {"English":71, "Higher Chinese":80, "Chemistry":63, "Geography":72, 
#         "Mathematics":60, "Physics":66,"Computing":70} 
# print(call1r5(test))

# Task 4.3
# Your main program should use the calL1R5( ) function and display the L1R5
# aggregate score.						[2]
# Test your program with the following input:
# Subjects	Marks
# English	71
# Higher Chinese	80
# Chemistry	63
# Geography	72
# Mathematics	60
# Physics	66
# Computing	70
#------------------------------------------------------------
