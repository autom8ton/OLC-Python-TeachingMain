'''
Task 4 - 2024 Paper 2 Development of Program
Open the file PRIME.py. You will see the following function that:
· takes number as a parameter
· divides the number by 2 and converts it down to the nearest integer
· returns the result
'''
def div_2(number):
      halved = int(number/2)
      return halved

'''
Task 4.1 [5]
Extend the program by writing another function odd_or_even() that:
· takes number as a parameter
· checks whether the number is odd or even
· returns the string 'Even' if the value is even or 'Odd'
 if the value is odd.

Save your program as PRIME_2024_<your name>_<centre number>_<index number>.py [5]
'''
# Write and test your code here
#----------------------------------------------------
# Task 4.1 [5]
#----------------------------------------------------

# Start of 4.1
def odd_or_even(number):
    # even number are divisible by 2
    remainder = number % 2 

    # if there is remainder from dividing 2, it is an odd number
    if remainder == 1: 
        return "Odd" 
    else:
        return "Even"

'''
Task 4.2 [10]
A number is a prime number if it is greater than 1 and divisible by itself and 1 
For example:
·        The number 5 is a prime number because it can only be divided by 5 and 1.
·        The number 9 is not a prime number because it can be divided by 9, 3 and1.

Extend your program by writing another function prime() that:
·        takes number as a parameter
·        check whether the number is a prime number
·        returns the string  'Prime' if the number is a prime number or 'Not prime'
         if the number is not a prime number.

Your function must check the number is even by using odd_or_even(). 
If the number is even, it cannot be prime, unless it is the number 2.
To check if the number is prime, your function must check If the number 
is divisible by every integer, starting from 3, up to half of the 
number by using div_2().
There is no requirement to check values above half of the number.

Save your program.  [10]
'''
# Write and test your code here
#----------------------------------------------------
# Task 4.2 [10]
#----------------------------------------------------

# Start of 4.2
def prime(number):
    # 0 and 1 are not considered prime numbers as they cannot 
    # follow the rule where it can only: 1 * itself = itself
    if number < 2: 
        return "Not prime"
    
    # 2 is the smallest prime number, that is even
    if number == 2: 
        return "Prime"
    
    # Other than 2, all other even numbers are not prime
    if odd_or_even(number) == "Even": 
        return "Not prime"
    
    # to check if it is divisible by any number from 3 to half of the number
    for i in range(3, div_2(number) + 1): 
        # if it is fully divisible by any number, it will have remainder of 0.
        if number % i == 0: 
            return "Not prime"
    
    return "Prime"  # All other even numbers are not prime

'''
Task 4.3
Extend your program to create a user interface.
The program must:
·        allow the user only input a whole number
·        output whether there number is prime or not, by making use of the function prime()
User suitable input and output messages. Save your program. [5]
'''
# Write and test your code here
#----------------------------------------------------
# Task 4.3 [5]
#----------------------------------------------------

# Start of 4.3
# repeat asking for input if it is not valid 
while True: 
    user_input = input("Please enter a whole number to check if it is prime: ")
    
    if user_input.isdigit():
        # convert string to integer
        number = int(user_input) 

        # get the result of the number
        result = prime(number)  
        print(f"The number {number} is {result}.")
        break
    else:
        # to let user know the correct input type
        print("Invalid input. Please enter a whole number only.") 