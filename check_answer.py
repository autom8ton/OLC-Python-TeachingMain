# -------------------------------------------------
# Task 5.5

# Start of 5.1 Code
def total_cost(cost):
    tax = cost * 0.09 # calculate the tax of 9%
    total = cost + tax

    return total


print(total_cost(100))

# Start of 5.2 Code
def discount(cost):
    cost = total_cost(cost) # calculate the tax

    if cost >= 50 and cost < 100:
        discounted = 0.05 * cost
        
    elif cost >= 100:
        discounted = 0.1 * cost
    else:
        discounted = 0

    cost = cost - discounted # apply the discount first

    return cost

print(discount(100))


# Start of 5.3 Code
def reward_points(total_cost_with_discount):

    # round down then multiply by 3
    reward = int(total_cost_with_discount) * 3

    return reward

# Start of 5.4 Code
def voucher(total_cost_with_discount, customer_first_name):
    if total_cost_with_discount > 25 and total_cost_with_discount <= 50:
        voucher_code = f"{customer_first_name[:3]}05PERCENT"
    elif total_cost_with_discount > 50:
        voucher_code = f"{customer_first_name[:3]}10PERCENT"
    else:
        voucher_code = None

    return voucher_code

# Start of 5.5 code
fname = input("Enter Customer's First Name: ")
cost_of_sale = float(input("Enter the cost of sale: ")) # convert to float

print("-"*30)
print("Receipt")

print(None)

total_cost_of_sale = total_cost(cost_of_sale)
print(f"Total cost of sale: ${round(total_cost_of_sale, 2)}")

discounted_cost = discount(cost_of_sale)
print(f"Discounted cost of sale: ${round(discounted_cost,2)}")

rewards = reward_points(discounted_cost)
print(f"Rewards received: {rewards}")

vcode = voucher(discounted_cost, fname)
if vcode == None:
    print("You need to spend over $25 for a voucher code.")
else:
    print(f"Your Voucher Code is {vcode}")

    with open("vouchercode.txt", "w") as fobj:
        fobj.write(vcode)

print("Thank you for shopping. Bye!")
print("-"*30)