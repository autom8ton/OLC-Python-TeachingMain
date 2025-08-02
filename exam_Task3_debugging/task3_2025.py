# The following program should check who can ride the 
# roller coaster using the following rules:  

# • age over seven years  
# • age not more than 70 years  
# • height greater than 1.3 metres.  

# The program calculates the number of people who ride 
# the roller coaster and the number rejected. 
# The program finishes when an age of zero or a 
# height of zero is input. The number of people who ride
# the roller coaster and the number of people rejected are then printed out.

age = 0
height = float(0)  #??
rejected = 0 # 3. starting value should be 0, not 100
rider = 0
age = int(input("Please enter your age ")) # 1. Missing Quotation
height = float(input("Please enter your height ")) 
while age != 0 and height != 0: #2.  should be !=, not <>

    if age <= 7 or age > 70 or height <= 1.3:  # 6. age < 7 will include age 7
        if age <= 7: # 6. age < 7 will include age 7
            print("You are too young to ride") 
        if age > 70: # 5. age check is above 70
            print("You are too old to ride") 
        if height <= 1.3:
            print("You are too short to ride") 
        rejected = rejected + 1 #8. rejected -1 is wrong
    else: # 4. indentation error. this is for if condition
        print("You can ride the Roller Coaster") 
        rider = rider + 1 # 7. Rider - wrong variable,

    age = int(input("Please enter your age ")) 
    height = float(input("Please enter your height "))  


print("Number of people rejected ", rider) 
print("Number of riders ", rejected)

# Original Code Backup #############
# age = 0
# height = float(0) 
# rejected = 100
# rider = 0
# age = int(input("Please enter your age ))
# height = float(input("Please enter your height ")) 
# while age <> 0 and height != 0:
#     if age < 7 or age > 70 or height <= 1.3: 
#         if age < 7:
#             print("You are too young to ride") 
#         if age > 90:
#             print("You are too old to ride") 
#         if height <= 1.3:
#             print("You are too short to ride") 
#         rejected = rejected - 1
# else:
#         print("You can ride the Roller Coaster") 
#         rider = Rider + 1
#     age = int(input("Please enter your age "))
#     height = float(input("Please enter your height ")) 
# print("Number of people rejected ", rider) 
# print("Number of riders ", rejected)


