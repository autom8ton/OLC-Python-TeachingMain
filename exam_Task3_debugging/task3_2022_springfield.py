'''
# Original Code - Do not change
import math
while true:
    dice_list = []
    for i in range(2):
        input("Player {}, press enter to roll the three dice".format(i+1))
        dice = {0}*3
        for j in range(3):
            dice[j] = random.randint(0,6)
        dice_list.eppend(dice)
        print("Player {}, dice = {}" .format(i,dice))
    if max(dice_list[0]) > max(dice_list[1]):
        print("Player 1 wins!")
    elif max(dice_list[0]) = max(dice_list[1]):
        print("No winners!")
    elif:
        print("Player 2 wins!")

    play = input("Play again? (Y/N): ").isupper()
    if play == 'N':
        print("Thank you for playing, goodbye!")
        break:
'''

# # # Answer as below
import random #1) random
while True: # 2) True
    dice_list = []
    for i in range(2):
        input("Player {}, press enter to roll the three dice".format(i+1))
        dice = [0]*3 # 3)[0]
        for j in range(3):
            dice[j] = random.randint(1,6) #4(1,6) 0 is not a dice value
        dice_list.append(dice) #5. append()
        print("Player {}, dice = {}" .format(i+1,dice)) #6 i+1
    if max(dice_list[0]) > max(dice_list[1]):
        print("Player 1 wins!")
    elif max(dice_list[0]) == max(dice_list[1]): #7) == 
        print("No winners!")
    else: #8) #else
        print("Player 2 wins!")

    play = input("Play again? (Y/N): ").upper() #isupper() #9 .upper()
    if play == 'N':
        print("Thank you for playing, goodbye!")
        break # 10. remove :


# import random # changed math to random because random is used but math is not
# while True: # changed true to True
#     dice_list = []
#     for i in range(2):
#         input("Player {}, press enter to roll the three dice".format(i+1))
#         dice = [0]*3 # changed from {0}*3 to [0]*3 to create a list
#         for j in range(3):
#             dice[j] = random.randint(1,6) # changed range from (0,6) to (1,6)
#         dice_list.append(dice) # changed .eppend() to .append()
#         print("Player {}, dice = {}" .format(i+1,dice)) # corrected player number by changing i to i+1
#     if max(dice_list[0]) > max(dice_list[1]):
#         print("Player 1 wins!")
#     elif max(dice_list[0]) == max(dice_list[1]):
#         print("No winners!")
#     else:
#         print("Player 2 wins!")
        
#     play = input("Play again? (Y/N): ").upper() # changed .isupper() to .upper()
#     if play == 'N':
#         print("Thank you for playing, goodbye!")
#         break