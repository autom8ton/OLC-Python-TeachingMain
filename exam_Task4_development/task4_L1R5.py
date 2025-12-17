
# The task is to write a program that computes the aggregate score 
# of all the subject grade points achieved by the students in an examination. 

# The final examination score for every subject taken by a student 
# is classified according to the following grading system: 
'''
Grade = Marks  = Grade Point 
A1    = 75-100 = 1 
A2    = 70-74  = 2 
B3    = 65-69  = 3  
B4    = 60-64  = 4 
C5    = 55-59  = 5 
C6    = 50-54  = 6 
D7    = 45-49  = 7 
E8    = 40-44  = 8 
F9    = 0-39   = 9 
'''

# All codes should have appropriate comments and 
# all identifiers should be appropriately named. [4] 

 

# Task 4.1 

# Write a function getgradepoint () that has a parameter mark passed to it. 
# The function must return the grade point for the mark based on the grading system. [4] 

# Task 4.1
#---------------------------------------










# ---------------------------------------

###############################
# Task 4.2 

# Write a function calL1R5() that takes the result as a parameter. 
# result is a dictionary with the key being the subject, and the value being the score. 

# Here is a sample dictionary format: 
# {"English":0, "Higher Chinese":0, "Chemistry":0, "Geography":0, "Mathematics":0, "Physics":0,"Computing":0} 

# The function must make use of the getgradepoint() function to 
# calculate the grade points of each subject in the result. 

# Your function needs to 
# • either compute English or Higher Chinese as a L1 subject, 
#     whichever grade point is lower 
# • compute the remaining subjects as the R5 subjects 
# • add the grade points of the L1 and R5 subjects as the L1 R5 score 		
# [6] 

# Task 4.2
#####################################################################
#---------------------------------------












#---------------------------------------

###############################################
# Your main program should use the calL1R5() function and display the L1R5 aggregate score.	
# Your program will ask the user to input the scores of 7 subjects. 
# You are not required to validate the inputs.
# [5] 

# Test your program with the following input: 
'''
English = 71 
Higher Chinese = 80 
Chemistry = 63 
Geography = 72 
Mathematics = 60 
Physics = 66 
Computing = 70 
'''

# Task 4.3
#---------------------------------------













#---------------------------------------

###############################
# Task 4.4
# Output the results and the corresponding L1R5 Score into a text file called “resultslip.txt”							
# [6] 

# Expected output in resultslip.txt. The scores will be whatever results that is entered.

# Result Slip
# English = 71 
# Higher Chinese = 80 
# Chemistry = 63 
# Geography = 72 
# Mathematics = 60 
# Physics = 66 
# Computing = 70 
# Computed L1R5: 16 

# Task 4.4
#---------------------------------------





#---------------------------------------

#####################################################################
# Answer Below
#####################################################################

# The task is to write a program that computes the aggregate score 
# of all the subject grade points achieved by the students in an examination. 

# The final examination score for every subject taken by a student 
# is classified according to the following grading system: 
'''
Grade = Marks  = Grade Point 
A1    = 75-100 = 1 
A2    = 70-74  = 2 
B3    = 65-69  = 3  
B4    = 60-64  = 4 
C5    = 55-59  = 5 
C6    = 50-54  = 6 
D7    = 45-49  = 7 
E8    = 40-44  = 8 
F9    = 0-39   = 9 
'''

# All codes should have appropriate comments and 
# all identifiers should be appropriately named. [4] 

 

# Task 4.1 

# Write a function getgradepoint () that has a parameter mark passed to it. 
# The function must return the grade point for the mark based on the grading system. [4] 

# Task 4.1
def getgradepoint(mark):
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

# print(getgradepoint(74))

###############################
# Task 4.2 

# Write a function calL1R5() that takes the result as a parameter. 
# result is a dictionary with the key being the subject, and the value being the score. 

# Here is a sample dictionary format: 
# {"English":0, "Higher Chinese":0, "Chemistry":0, "Geography":0, "Mathematics":0, "Physics":0,"Computing":0} 

# The function must make use of the getgradepoint() function to 
# calculate the grade points of each subject in the result. 

# Your function needs to 
# • either compute English or Higher Chinese as a L1 subject, 
#     whichever grade point is lower 
# • compute the remaining subjects as the R5 subjects 
# • add the grade points of the L1 and R5 subjects as the L1 R5 score 		
# [6] 

# Task 4.2
#####################################################################

def calL1R5(result):
    english = result["English"]
    hchinese = result["Higher Chinese"]
    l1 = 0
    r5 = 0
    if english > hchinese:
        l1 = getgradepoint(english)
    else:
        l1 = getgradepoint(hchinese)
    
    for subject, score in result.items():
        if subject == "English" or subject == "Higher Chinese":
            continue
        else:
            r5 = r5 + getgradepoint(score)
        
    return l1 + r5

# sample = {"English":71, "Higher Chinese":80, "Chemistry":63, "Geography":72, "Mathematics":60, "Physics":66,"Computing":70} 
# print(calL1R5(sample))

###############################################
# Your main program should use the calL1R5() function and display the L1R5 aggregate score.	
# Your program will ask the user to input the scores of 7 subjects. 
# You are not required to validate the inputs.
# [5] 

# Test your program with the following input: 
'''
English = 71 
Higher Chinese = 80 
Chemistry = 63 
Geography = 72 
Mathematics = 60 
Physics = 66 
Computing = 70 
'''

# Task 4.3

results = {"English":0, "Higher Chinese":0, "Chemistry":0, "Geography":0, "Mathematics":0, "Physics":0,"Computing":0} 

for subject in results:
    score = input(f"What is the score for {subject}? ")
    results[subject] = int(score)

calculatedL1R5 = calL1R5(results)
print(f"Your L1R5 score is {calculatedL1R5}")


###############################
# Task 4.4
# Output the results and the corresponding L1R5 Score into a text file called “resultslip.txt”							
# [6] 

# Expected output in resultslip.txt. The scores will be whatever results that is entered.

# Result Slip
# English = 71 
# Higher Chinese = 80 
# Chemistry = 63 
# Geography = 72 
# Mathematics = 60 
# Physics = 66 
# Computing = 70 
# Computed L1R5: 16 

# Task 4.4

with open("resultslip.txt", "w") as fobj:
    for subject, score in results.items():
        fobj.write(f"{subject} : {score} \n")

    fobj.write(f"Calculated L1R5 Score : {calculatedL1R5}")