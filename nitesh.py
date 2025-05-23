
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
##################
# classlist= []
# while True:
#     student= input("Enter a new name ('X' to quit): ")
#     if student.upper() == 'X':
#         break
#     else:
#         classlist.append(student)

# classlist = ['Ivan', 'Dino', 'Ben', 'Ethan', 'Shion', 'Navan']
# print(classlist[0])
# print(classlist[1])
# print(classlist[2])
# print(classlist[3])
# print(classlist[4])
# print(classlist[5])

# # for name in classlist: # direct loop through of the list items
# for i in range(len(classlist)): # range(6) #0,1,2,3,4,5
#     print(f"{i+1} {classlist[i]}")


# # for i in range(6):
# #     print(i)


########################################

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
# classlist = ['Ivan','Dino','Ben','Ethan','Shion','Navan']
# # ask for the name to remove first
# remove_name = input("Enter name to remove: ")

# classlist.remove(remove_name)
# print(classlist)

# # sort the class list . sorted()
# classlist = sorted(classlist)
# print(classlist)

# # print out the class list
# print("Class List")
# for i in range(len(classlist)):
#     print(f"{i+1} {classlist[i]}")



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
# classlist = ['Ivan','Dino','Ben','Ethan','Shion','Navan']

# # ask for name, then change it
# oldname = input("Enter name to change: ")
# newname = input("Enter new name: ")

# oldindex = classlist.index(oldname)
# print(oldindex)

# classlist[oldindex] = newname
# print(classlist)

# # not sure if sorted???
# classlist = sorted(classlist)

# # print 
# print("Class List")
# for i in range(len(classlist)):
#     print(f"{i+1} {classlist[i]}")

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
#####################################################################

namelist = ['Vani','Ethan','Jay']
weightlist = []
heightlist = []
bmilist = []

# loop through all the students
for student in namelist:
    print(f"Enter data for {student}")

    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in m: "))
    bmi = round(weight / (height ** 2))

    weightlist.append(weight)
    heightlist.append(height)
    bmilist.append(bmi)

# print(namelist)
# print(weightlist)
# print(heightlist)
# print(bmilist)

# ['Vani',              'Ethan',           'Jay']
# [50.0,                60.0,               80.0]
# [1.6,                 1.6,                 1.6]
# [19.531249999999996, 23.437499999999996, 31.249999999999993]

for i in range(len(namelist)):
    # Vani is 50.0KG 1.6M with a BMI of 20
    print(f"{namelist[i]} is {weightlist[i]}KG {heightlist[i]}M with a BMI of {bmilist[i]}")
    if bmilist[i] > 30:
        print(f"{namelist[i]} is overweight")