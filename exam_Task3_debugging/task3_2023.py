# Answer for Debugging Task 3 Question

# backup for the original buggy code
# import random
# questions = 10
# answer_list = []
# correct = 0
# incorrect = 0
# total_mark = 0
# for x in range(questions): # 11. Should not minus 1 from questions
#     num1 = random.randint(1, 50) 
#     num2 = random.randint(1, 50) 
#     answer = num1 + num2 # 3. missing variable for answer
#     print("What is", num1, "+", num2, "?")
#     user_answer = int(input()) # 7. input must convert to integer
#     if user_answer == answer:
#         if num1 > 25 and num2 > 25: #9. should be and condition.
#             total_mark = total_mark + 2  
#         else:
#             total_mark = total_mark + 1
#         #8. This code was in the wrong place. out of if condition
#         answer_list = answer_list + ["Correct"] # 1. fixed wrong quotation mark  
#     else:
#         answer_list = answer_list + ["Incorrect"]
# # print(answer_list) # testing purpose

# list_length = len(answer_list) #- 1 # 2. removed wrong minus sign, #4. fixed answer_list -1
# for i in range(list_length):
#     if answer_list[i] == "Correct": # 10. variable should be i, not x
#         correct = correct + 1 # 6. not adding properly, changed to correct + 1
# if correct  == 1: ## 5. message variable is wrong, replace with correct
#     message = "correct answer."
# else:
#     message = "correct answers."
# print("Your total mark is", total_mark, "and you had", correct, message)

import random
questions = 10 # temporarily change to 3 first
answer_list = []
correct = 0
incorrect = 0
total_mark = 0
for x in range(questions):  # 6. no need to -1
    num1 = random.randint(1, 50)  # temp removal
    num2 = random.randint(1, 50)  # temp removal
    answer = num1 + num2 # 3. fixed answer variable not defined
    print(answer) # temp, will remove later
    print("What is", num1, "+", num2, "?")
    user_answer = input()
    if int(user_answer) == answer: # 7. convert input() into int

        if num1 > 25 and num2 > 25: #8. should be and condition
            total_mark = total_mark + 2
            # answer_list = answer_list + ['Correct'] # 1. fixed quotation mark
        else:
            total_mark = total_mark + 1
        answer_list = answer_list + ['Correct']  # 11. need to add "Correct" regardless of marks
    else:
        answer_list = answer_list + ["Incorrect"]

    print(answer_list) 
list_length = len(answer_list) # - 1 # 2 fixed minus character #4 actually i don't need to -1 here 
for i in range(list_length):
    if answer_list[i] == "Correct": #10 should be i, not x
        correct = correct + 1 # 9. fixed wrong minus to increase
if correct  == 1: # 5. fixed message, should be correct variable
    message = "correct answer."
else:
    message = "correct answers."
print("Your total mark is", total_mark, "and you had", correct, message)
