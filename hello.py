# colour_list = ["red", "green", "blue", "orange", "purple", "yellow"]
# colour_to_find = input("Which colour would you like to search for? ")
# items = len(colour_list)  # fixed len of colour list 
# item_number = 0
# colour_found = False 
# while colour_found == False: # change to False
#     # print("sfsdf")
#     while item_number < items: # testing with less than
#         # print("lalala")
#         if colour_list[item_number] == colour_to_find: # fixed missing double equal and colon
#             # print(f"First {item_number}")
#             # fixed item to items
#             print("There are " + str(items) + " colours in the list, " + colour_to_find + " is item " + str(item_number + 1) + " in the list.") # fixed item_number - 1, becos zero based.
#             colour_found = True
#             item_number = items # should be items (len of list)
#         elif item_number == items - 1:
#             # print(f"Second {item_number}")
#             print("The colour is not in the list.")
#             colour_found = False
#             item_number = items
#         else:
#             # print(f"Third {item_number}")
#             # item_number = items # should be increment item_number value
#             item_number += 1# testing increment item number

# colour_list = ["red", "green", "blue", "orange", "purple", "yellow"]
# colour_to_find = input("Which colour would you like to search for? ")
# items = len(colour_to_find)
# item_number = 0
# colour_found = False
# while colour_found == True:
#     while item_number > items:
#         if colour_list[item_number] = colour_to_find
#             print("There are " + str(item) + " colours in the list, " + colour_to_find + " is item " + str(item_number - 1) + " in the list.")
#             colour_found = True
#             item_number = item_number
#         elif item_number == items - 1:
#             print("The colour is not in the list.")
#             colour_found = False
#             item_number = items
#         else:
#             item_number = items


# def record(name, cca):
#     f = open('cca.txt','a')     # 'a' means append to the last line of the file   
#     f.write(name)
#     f.write("\n")               # take note that I changed "," to "\n" so that each \n create a new line
#     f.write(cca)                
#     f.write("\n")               # each new line will be considered as an element in a list of you use readlines()
#     f.close()   

# name = input("Enter student's name: ")
# cca = input("Enter his/her cca: ")

# record(name, cca)

# with open('cca.txt', 'r') as fobj:
#     x = fobj.readlines() 
# print(x)


namelist = ["John","Malcolm","William"]
agelist = [34,56,23]

num = int(input("How many staff to enter? "))

for staff in range(num):
    name = input("What is the name of the staff? ")
    age = int(input("What is the age of the staff? "))

    namelist.append(name)
    agelist.append(age)

print(namelist)
print(agelist)


changedindex = namelist.index("Malcolm") # find the index of a particular item
namelist[changedindex] = "Samson" # change the value of the index in the list
print(namelist)
    
#david.lee@computhink.com.sg