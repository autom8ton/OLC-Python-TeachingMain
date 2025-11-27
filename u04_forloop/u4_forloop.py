#######

# loop - repeats certain codes

# i for iteration
# for i in range(10):
#     print(i)

# # i want to start counting from 1 - 10

# for i in range(1, 11):
#     print(i)

# print from 23- 35

# print from 88-96

# multiples of 4 from 4 to 48
# for i in range(4, 49, 4): # start, stop and step
#     print(i)

# # print multiples of 2 from 2 to 24

# # print odd numbers from 3 to 27

# # print descending numbers from 10 to 1

# for i in range(10, 0, -1):
#     print(i)


#########################################
# create a times-table program

# ask the user to enter a number 
number = input("Enter a number: ")

for i in range(1, 13):
    # print(i)
    answer = int(number) * i # return me the answer

    print(f"{number} x {i} = {answer}")

    # print(number, " x ", i, "=", answer)

# 3 x 1 = 3
# 3 x 2 = 6
# .....
# 3 x 12 = 36

