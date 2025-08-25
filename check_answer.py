# while True:
#     x = int(input("PLayer 1, Please input a whole number between 1 and 50 inclusive, for player 2 to guess"))
#     if x<1 or x>50:
#         print("You have inputted a invalid number, please try again.")
#     else:
#         break
# MAX_GUESSES = 5
# guesses = 0
# while MAX_GUESSES > guesses:
#     y = int(input("Player 2 ,Please input a whole number between 1 and 50 inclusive"))
#     if y == x :
#         print("You have gotten the correct answer")
#         break
#     else:
#         print("You have got the wrong answer")
#         guesses += 1
# if guesses > MAX_GUESSES:
#     print("GAME OVER")

# queue = ["Person1", "Person2", "Person3", "Person4", "Person5"]
# rotate = int(input("How may time to roate? : "))
# person = queue[0]
# for i in range(rotate+1):
#     queue.remove(person)
#     queue.insert(i,person)
# print(queue)

# queue = ["Person1", "Person2", "Person3", "Person4", "Person5"]
# rotate = int(input("How many times to rotate? : "))

# for i in range(rotate):
#     first_person = queue.pop(0)   # remove first person
#     queue.append(first_person)    # add them to the back

# print(queue)
number = float(input("Enter a number: "))
i = 0
total = 1
while i < number:
    i += 1
    total = total * i 
print(total)