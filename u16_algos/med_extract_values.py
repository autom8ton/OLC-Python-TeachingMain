
# Scenario 1: Extracting VIP Guests from an Event RSVP List
# An event organizer maintains a list of guest ticket numbers.

# VIP guests have ticket numbers greater than 5000.
# Extract all VIP guests' ticket numbers into a new list.
# Print out all the VIP ticket numbers
guest_tickets = [1023, 5678, 4502, 8100, 3789, 5021, 6999, 2304, 4888, 5155]
# Write your code here 

# vips = []
# vipnum = 5000

# for g in guest_tickets:
#     if g > vipnum:
#         vips.append(g)

# print(vips)


##########################################################################
# Scenario 2:Extracting Priority Passengers from a Flight Check-In List
# An airline is organizing priority boarding for passengers based on their frequent flyer miles.

# Passengers with more than 50,000 miles qualify for priority boarding.
# Extract all priority passengers' frequent flyer miles into a new list.
# Print out all the miles for priority passengers
requent_flyer_miles = [12000, 67500, 48900, 72000, 53000, 26500, 88000, 34000, 15000, 59999]
# Write your code here 






##########################################################################
# Scenario 3:Filtering High Electricity Consumption in Households
# A power company monitors monthly electricity usage for different households.
# Extract households that consumed more than 500 kWh in a month 
# and store them in a separate dictionary.

# Calculate the average electricity consumption in this block

# Print a message to all these households advising them to save electricity
# Example: 
# "Unit 03-02, Electricity Consumption of 541 kwh is higher than the average of 354. "

electricity_usage = {
    "Unit 01-01": 450, "Unit 01-02": 158, "Unit 01-03": 320,
    "Unit 02-01": 700, "Unit 02-02": 550, "Unit 02-03": 400,
    "Unit 03-01": 210, "Unit 03-02": 346, "Unit 03-03": 548,
    "Unit 04-01": 235, "Unit 04-02": 536, "Unit 04-03": 650
}

# Write your code here 





##########################################################
# Scenario 4: Selecting VIP Customers Based on Purchase Amounts
# An online store tracks customer purchases and 
# identifies VIP customers who spent more than $1000 in a month.

# Extract these customers into a vip dictionary.
# Print a message to these VIP Customers that they are eligible for a Gold Card
# Example:
# "Hi Bob, you have been upgraded to VIP status and awarded a Gold Card. Congratulations!"


# Separately, Extract customers who spend below $1000 to a non_vip dictionary.
# Print a message to all of these non-vip customers, 
# informing them how much more they must spend to be a VIP member
# "Hi Charlie, spend $500 more to become a VIP member!"

customer_spending = {
    "Alice": 950, "Bob": 1200, "Charlie": 500, "Diana": 1800, "Ethan": 2200,
    "Fiona": 700, "John": 685, "Hor Kee": 1389, "Siew Ling": 235, "Matt": 452,
    "Kristen": 985, "Johnson": 785, "Charles": 2352, "Tommy": 741, "Laura": 689
}
# Write your code here 







##########################################################
# Scenario 5: Extracting Low-Stock Products from a Warehouse Inventory
# A warehouse manager is reviewing the 
# inventory stock levels of various products.

# Given a dictionary of products and their stock quantities, 
# extract all low-stock products (less than 20 units) and 
# store them in a separate dictionary.

# Print a message to the Procurement Department to buy more
# Example:
# Stock for Mouse is low at 12. Buy more.

warehouse_stock = {
    "Laptop": 35, "Mouse": 12, "Keyboard": 25,
    "Monitor": 8, "Headphones": 50, "USB-Drive": 18,
    "Tablet": 5, "Printer": 20, "MousePad": 5
}
# Write your code here 






############################################################
# Scenario 6: Filtering High-Risk Investments from a Portfolio
# A financial analyst is reviewing a list of investment stocks 
# and their volatility percentages.

# Stocks with a volatility greater than 10% are considered high-risk investments.
# Extract these high-risk investments into a new dictionary called high_risk.

# Print out a message asking the manager to sell these stocks
# Example: Tesla at 12.7% is high risk. Sell now.

investment_portfolio = {
    "Apple": 5.3, "Tesla": 12.7, "Amazon": 9.2,
    "Bitcoin": 15.6, "Google": 6.8, "Netflix": 11.4,
    "Ethereum": 18.3, "Facebook": 7.1, "Nvidia": 23.4
}
# Write your code here 




#########################################################






##################################
# Assignment
# Scenario: Identifying Star Students for an Award Ceremony
    
# Your school is preparing for the end-of-year award ceremony.
# The principal wants to recognise "Star Students" — those who have shown:
# - Excellent attendance (at least 90%)
# - Strong academic performance (score of at least 85)

# You're given two separate dictionaries:
# - One with student attendance (in %)
# - One with student scores (out of 100)

# Extract the names of students who meet both criteria.
# (1) Store them in a list called star_students.
    
# (2) Loop through the star_students list and 
#      print a congratulatory message to each star student like this:
# "Congratulations Chloe Lim! With an attendance of 95% and a score of 92,
# you are awarded the Star Student Award!""

# You may assume that the same keys exist in both dictionaries.

attendance = {
    "Alex Tan": 92, "Benjamin Lee": 88, "Chloe Lim": 95,
    "Dana Ong": 87, "Ethan Raj": 91, "Farah Bte Ahmad": 94,
    "Gerald Chan": 78, "Hannah Goh": 85, "Ivan Wong": 96,
    "Jolene Ng": 93, "Kishore Menon": 70, "Liyana Yusof": 90
}

scores = {
    "Alex Tan": 84, "Benjamin Lee": 86, "Chloe Lim": 92,
    "Dana Ong": 81, "Ethan Raj": 89, "Farah Bte Ahmad": 90,
    "Gerald Chan": 65, "Hannah Goh": 88, "Ivan Wong": 93,
    "Jolene Ng": 79, "Kishore Menon": 72, "Liyana Yusof": 85
}
