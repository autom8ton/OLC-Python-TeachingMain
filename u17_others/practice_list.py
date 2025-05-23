# (1)
# A private school is opening for registration. 
# It is not known how many students will be signing up.
# Write a program to keep track of names and students who have signed up. 

# A "X" is entered to indicate the end of registration.
# Print out a class list, which includes an index number and name 
# for all students according to their registration sequence [3m]

# Assume that the input data will always be valid.

# Data to be tested Ivan, Dino, Ben, Ethan, Shion, Navan, X

# Sample Output
"""
Enter a new name ('X' to quit): Ivan
Enter a new name ('X' to quit): Dino
Enter a new name ('X' to quit): Ben
Enter a new name ('X' to quit): Ethan
Enter a new name ('X' to quit): Shion
Enter a new name ('X' to quit): Navan
Enter a new name ('X' to quit): X

Class List
1 Ivan
2 Dino
3 Ben
4 Ethan
5 Shion
6 Navan
"""
#####################################################################
# input()
# list to store
# while loop >> x to break

# for loop through the list








# (2) On the first day of school, a student informed the
# school that he will be joining another school nearer his home.
# Teacher finds that it is difficult to look for the 
# students' name as they were listed according to their registration sequence.

# Write a program to remove the name of the student. 
# Print out a new class list listed according to alphabetic sequence [3m]

# Use the following name list: ['Ivan','Dino','Ben','Ethan','Shion','Navan']

# Data to be tested: Dino

"""
Enter name to remove: Dino

Class List
1 Ben
2 Ethan
3 Ivan
4 Navan
5 Shion
"""






# (3) During registration, a student's name was entered wrongly. 
# Write a program to replace the name of a student who had registered earlier.
# Print out a new class list [3m]

# Assume that the input data will always be valid.

# Data to be tested: Ben, Benedict

"""
# Sample output
Enter name to change: Ben
Enter new name: Benedict

Class List
1 Benedict
2 Dino
3 Ethan
4 Ivan
5 Navan
6 Shion
"""




# (4)
# During PE lesson, the teacher records down the students 
# weight and height so that their BMI can be calculated.

# Write a program to keep track of the student's weight 
# and height. Calculate their Body Mass Index (BMI) using the following:
# BMI = weight in kg/ squared of height in m

# Print out a list of students which includes the 
# name, weight, height and BMI [5m]

# Assume that the input data will always be valid.

# Data to be tested:
# Vani, Wt = 50, Ht = 1.6
# Ethan, Wt = 60, Ht = 1.6
# Jay, Wt = 80, Ht = 1.6

# Use this namelist ['Vani','Ethan','Jay']
# * Bonus: if you indicate if the student is obese (BMI more than 30)

"""
#Sample output

Enter data for Vani
Enter weight in kg: 50
Enter height in m: 1.6

Enter data for Ethan
Enter weight in kg: 60
Enter height in m: 1.6

Enter data for Jay
Enter weight in kg: 80
Enter height in m: 1.6

Vani is 50.0KG 1.6M with a BMI of 20
Ethan is 60.0KG 1.6M with a BMI of 23
Jay is 80.0KG 1.6M with a BMI of 31
Jay is overweight

"""

namelist = ['Vani','Ethan','Jay']

# data = [["Vani",50,1.6,24], [""]]
heightlist = []
weightlist = []
bmilist = []

# for name in namelist:
#     # ask for weight
    