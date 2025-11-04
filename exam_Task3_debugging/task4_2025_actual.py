group_1 = []
group_2 = []
group_3 = []
count = 0 # 4. set initial value of count to 0
flag = True
while flag:
    first_name = input("Please enter the child's name: ").upper()
    first_letter = first_name[0] # 1. should be first_letter not first_name, #2 should be index 0
    age = int(input("Please enter the child's age: ")) #3. convert to int()
    if first_letter >= "A" and first_letter <= "M" and age > 10:
        group_1 = group_1 + [first_name]
    elif first_letter > "M" and age > 10: # 8 should be > M, not >= M, 11. should be and condition
        group_2 = group_2 + [first_name]
    elif age <= 10: # 9 should be <= 10
        group_3 = group_3 + [first_name]
    count += 1 # 10. count should happen regardless of the groups
    more = input("Do you have another child to enter, Y or N?: ").upper() #6. force to upper
    if more == "N": # 5. should be N to stop loop
        flag = False

print("You have entered the names of", count, "children") # 7. should be count, not flag
print("The members of group 1 are", group_1)
print("The members of group 2 are", group_2)
print("The members of group 3 are", group_3)

# group_1 = []
# group_2 = []
# group_3 = []
# flag = True
# while flag:
#     first_name = input("Please enter the child's name: ").upper()
#     first_name = first_name[1]
#     age = input("Please enter the child's age: ")
#     if first_letter >= "A" and first_letter <= "M" and age > 10:
#         group_1 = group_1 + [first_name]
#     elif first_letter >= "M" or age > 10:
#         group_2 = group_2 + [first_name]
#     elif age < 10:
#         group_3 = group_3 + [first_name]
#         count += 1
#     more = input("Do you have another child to enter, Y or N?: ")
#     if more == "Y":
#         flag = False

# print("You have entered the names of", flag, "children")
# print("The members of group 1 are", group_1)
# print("The members of group 2 are", group_2)
# print("The members of group 3 are", group_3)



