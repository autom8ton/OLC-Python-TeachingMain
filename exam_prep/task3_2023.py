# Answer for Debugging Task 3 Question

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
questions = 10
answer_list = []
correct = 0
incorrect = 0
total_mark = 0
for x in range(questions):    #5. removed the -1
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    answer = num1 + num2       #3. answer not defined
    print("What is", num1, "+", num2, "?")
    user_answer = int(input())     #10 converted user_answer from string to integer
    if user_answer == answer:
        answer_list = answer_list + ["Correct"]    #1 change wrong quotation signs  #9 brought this whole line out of the if condition
        if num1 > 25 and num2 > 25:    #8 changed or to and
            total_mark = total_mark + 2
        else:
            total_mark = total_mark + 1
    else:
        answer_list = answer_list + ["Incorrect"]
list_length = len(answer_list) - 1   #2 remove minus sign      #4 bring the minus 1 out of the len() function
for i in range(list_length):
    if answer_list[i] == "Correct": #7 changed variable x to i
        correct = correct + 1    #11 changed from -1 to +1
if correct  == 1:      #6 changed message to correct
    message = "answer."
else:
    message = "answers."
print("Your total mark is", total_mark, "and you had", correct, message)