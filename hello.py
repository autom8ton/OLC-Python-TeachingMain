


# password = "abcd"

# # for num in password: # loop through every single character in [password]
# #     print(num)

# for i in range(10):
#     print(i)

# ord() to retrieve the ordinal number for a character
# chr() to retrieve a character from a number
# 65 - 90

# number_students = int(input("Enter the number of students: "))
# passing_score = 50
# for x in range(0, number_students):
#     name = input("Name of student: ")
#     score = float(input("Score of student: "))
#     attendance = float(input("Attendance of student: "))
#     if attendance >= 75 and score < passing_score:
#         print("The student has not passed the score.")
#     if attendance <= 75 and score >= passing_score:
#         print("The student has not attended enough classes.")
#     if attendance <= 75 and score <= passing_score:
#         print("The student has not passed the score and not attended enough classes")
#     if attendance >= 75 and score >= passing_score:
#         print("The student has passed both the score and attendedance")
valid_codes = ["A1B2", "C3D4", "E5F6", "G7H8", "I9J0"]
while True:
    number = False
    letter = False
    code = input("input code: ").upper()
    if len(code) != 4:
        print('make sure its 4 chars long')
        continue
    for i in code:
        if i.isalpha():
            letter = True
        elif i.isdigit():
            number = True
    if not number or not letter:
        print('plz add number n letter')
        continue
    if code in valid_codes:
        retry = input('Reenter code.').upper()
        if retry == code:
            print('Access granted.')
            break
        else:
            print("Access denied. Please try again.")
    else:
        print("Access denied.")
