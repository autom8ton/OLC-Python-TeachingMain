# for loop is like the repeat loop in scratch

# range(10), string, list, dictionary

# for i in range(10):
#     print(i)


# name = "KEIJI"

# for c in name:
#     print(f"Give me a {c}!")

# print("who is the best?!?!?!")
# print(name)

# range(stop)
# for i in range(10):
#     print(i)

# range(start, stop)
# for i in range(5,16):
#     print(i)

# range(start, stop, step)
# for i in range(4, 49, 4):
#     print(i)

# for i in range(10, -1, -1):
#     print(i)

# for i in range(10):
#     print(i)

# javascript/ C/ C++/ C#/ Java
# for (var i = 0; i < 10; i++){
#     console.log(i)
# }






# U4 - Exercise 2
# Write a program to generate the multiplication tables for
# any number.
# Example:
# Input = 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# ...

# * operator
# join statements >>> f"
# input() / print()
# range()
# for loop

# num = int(input("What is the number: "))

# for i in range(1, 13):
#     print(f"{num} x {i} = {num * i}")


# print(f"{num} x 1 = {num * 2}")
# print(f"{num} x 1 = {num * 3}")
# print(f"{num} x 1 = {num * 4}")
# print(f"{num} x 1 = {num * 5}")



# print(num * 1)
# print(num * 2)
# print(num * 3)
# print(num * 4)
# print(num * 5)
# print(num * 6)
# print(num * 7)
# print(num * 8)
# print(num * 9)
# print(num * 10)



#------------------------------------------------------------
# Exercise 11: Custom Counting Pattern
# Write a program to print the following pattern:
# 5
# 44
# 333
# 2222
# 11111

# counter algorithm 
count = 1

for i in range(5, 0, -1):  
    print(str(i) * count) 
    count = count + 1 ### same as change (count) by 1
    