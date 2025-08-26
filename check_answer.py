names = []
marks = []
highest_pos = 0
highest_name = ""
while True:
  name = input("Student's name: ")
  names.append(name)
  while True:
    mark = int(input("Student's mark: "))
    if 0 <= mark <= 100:
      marks.append(mark)
      break
    else:
      print("Invald score. Enter number from 0 to 100.")
  
#   if mark > highest_pos:
#     highest_pos = mark
#     highest_name = name

  moreinput = input("Do you wish to add more details? (Y/N): ")
  if moreinput.upper() == 'N':
    break
student_count = len(names)
avrg = sum(marks)/student_count

highest = 0
for i in marks:
  if i > highest:
    highest = i
highest_pos = marks.index(highest)
highest_name = names[highest_pos]

print(f"There are {student_count} students.")
print(f"The average mark is {avrg}.") # round to 1 decimal place
print(f"{highest_pos} scored the highest score of {highest}.")



import math
remedial = {}

for i in range(student_count):
  if marks[i] < math.floor(avrg):
    remedial[names[i]] = marks[i]

if len(remedial) == 0:
  print("There are no students for remedial.")
else:
  
    tutor_count = (len(remedial)+3) // 3
    highest_name = names[highest_pos]
    print(f"Number of peer tutors needed: {tutor_count}")

remedial_students = 14 # len of remedial

groups = remedial_students // 3
remainder = remedial_students % 3
if remainder > 0:
  groups += 1
