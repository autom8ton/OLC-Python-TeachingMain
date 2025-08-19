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

# isaac 5:04 PM
# toppings = ['ham', 'cheese', 'lettuce', 'tomatoes', 'capsicum']
# top_cost = [1, 0.8, 0.5, 0.5, 0.8]
# print("Welcome to All-Health Salad Bar!")
# print("Please select your toppings below.")
# ham = int(input("Quantity of ham: "))
# cheese = int(input("Quantity of cheese: "))
# lettuce = int(input("Quantity of lettuce: "))
# tomatoes = int(input("Quantity of tomatoes: "))
# capsicum = int(input("Quantity of capsicums"))
# total_cost = ham*top_cost[0] + cheese*top_cost[1] + lettuce*top_cost[2] + tomatoes*top_cost[3] + capsicum*top_cost[4]
# print("Total cost: $", round(total_cost,1))

# while True:
#     if total_cost < 5:
#         print("Minimum order is $5.00")
#         ham = int(input("Quantity of ham: "))
#         cheese = int(input("Quantity of cheese: "))
#         lettuce = int(input("Quantity of lettuce: "))
#         tomatoes = int(input("Quantity of tomatoes: "))
#         capsicum = int(input("Quantity of capsicums: "))
#         total_cost = ham*top_cost[0] + cheese*top_cost[1] + lettuce*top_cost[2] + tomatoes*top_cost[3] + capsicum*top_cost[4]
#         print("Total cost: $", round(total_cost,1))
#         if total_cost >= 5:
#             break

# toppings = ['ham', 'cheese', 'lettuce', 'tomatoes','capsicum']
# top_cost = [1, 0.8, 0.5, 0.5, 0.8]
# print("Welcome to All-Health Salad Bar!")
# while True:
#     print("Please select your toppings below.")
#     ham = int(input("Quantity of ham: "))
#     cheese = int(input("Quantity of cheese: "))
#     lettuce = int(input("Quantity of lettuce: "))
#     tomatoes = int(input("Quantity of tomatoes: "))
#     capsicum = int(input("Quantity of capsicum: "))
#     total_cost = ham*top_cost[0] + cheese*top_cost[1] + lettuce*top_cost[2] + tomatoes*top_cost[3]
#     if ham*-1 + cheese*-0.5 + lettuce*3 + tomatoes*2.5 + capsicum*3.2:
#         total_cost -= 1
#     if total_cost < 5:
#         print('Please make an order above $5.')
#         continue
#     elif total_cost > 8:
#         print('You are entitled to a free drink.')
#     break
# print("Total cost: $", round(total_cost,1))