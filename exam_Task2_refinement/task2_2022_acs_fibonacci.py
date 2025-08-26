# Task 2 
# A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8.... 
# The first two terms are 0 and 1. 
# All other terms are obtained by adding the preceding two terms. 
# The following program outputs the first five terms in the Fibonacci sequence. 

# n1 = 0 
# n2 = 1 
# nterms = 5 
# for i in range(nterms): 
#     print(n1) 
#     nth = n1 + n2 
#     n1 = n2 
#     n2 = nth 

###########################################################
# 6. Edit the program so that it works for any number of terms. 
# The program must display a suitable input message.
# [1]
###########################################################
# Copy + Paste & Write your code here

n1 = 0 
n2 = 1 
# Task 2.6 work for any terms
# nterms = 5 
nterms = int(input("How many terms should this be run for? "))
for i in range(nterms): 
    print(n1) 
    nth = n1 + n2 
    n1 = n2 
    n2 = nth 


###########################################################
# 7. Edit the program to only accept a positive integer to be input. 
# A suitable error message must be displayed if the nterms 
# is not in the range. The program must loop until a valid nterms is input.
# [3]
###########################################################
# Copy + Paste & Write your code here

n1 = 0 
n2 = 1 
# Task 2.6 work for any terms
# nterms = 5 

# Task 2.7 - check for positive integer
while True:
    nterms = int(input("How many terms should this be run for? "))

    if nterms > 0:
        break
    else:
        print(f"{nterms} is not valid.")
        print("Terms must be a positive integer only.")

for i in range(nterms): 
    print(n1) 
    nth = n1 + n2 
    n1 = n2 
    n2 = nth 



###########################################################
# 8. Edit the program to store the Fibonacci sequence in a list. 
# Display the list at the end of program.
# [3]
###########################################################
# Copy + Paste & Write your code here

fnumbers = [] # list for fibonacci numbers
n1 = 0 
n2 = 1 
# Task 2.6 work for any terms
# nterms = 5 

# Task 2.7 - check for positive integer
while True:
    nterms = int(input("How many terms should this be run for? "))

    if nterms > 0:
        break
    else:
        print(f"{nterms} is not valid.")
        print("Terms must be a positive integer only.")

for i in range(nterms): 
    fnumbers.append(n1) # Task 2.8
    print(n1) 
    nth = n1 + n2 
    n1 = n2 
    n2 = nth 

print(fnumbers) # Task 2.8

###########################################################
# 9.
# Edit the program to allow user to input another positive integer 
# and display if the integer is in the first hundredth terms of 
# the Fibonacci sequence. You do not need to validate the input.
# [3]
###########################################################
# Copy + Paste & Write your code here

checknum = int(input("Enter a number to check if it is within first 100 fibonacci numbers: "))

fnumbers = [] # list for fibonacci numbers
n1 = 0 
n2 = 1 
# Task 2.6 work for any terms
nterms = 100

# Task 2.7 - check for positive integer
# while True:
#     nterms = int(input("How many terms should this be run for? "))

#     if nterms > 0:
#         break
#     else:
#         print(f"{nterms} is not valid.")
#         print("Terms must be a positive integer only.")

for i in range(nterms): 
    fnumbers.append(n1) # Task 2.8
    print(n1) 
    nth = n1 + n2 
    n1 = n2 
    n2 = nth 

print(fnumbers) # Task 2.8

if checknum in fnumbers:
    print(f"{checknum} is within the first 100 fibonacci numbers.")
else:
    print(f"{checknum} is not within the first 100 fibonacci numbers.")
