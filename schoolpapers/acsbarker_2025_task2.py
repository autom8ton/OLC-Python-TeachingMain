"""
The task is to edit program code that generates unique library accounts, 
manages secure PIN creation, and validates user authentication for a school library system.

The following program creates a digital library ID for a student. 
It creates the ID using the student's name and automatically 
generates a 4-digit access PIN for library services
"""

# from random import randint
# firstname = input("Enter first name: ")
# lastname = input("Enter last name: ")
# library_id = firstname + lastname
# print("Library ID is " + library_id)
# pin = ""
# for i in range(4):
#     pin += str(randint(0,9))
# print("PIN is " + pin)


"""
Task 2.1 
Edit the program so that: 

[3]
(a) the library ID follows this format:
>>  Takes the first letter of the first name
>>  Takes the last three letters of the last name
>>  Adds "2025" at the end
>>  Converts the library ID to uppercase 
Example: If first name is 'John' and last name is "Smith", 
ID should be "JITH2025" 
"""
####################################################
# Task 2.1 a
# from random import randint
# firstname = input("Enter first name: ")
# lastname = input("Enter last name: ")
# library_id = firstname[0] + lastname[-3:]+"2025"
# library_id = library_id.upper()
# print("Library ID is " + library_id)
# pin = ""
# for i in range(4):
#     pin += str(randint(0,9))
# print("PIN is " + pin)




"""
[1]
(b) the generated PIN is 6-digits 
    instead of 4-digits.
"""
####################################################
# Task 2.1 b
# from random import randint
# firstname = input("Enter first name: ")
# lastname = input("Enter last name: ")
# library_id = firstname[0] + lastname[-3:]+"2025"
# library_id = library_id.upper()
# print("Library ID is " + library_id)
# pin = ""
# for i in range(6):
#     pin += str(randint(0,9))
# print("PIN is " + pin)




"""
Task 2.2 [6]
The program needs to ensure that the student confirms their library PIN for security purposes.
Edit the program to implement PIN verification:
• ask the student to enter the PIN after the display of the generated PIN
• if PIN entries match, output "Library account activated!" and end the program
if PIN doesn't match, display "PIN not verified! New PIN generated." and
generate a new PIN. Allow the student to try again.
•  Limit PIN entry attempts to 3 tries before displaying "Inactive account!" and
ending the program.

Suitable output messages must be used.
"""
####################################################
# Task 2.2

from random import randint
firstname = input("Enter first name: ")
lastname = input("Enter last name: ")
library_id = firstname[0] + lastname[-3:]+"2025"
library_id = library_id.upper()
print("Library ID is " + library_id)
pin = ""


attempts = 0
while True:
    pin = ""
    for i in range(6):
        pin += str(randint(0,9))
        print("PIN is " + pin)

    pin2 = input("Enter the PIN again to verify: ")
    if pin == pin2:
        print("Library account activated!")
        break
    else:
        attempts += 1
        if attempts == 3:
            print("Inactive account!")
            break
        else:
            print("PIN not verified! New PIN generated.")

        
