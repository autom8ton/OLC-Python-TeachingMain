count = 1
total = 0
max_score = 50
min_score = 50

print("Enter student scores (0-50). Enter -1 to send.")
score = int(input("Enter score: ")
while score != -1:
    if score > 0 or score < 50:
        count += 1
        total = total + score
        if score > max_score:
            max_score = score
        elif score < min_score:
            min_score = score
else:
        print("Invalid score! Please enter 0 - 50 only")
    score = int(input("Enter score: "))

print("Processing results...")
if count = 0:
    print("No scores were entered")
else:
    average = total // count
    print(f"Number of scores: {count}")
    print(f"Maximum score: {max_score}\tMinimum score: {min_score}")
    print("Average score: {average}")



# # DEBUGGING 
count = 0 # 6. count should start from 0 not 1
total = 0
max_score = 0 #7. max_score has to start from lowest possible, i.e. 0
min_score = 50

print("Enter student scores (0-50). Enter -1 to send.")
score = int(input("Enter score: ")) # 1. close bracket
while score != -1:
    if score > 0 and score < 50: # 10. should be and condition
        count += 1
        total = total + score
        if score > max_score:
            max_score = score
        if score < min_score: # 11. cannot do an elif 
            min_score = score
    else: # 3. indentation, else is for if, not while.
        print("Invalid score! Please enter 0 - 50 only") # 2. indentation
    score = int(input("Enter score: ")) # 5. this input must be part of while, not else

print("Processing results...")
if count == 0: # 4. missing double equals
    print("No scores were entered")
else:
    average = total // count # 9. should not be floor divide
    print(f"Number of scores: {count}")
    print(f"Maximum score: {max_score}\tMinimum score: {min_score}")
    print(f"Average score: {average}") #8 missing f for fstring

################################################
# # DEBUGGING ORIGINAL
# count = 1
# total = 0
# max_score = 50
# min_score = 50

# print("Enter student scores (0-50). Enter -1 to send.")
# score = int(input("Enter score: ")
# while score != -1:
#     if score > 0 or score < 50:
#         count += 1
#         total = total + score
#         if score > max_score:
#             max_score = score
#         elif score < min_score:
#             min_score = score
# else:
#         print("Invalid score! Please enter 0 - 50 only")
#     score = int(input("Enter score: "))

# print("Processing results...")
# if count = 0:
#     print("No scores were entered")
# else:
#     average = total // count
#     print(f"Number of scores: {count}")
#     print(f"Maximum score: {max_score}\tMinimum score: {min_score}")
#     print("Average score: {average}")

########################################################
