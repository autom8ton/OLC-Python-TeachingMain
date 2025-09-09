colour_list = ['red','green', 'blue','orange', 'purple','yellow']
colour_to_find = input("Which colour would you like to search for? ")
items = len(colour_list) # 4. change to colour_list
item_number = 0
colour_found = False
while colour_found == False: # 3. change boolean to False to start the loop
    print('test')
    while item_number < items: # 5 change to < less than items
        if colour_list[item_number] == colour_to_find: # 1. missing == 2. missing colon
            print("There are " + str(items) + " colours in the list, " + colour_to_find + " is item " + str(item_number + 1) + " in the list.") # 6 change to items. #7 item_number is the correct one # 9 should be plus not minus
            colour_found = True
            item_number = items # 8. should be items
        elif item_number == items - 1:
            print("The colour is not in the list. ")
            colour_found = True # 11 change to true
            item_number = items
        else:
            item_number += 1   #= items #10 increment the value of item_number

# colour_list = ['red','green', 'blue','orange', 'purple','yellow']
# colour_to_find = input("Which colour would you like to search for? ")
# items = len(colour_to_find)
# item_number = 0
# colour_found = False
# while colour_found == True:
#     while item_number > items:
#         if colour_list[item_number] = colour_to_find
#             print("There are " + str(item) + " colours in the list, " + colour_to_find + " is item " + str(iten_number - 1) + " in the list.")
#             colour_found = True
#             item_number = item_number
#         elif item_number == items - 1:
#             print("The colour is not in the list. ")
#             colour_found = False
#             item_number = items
#         else:
#             item_number = items

# colour_list = ['red','green', 'blue','orange', 'purple','yellow']
# colour_to_find = input("Which colour would you like to search for? ")
# items = len(colour_list) # 3. should be length of list
# item_number = 0
# colour_found = False # 5. set boolean to False first to start the loop
# while colour_found == False:
#     while item_number < items: # 4. should be less than items
#         if colour_list[item_number] == colour_to_find: # 1. missing colon 2. missing ==
#             print("There are " + str(items) + " colours in the list, " + colour_to_find + " is item " + str(item_number + 1) + " in the list.") # 6. should be items #7 should be item_number # 9 should be item_number + 1 instead of minus
#             colour_found = True
#             item_number = items # 8 should set to the length so can exit loop
#         elif item_number == items - 1:
#             print("The colour is not in the list. ")
#             colour_found = True # 11 set to true to exit the loop
#             item_number = items
#         else:
#             item_number += 1 #items # 10 increment item_number by 1

