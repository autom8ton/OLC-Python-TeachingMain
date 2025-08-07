# The following program is written for a sandwich bar for customers 
# to place orders and calculate the cost of the sandwiches 
# they have ordered.

# toppings = ['ham', 'cheese', 'lettuce', 'tomatoes']
# top_cost = [1, 0.8, 0.5, 0.5]
# print("Welcome to All-Health Salad Bar!")
# print("Please select your toppings below.")
# ham = int(input("Quantity of ham: "))
# cheese = int(input("Quantity of cheese: "))
# lettuce = int(input("Quantity of lettuce: "))
# tomatoes = int(input("Quantity of tomatoes: "))
# total_cost = ham*top_cost[0] + cheese*top_cost[1] + lettuce*top_cost[2] + tomatoes*top_cost[3]
# print("Total cost: $", total_cost)

##########################################################
# Task 2.1 [3]

# Capsicum, a new topping, is added to the list of toppings and 
# will be priced at $0.80 per unit.

# Edit the program so that the new topping is available for selection and recalculate the cost.
# Cost is rounded to 1 decimal place.
##########################################################
toppings = ['ham', 'cheese', 'lettuce', 'tomatoes','capsicum']
top_cost = [1, 0.8, 0.5, 0.5, 0.8]
print("Welcome to All-Health Salad Bar!")
print("Please select your toppings below.")
ham = int(input("Quantity of ham: "))
cheese = int(input("Quantity of cheese: "))
lettuce = int(input("Quantity of lettuce: "))
tomatoes = int(input("Quantity of tomatoes: "))
capsicums = int(input("Quantity of capsicum: "))
total_cost = ham*top_cost[0] + cheese*top_cost[1] + lettuce*top_cost[2] + tomatoes*top_cost[3] + capsicums*top_cost[4]
# print("Total cost: $", round(total_cost, 2))
print(f"Total cost: ${total_cost:.2f}")


##########################################################
# Task 2.2 [2]

# Each order should be at least $5.

# Edit the program so that the user will be continually
# prompted to re-order if the selection is less than $5.

# Use appropriate input and output messages.
##########################################################

toppings = ['ham', 'cheese', 'lettuce', 'tomatoes','capsicum']
top_cost = [1, 0.8, 0.5, 0.5, 0.8]
print("Welcome to All-Health Salad Bar!")

while True:
    print("Please select your toppings below.")
    ham = int(input("Quantity of ham: "))
    cheese = int(input("Quantity of cheese: "))
    lettuce = int(input("Quantity of lettuce: "))
    tomatoes = int(input("Quantity of tomatoes: "))
    capsicums = int(input("Quantity of capsicum: "))
    total_cost = ham*top_cost[0] + cheese*top_cost[1] + lettuce*top_cost[2] + tomatoes*top_cost[3] + capsicums*top_cost[4]
    # print("Total cost: $", round(total_cost, 2))
    print(f"Total cost: ${total_cost:.2f}")

    if total_cost < 5:
        print("Your minimum order must be at least $5.00")
        print("Please re-enter your order again.")
    else:
        print("Thank you for ordering!")
        break


##########################################################
# Task 2.3 [2]

# Customers will get a free drink if the sandwich ordered costs more than $8.

# Edit the program to inform eligible customers on the free drink.

# Your program should inform the user with the following message: 
# “You are entitled to a free drink.”
##########################################################
toppings = ['ham', 'cheese', 'lettuce', 'tomatoes','capsicum']
top_cost = [1, 0.8, 0.5, 0.5, 0.8]
print("Welcome to All-Health Salad Bar!")

while True:
    print("Please select your toppings below.")
    ham = int(input("Quantity of ham: "))
    cheese = int(input("Quantity of cheese: "))
    lettuce = int(input("Quantity of lettuce: "))
    tomatoes = int(input("Quantity of tomatoes: "))
    capsicums = int(input("Quantity of capsicum: "))
    total_cost = ham*top_cost[0] + cheese*top_cost[1] + lettuce*top_cost[2] + tomatoes*top_cost[3] + capsicums*top_cost[4]
    # print("Total cost: $", round(total_cost, 2))
    print(f"Total cost: ${total_cost:.2f}")

    if total_cost < 5:
        print("Your minimum order must be at least $5.00")
        print("Please re-enter your order again.")
    else:
        print("Thank you for ordering!")

        if total_cost > 8:
            print("You are entitled to a free drink.")
        break



##########################################################
# Task 2.4 [3]

# Each topping is given a health score as shown below:

# Ham: -1 Cheese: -0.5 Lettuce: 3 Tomatoes: 2.5 Capsicum: 3.2

# Edit the program to calculate the health score of the purchased sandwich.

# Orders with a health score of more than 10 will be entitled to $1 discount.
##########################################################


toppings = ['ham', 'cheese', 'lettuce', 'tomatoes','capsicum']
top_cost = [1, 0.8, 0.5, 0.5, 0.8]
print("Welcome to All-Health Salad Bar!")

while True:
    print("Please select your toppings below.")
    ham = int(input("Quantity of ham: "))
    cheese = int(input("Quantity of cheese: "))
    lettuce = int(input("Quantity of lettuce: "))
    tomatoes = int(input("Quantity of tomatoes: "))
    capsicums = int(input("Quantity of capsicum: "))
    total_cost = ham*top_cost[0] + cheese*top_cost[1] + lettuce*top_cost[2] + tomatoes*top_cost[3] + capsicums*top_cost[4]
    # print("Total cost: $", round(total_cost, 2))
    print(f"Total cost: ${total_cost:.2f}")

    # check if order hits minimum cost
    if total_cost < 5:
        print("Your minimum order must be at least $5.00")
        print("Please re-enter your order again.")
    else:
        print("Thank you for ordering!")

        # check if eligible for free drink
        if total_cost > 8:
            print("You are entitled to a free drink.")

        # calculate health score
        health_score = (ham * -1) + (cheese * -0.5) + (lettuce * 3) + (tomatoes*2.5) + (capsicums * 3.2)

        if health_score > 10:
            total_cost = total_cost -1
            print(f"Your meal score is {health_score}, and is healthy! ")
            print("You get a $1 discount.")
            print(f"Your Total Cost is :${total_cost:.2f} ")
        
        # minimum order reach, so you break anyway
        break