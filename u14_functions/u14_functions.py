
###################################################
# Part 1: Learning Exercises

# Exercise 1: A Simple Function
# Define a function that prints "Hello, World!" and call it.

def greet():
    print("Hello World")







#------------------------------------------------------------
# Exercise 2: Function with One Parameter
# Define a function that takes a name as a parameter and greets the user.

def hello(name):
    print(f"Hello {name}")

# hello("John")
# hello("Mary")
# hello("Desmond")


#------------------------------------------------------------
# Exercise 3: Function with Two Parameters
# Define a function that takes two numbers and prints their sum.

def area_triangle(base, height):

    area = 0.5 * base * height
    print(f"Area of Triangle of base {base} and height {height} is {area}")

# area_triangle(45, 69)
# area_triangle(234, 654)
# area_triangle(123, 6564)

#------------------------------------------------------------
# Exercise 4: Function with a Return Value
# Define a function that calculates the area of a rectangle.

def area_triangle(base, height):

    area = 0.5 * base * height
    # print(f"Area of Triangle of base {base} and height {height} is {area}")

    return area

# scenario: you have 10 rectangles
# you need to find the total area of 10 rectangles

triangle1 = area_triangle(45, 69)
triangle2 = area_triangle(234, 654)
triangle3 = area_triangle(123, 6564)

total = triangle1 + triangle2 + triangle3


#------------------------------------------------------------
# Exercise 5: Using Returned Values in Further Computations
# Define a function that calculates the perimeter of a rectangle.
def peri_rect(length, breadth):
    peri = (length + breadth) * 2 

    return peri

rect1 = peri_rect(54,21)
# print(rect1)



#------------------------------------------------------------
# Exercise 6: Demonstrating Local and Global Variables
# Define a function that modifies a local variable.
# def local_variable_example():
#     x = 10  # Local variable
#     print("Inside the function, x is {}".format(x))

# # Outside the function.
# x = 20  # Global variable
# local_variable_example()
# print("Outside the function, x is {}".format(x))

# num1 = 10

# def dosomething(var1):
#     print(var1)

# print(num1)

# dosomething(20)


#------------------------------------------------------------



# Exercise 7: Greeting Multiple Users
# Write a function that takes a list of names and greets each one.


# Call the function with a list of names.
# greet_users(["Alice", "Bob", "Charlie"])

def greet(names): # assume names is a list
    for n in names:
        print(f"Hello {n}")

students = ["Alice", "Bob","John"]
greet(students)