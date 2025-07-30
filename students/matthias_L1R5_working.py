
L1 = ["ENGLISH", "CHINESE"]
R5 = ["E MATH", "A MATH", "CHEMISTRY", "PHYSICS", "BIOLOGY", "GEOGRAPHY", "HISTORY", "LITERATURE", "SOCIAL STUDIES", "COMPUTING", "ART", "MUSIC", "FCE"]
grades = ["A1", "A2", "B3", "B4", "C5", "C6", "D7", "E8", "F9"]
grade_points = {"A1":1, "A2":2, "B3":3, "B4":4, "C5":5, "C6":6, "D7":7, "E8":8, "F9":9}

L1_subject_score = {}
R5_subject_score = {}

######## start of l1
L1_subject = input("Enter one subject from L1: ").upper()
while not L1_subject.upper() in L1:
    print("Invalid subject\nPlease choose a valid subject")
    L1_subject = input("Enter one subject from L1: ")

L1_score = input(f"Enter the score for {L1_subject}: ").upper()
while not L1_score in grades:
    print("Invalid score\nPlease choose a valid score")
    L1_score = input(f"Enter the score for {L1_subject}: ")
    

L1_subject_score[L1_subject] = L1_score

################ Start of R5

print("Enter five subjects from R5:")
count = 0
while count < 5:
    R5_subject = input("Enter one subjects from R5: ").upper()
    while not R5_subject.upper() in R5:
        print("Invalid Subject\n Please choose a valid subject")
        R5_subject = input("Enter one subjects from R5: ").upper()

    else:
        while R5_subject in R5_subject_score:
            print(f"{R5_subject} has already been added. ")
            R5_subject = input("Enter one subject from R5: ").upper()

    R5_score = input(f"Enter the score for {R5_subject}: ").upper()

    while not R5_score in grades:
        print("Invalid score\nPlease choose a valid score")
        R5_score = input(f"Enter the score for {R5_subject}: ").upper()
    R5_subject_score[R5_subject] = R5_score
    count += 1
    
total = L1_score + R5_score
print(total)
