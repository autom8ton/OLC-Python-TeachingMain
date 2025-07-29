# Subjects = ["English", "Chinese", "E math", "A math", "Chemistry", "physics", "Biology", "Geography", "History", "Literature", "Social Studies",
#             "Computing", "Art", "Music", "FCE"]

# subject_taken = input("Enter the subjects taken and separate each subject with commas: ").split(",")
# subject_grades = input("Enter the grades for the subjects and separate each grade with commas: ").split(",")
# #for sub, grade in (subject_taken, subject_grades):
# #  print(f"subject: {sub}, grade: {grade}")
# t = {}
# for i in range(len(subject_taken)):
#   t[subject_taken[i]] = subject_grades[i]
# print(t)
# Subjects = ["English", "Chinese", "E math", "A math", "Chemistry", "physics", "Biology", "Geography", "History", "Literature", "Social Studies",
#             "Computing", "Art", "Music", "FCE"]



# subject_taken = input("Enter the subjects taken and separate each subject with commas: ").split(",")
# subject_grades = input("Enter the grades for the subjects and separate each grade with commas: ").split(",")
# t = {}
# for i in range(len(subject_taken)):
#   t[subject_taken[i]] = subject_grades[i]
# print(t)

# Store the R5 - related subjects in 1 list (for validation)
r5subs = ["E MATH","A MATH", "CHEMISTRY","PHYSICS", "BIOLOGY", "GEOGRAPHY", "HISTORY",
          "LITERATURE","SOCIAL STUDIES", "COMPUTING", "ART", "MUSIC", "FCE"]

# Store the L1 - related subjects in 1 list (for validation)
l1subs = ["ENGLISH", "CHINESE"]
grades = ["A1", "A2", "B3", "B4", "C5", "C6", "D7", "E8", "F9"]

# Use 2 empty dictionaries
l1subject_score = {} # use this to store the l1 score
r5subject_score = {} # use this to store the r5 scores for each subject.

l1count = 0 # count for at least 1 language
r5count = 0 # count for at least 5 subjects

# Validates if the subject in question is a proper subject
def validate(question, validlist):
  while True:
    output = input(question).upper()
    if output in validlist:
      return output
    else:
      print("Only the below values are accepted. ")
      for i in validlist:
        print(i)

# ask user to input 1 language subject. Store subject and grade into l1subject_score variable
while True:
  print("\n********************")
  print("Enter at least 1 L1 Subject")
  print(f"L1 Subject Count: {l1count}\n")
  l1subject = validate("Enter a L1 Language Subject: ", l1subs)

  ### need to do validation for the inputs above
  if l1subject not in l1subject_score:
    l1score = validate("Enter the grade: ", grades)
    l1subject_score[l1subject] = l1score
    l1count += 1

    # make sure at least 1 language subject
    if l1count < 2:
      proceed = input("Enter Y if you have more subjects to enter: ").upper()
      if proceed != "Y":
        break
    else:
      break
  else:
    print(f"You have already entered {l1subject}")

print(l1subject_score)

while True:
  print("\n********************")
  print("Enter at least 5 R5 Subjects")
  print(f"R5 Subject Count: {r5count}\n")
  r5subject = validate("Enter a R5 Subject: ", r5subs)
  
  ### need to do validation for the inputs above
  if r5subject not in r5subject_score:
    r5score = validate("Enter the grade: ", grades)
    r5subject_score[r5subject] = r5score
    r5count += 1 # increase the count

    if r5count >= 5:
      proceed = input("Enter Y if you have more subjects to enter: ").upper()
      if proceed != "Y":
        break
  else:
    print(f"You have already entered {r5subject}")


print(r5subject_score)

# function to select the best score by looping through grades
def selectbest(subjectscore, grades, requiredCount):

  selectedsubjects = {} # empty dictionary to hold the output
  count = 0 # used to count number of required grades

  for bestscore in grades: # loop through the grades e.g. A1 > A2 > B3

    for subject, score in subjectscore.items():
      # Look for the first subject that that is the score
      # i.e. is there any subject with A1.. or A2...
      if score == bestscore:
        selectedsubjects[subject] = score
        count += 1

        if count == requiredCount:
          return selectedsubjects

l1selected = selectbest(l1subject_score, grades, 1)
r5selected = selectbest(r5subject_score, grades, 5)

print("Your L1R5 is: ")
for subject, score in l1selected.items():
  print(f"{subject} : {score}")
for subject,score in r5selected.items():
  print(f"{subject} : {score}")


