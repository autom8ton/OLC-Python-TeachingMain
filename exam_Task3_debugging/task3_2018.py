# students = False
# while students == True:
#     comp = input("Enter the Computing test score ")
#     math = int(input("Enter the Mathematics test score ))
#     joint_score = comp + comp
#     if comp > 100 and math > 100:
#         print("Student is awarded a gold award")
#     elif comp >= 100 and math >= 100 or joint_score >= 180:
#         print("Student is awarded a silver award")
#     elif comp >= 75 and math >= 75:
#         print("Student is awarded a bronze award")
#     else:
#         print("NO award this time, keep trying")
#     more_scores = input("Any more test scores to enter? Type 'Y' or 'N' ")
#     if More_scores == 'N':
#         students = True
#     else:
#         students = True

students = True   # 2 change value to True 
while students == True:
    comp = int(input("Enter the Computing test score ")) # 3 need to have int
    math = int(input("Enter the Mathematics test score" )) # 1 missing  "
    joint_score = comp + math # 7 1 of the comp change to math 
    if comp >= 100 and math >= 100: # 4 missing = 
        print("Student is awarded a gold award")
    elif comp >= 100 or math >= 100 and joint_score >= 180:  # 6 and or conditions switched 
        print("Student is awarded a silver award")
    elif comp >= 75 and math >= 75:
        print("Student is awarded a bronze award")
    else:
        print("NO award this time, keep trying")
    more_scores = input("Any more test scores to enter? Type 'Y' or 'N' ")
    if more_scores == 'N': # 5 the variable name is wrong 
        students = True
    else:
        students = True

