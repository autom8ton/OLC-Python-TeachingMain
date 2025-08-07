toppings = ['ham', 'cheese', 'lettuce', 'tomatoes']
top_cost = [1, 0.8, 0.5, 0.5]
print("Welcome to All-Health Salad Bar!")
print("Please select your toppings below.")
ham = int(input("Quantity of ham: "))
cheese = int(input("Quantity of cheese: "))
lettuce = int(input("Quantity of lettuce: "))
tomatoes = int(input("Quantity of tomatoes: "))
total_cost = ham*top_cost[0] + cheese*top_cost[1] + lettuce*top_cost[2] + tomatoes*top_cost[3]
print("Total cost: $", total_cost)