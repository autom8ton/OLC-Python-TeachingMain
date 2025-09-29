# Task 2 - Refinement of Program (10 marks)
# You are given a Python program that classifies mobility devices 
# using the k-Nearest Neighbour (k = 1) method. 
# Each device is represented with two features: width and length. 
# You are to refine the given program by completing the tasks below.

import math

#### do not change this code 
devices = {
    "523WR": ["Telmo",  "Speed23",  "PMD",     0.70, 1.10],
    "924MN": ["Lambo",  "Comfit1",  "PMD",     0.60, 1.15],
    "32XC" : ["Lambo",  "Zipline",  "Scooter", 0.35, 0.60],
    "A101X": ["Volt",   "Feather",  "Scooter", 0.32, 0.52],
    "D404Q": ["RoadMax","Urban",    "PMD",     0.66, 1.18],
}

print("Mobility Device Classifier (kNN, k = 1)")
print("Total devices loaded:", len(devices))
#### do not change this code 

# Task 2.1 - Complete the function below
def distance2(p1x, p1y, p2x, p2y):
    # Task 2.1 – To be completed by student
    pass # remove this and replace with code.


# Task 2.2 - Complete the function below
def predict_type_2d(devices_dict, newdevice_width, newdevice_length):
    # Task 2.2 – To be completed by student
    pass # remove this and replace with code. 

# --- main flow (to be refined by you) ---
# Students will add input validation and output formatting later


# ________________________________________
# Task 2.1 [3 marks]
# Complete the function distance2(p1x, p1y, p2x, p2y) so that it 
# calculates and returns the Euclidean distance between the two points.

# Arguments:
# •	p1x: First point x coordinate (float).
# •	p1y: First point y coordinate (float).
# •	p2x: Second point x coordinate (float).
# •	p2y: Second point y coordinate (float).
# Returns:
# •	A float representing the Euclidean distance between the two points.

# Use the formula: math.sqrt( (p1x - p2x)**2 + (p1y - p2y)**2 )
# ________________________________________




 
# ________________________________________
# Task 2.2 [5 marks]
# Complete the function:
# predict_type_2d(devices_dict, newdevice_width, newdevice_length) 
# so that it can decide whether the new device 
# should be classified as a PMD or a Scooter.

# Arguments:
# •	devices_dict: dictionary of devices, each value is [brand, model, type, width, length].
# •	newdevice_width: width of the new device (float).
# •	newdevice_length: length of the new device (float).
# Returns:
# •	A string: the predicted type ("PMD" or "Scooter").

# Your function should make use of the distance2(...) function 
# in Task 2.1 to compare the new device against the known devices, 
# and then determine the type of the most similar device. 
# The function must finally return the predicted type as a string.
# ________________________________________





# ________________________________________
# Task 2.3 [2 marks]
# Refine the main program so that:
# •	The user is repeatedly asked to input the width 
#    until they enter a positive number.
# •	The user is repeatedly asked to input the length 
#    until they enter a positive number.
# •	Upon successful validation, call the predict_type_2d () 
#    function and print the classified type of the device. E.g.
# o	Predicted type: Scooter
# ________________________________________





########################################
######### ANSWER BELOW #################
########################################
# Task 2 - Refinement of Program (10 marks)
# You are given a Python program that classifies mobility devices 
# using the k-Nearest Neighbour (k = 1) method. 
# Each device is represented with two features: width and length. 
# You are to refine the given program by completing the tasks below.

import math

#### do not change this code 
devices = {
    "523WR": ["Telmo",  "Speed23",  "PMD",     0.70, 1.10],
    "924MN": ["Lambo",  "Comfit1",  "PMD",     0.60, 1.15],
    "32XC" : ["Lambo",  "Zipline",  "Scooter", 0.35, 0.60],
    "A101X": ["Volt",   "Feather",  "Scooter", 0.32, 0.52],
    "D404Q": ["RoadMax","Urban",    "PMD",     0.66, 1.18],
}

print("Mobility Device Classifier (kNN, k = 1)")
print("Total devices loaded:", len(devices))
#### do not change this code 

# Task 2.1 - Complete the function below
def distance2(p1x, p1y, p2x, p2y):
    # Task 2.1 – To be completed by student
    pass # remove this and replace with code.


# Task 2.2 - Complete the function below
def predict_type_2d(devices_dict, newdevice_width, newdevice_length):
    # Task 2.2 – To be completed by student
    pass # remove this and replace with code. 

# --- main flow (to be refined by you) ---
# Students will add input validation and output formatting later


# ________________________________________
# Task 2.1 [3 marks]
# Complete the function distance2(p1x, p1y, p2x, p2y) so that it 
# calculates and returns the Euclidean distance between the two points.

# Arguments:
# •	p1x: First point x coordinate (float).
# •	p1y: First point y coordinate (float).
# •	p2x: Second point x coordinate (float).
# •	p2y: Second point y coordinate (float).
# Returns:
# •	A float representing the Euclidean distance between the two points.

# Use the formula: math.sqrt( (p1x - p2x)**2 + (p1y - p2y)**2 )
# ________________________________________
def distance2(p1x, p1y, p2x, p2y):

    distance = (p1x - p2x)**2 + (p1y - p2y)**2
    distance = math.sqrt(distance)
    return distance



 
# ________________________________________
# Task 2.2 [5 marks]
# Complete the function:
# predict_type_2d(devices_dict, newdevice_width, newdevice_length) 
# so that it can decide whether the new device 
# should be classified as a PMD or a Scooter.

# Arguments:
# •	devices_dict: dictionary of devices, each value is [brand, model, type, width, length].
# •	newdevice_width: width of the new device (float).
# •	newdevice_length: length of the new device (float).
# Returns:
# •	A string: the predicted type ("PMD" or "Scooter").

# Your function should make use of the distance2(...) function 
# in Task 2.1 to compare the new device against the known devices, 
# and then determine the type of the most similar device. 
# The function must finally return the predicted type as a string.
# ________________________________________

def predict_type_2d(devices_dict, newdevice_width, newdevice_length):
   
    min_distance = math.inf
    min_type = ""
    for device, specs in devices_dict.items():
        current_width = specs[3]
        current_length = specs[4]
        current_type = specs[2]

        distance = distance2(newdevice_width,  newdevice_length, current_width, current_length)

        if distance < min_distance:
            min_distance = distance
            min_type = current_type

    return min_type



# ________________________________________
# Task 2.3 [2 marks]
# Refine the main program so that:
# •	The user is repeatedly asked to input the width 
#    until they enter a positive number.
# •	The user is repeatedly asked to input the length 
#    until they enter a positive number.
# •	Upon successful validation, call the predict_type_2d () 
#    function and print the classified type of the device. E.g.
# o	Predicted type: Scooter
# ________________________________________
while True:
    w = float(input("Enter width (m): "))

    if w < 0:
        print("width must be a valid positive number.")
    else:
        break

while True:
    l = float(input("Enter length (m): "))
    if l < 0:
        print("length must be a valid positive number.")
    else:
        break

result = predict_type_2d(devices, w, l)
print(f"Predicted type: {result}")




