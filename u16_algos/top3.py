
# Scenario 1: Finding Gold, Silver, and Bronze in a 200m Sprint (Using a List)
# You cannot use any in-built functions to do this.

# A sports coach has recorded race completion times (in seconds) 
# for 15 athletes in a 200m sprint event. 
# The fastest times (lowest values) win the medals.

# - Identify the Gold, Silver, and Bronze medalists.
# - Print their times and their original positions in the list.

#Expected Output
# Gold Medalist: 19.5 seconds (Index: 12)
# Silver Medalist: 19.6 seconds (Index: 8)
# Bronze Medalist: 19.7 seconds (Index: 4)

race_times = [20.4, 19.9, 21.3, 20.1, 19.7, 22.0, 21.8, 20.8, 
              19.6, 23.5, 21.2, 22.5, 19.5, 20.6, 21.1]
# Write your code here
# sorted_race_time = sorted(race_times)
# print(sorted_race_time[0])
# print(sorted_race_time[1])
# print(sorted_race_time[2])

# Initialize top 3 positions with high values
gold_time = race_times[0]   # Fastest time
silver_time = race_times[0] # Second fastest
bronze_time = race_times[0] # Third fastest

gold_index = 0
silver_index = 0
bronze_index = 0

# Loop through the race times to find the top 3
for i in range(len(race_times)): # help me to find the lane number
    time = race_times[i]
    
    if time < gold_time:  
        # New fastest time found
        bronze_time = silver_time  # Previous silver becomes bronze
        bronze_index = silver_index

        silver_time = gold_time  # Previous gold becomes silver
        silver_index = gold_index

        gold_time = time  # Update new gold
        gold_index = i

    elif time < silver_time:  
        # New second-fastest time found
        bronze_time = silver_time  # Previous silver becomes bronze
        bronze_index = silver_index

        silver_time = time  # Update new silver
        silver_index = i

    elif time < bronze_time:  
        # New third-fastest time found
        bronze_time = time  
        bronze_index = i

# Print results
print(f"Gold Medalist: {gold_time} seconds (Lane Position: {gold_index+1})")
print(f"Silver Medalist: {silver_time} seconds (Lane Position: {silver_index+1})")
print(f"Bronze Medalist: {bronze_time} seconds (Lane Position: {bronze_index+1})")






#######################################################################

# Scenario 2: Finding the Top 3 Scores in a Programming Competition (Using a List)
# You cannot use any in-built functions to do this.

# A coding competition ranks students based on their final scores. 
# The top 3 highest scores win prizes.

# - Identify the top 3 scores.
# - Print their values and original positions in the list.

# Expected output
# 1st Place: 100 (Index: 12)
# 2nd Place: 99 (Index: 11)
# 3rd Place: 98 (Index: 4)


# List of programming competition scores
competition_scores = [95, 87, 92, 90, 98, 85, 88, 91, 96, 89, 94, 99, 100, 97, 93]
# Write your code here







#######################################################################
# Scenario 3: Identifying the Top 3 Best-Selling Products (Using a Dictionary)
# You cannot use any in-built functions to do this.
# A retail company tracks monthly sales for different products.

# - Identify the 3 best-selling products based on the number of units sold.
# - print the position and the units sold

# Expected output
# 1st Best-Selling Product: Smartphone (230 units sold)
# 2nd Best-Selling Product: Headphones (210 units sold)
# 3rd Best-Selling Product: Smartwatch (190 units sold)


# Dictionary of product sales data (units sold)
sales_data = {
    'Laptop': 150, 'Smartphone': 230, 'Tablet': 180, 'Monitor': 170, 
    'Keyboard': 140, 'Mouse': 130, 'Headphones': 210, 'Smartwatch': 190, 
    'Printer': 120, 'Camera': 160
}
# Write your code here







#######################################################################
# Scenario 4: Identifying the Top 3 Swimmers in a National Championship 
# You cannot use any in-built functions to do this.

# A swimming competition ranks athletes based on their 
# 100m freestyle times (in seconds). 

# The fastest times (lowest values) win.
# - Identify the top 3 fastest swimmers and their swim time.

#Expected output
# 1st Place: Caeleb (46.9 seconds)
# 2nd Place: Florent (47.5 seconds)
# 3rd Place: Michael (47.8 seconds)

# Dictionary of swimmers' 100m freestyle times (lower times are better)
swimming_times = {
    'Michael': 47.8, 'Ryan': 48.2, 'Joseph': 49.5, 'Nathan': 48.0, 
    'Kyle': 47.9, 'Caeleb': 46.9, 'Bruno': 48.7, 'Chad': 49.1, 'Florent': 47.5
}
# Write your code here







#######################################################################
# Scenario 5: Finding the Top 3 Most Expensive Cars 
# You cannot use any in-built functions to do this.

# A luxury car dealership wants to identify the three 
# most expensive cars in their inventory.
# Extract the top 3 highest-priced cars and their price

# expected output
# 1st Most Expensive Car: Bugatti Chiron ($3000000)
# 2nd Most Expensive Car: Ferrari SF90 ($625000)
# 3rd Most Expensive Car: Lamborghini Aventador ($507000)


# Dictionary of car prices
car_prices = {
    'Ferrari SF90': 625000, 'Lamborghini Aventador': 507000, 'Porsche 911 GT3': 200000,
    'McLaren 720S': 315000, 'Rolls Royce Ghost': 345000, 'Bugatti Chiron': 3000000,
    'Aston Martin DBS': 316000, 'Bentley Continental GT': 250000, 'Maserati MC20': 230000
}
# Write your code here






###################################################################