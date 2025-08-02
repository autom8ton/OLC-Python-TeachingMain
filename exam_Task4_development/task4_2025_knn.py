'''
2025 - Task 4 Development of Program (KNN)
MOBILITY DEVICES
The serial numbers and specifications of several mobility devices 
are stored in two separate lists as shown below.
All code should have appropriate comments and 
all identifiers should be appropriately named. [4]
'''

serial_nos = ['523WR','924MN','1903MW','420QK','8421AB','92VC','292KS','32XC']

# Each item in the details list contains:
# [brand, model, type, width, length, height, max_speed]
details = [
    ['Telmo', 'Speed23', 'PMD', 0.7, 1.1, 1.33, 9],
    ['Lambo', 'Comfit1', 'PMD', 0.6, 1.15, 1.35, 8],
    ['Stylo', 'CoolD', 'PMD', 0.65, 1.2, 1.4, 10],
    ['Nimbus', 'SailX', 'PMD', 0.6, 0.95, 1.3, 9.5],
    ['Telmo', 'Coastie', 'PMD', 0.7, 1.1, 1.33, 10],
    ['Telmo', 'Wheeler5', 'PMD', 0.6, 1.0, 1.3, 9],
    ['Nimbus', 'SmooXth', 'Scooter', 0.3, 0.5, 1.5, 10],
    ['Lambo', 'Zipline', 'Scooter', 0.35, 0.6, 1.48, 10]
]

'''
Task 1.1 [3]
Create a dictionary named registered that uses 
the serial numbers as keys and their corresponding specifications as values.
'''
registered = {}
for i in range(len(serial_nos)):
    # build the dictionary using parallel lists
    registered[serial_nos[i]] = details[i]  

print(registered)

'''
Task 1.2 [1]
Delete the record for serial number '1903MW' from the registered dictionary.
'''
del(registered['1903MW'])  # remove the key-value pair
print(registered)

'''
Task 1.3 [1]
Add a new record to the registered dictionary using the serial number '999XY'.
'''
registered['999XY'] = ['Telmo', 'Roadster', 'PMD', 0.55, 1.12, 1.45, 10]
print(registered)

'''
Task 1.4 [3]
Read the file 'mobility_devices.csv' and append the new records into the 
registered dictionary. Each row contains a serial number followed by its specifications.
'''
with open('mobility_devices.csv', 'r') as fobj:
    datalist = fobj.readlines()

for d in datalist[1:]:  # skip the header row
    row = d.strip().split(',')  # convert CSV line to list
    serial = row[0]             # first value is the serial number
    specs = row[1:]             # rest are specifications
    registered[serial] = specs  # add to the dictionary

'''
Task 1.5 [5]
Use K-Nearest Neighbour (k = 1) to predict the type of a mobility device 
based on width and length. Use Euclidean distance formula.
'''
import math

# Prompt the user for input
x1width = float(input("What is the width? "))
y1length = float(input("What is the length? "))

knn = 10000  # set initial "infinite" distance
pre_type = ''  # predicted type of the closest match

# Loop through dictionary to calculate distance to each device
for mobdev in registered:
    record = registered[mobdev]
    width = float(record[3])   # get width from record
    length = float(record[4])  # get length from record

    # Euclidean distance calculation using width and length
    distance = math.sqrt((width - x1width)**2 + (length - y1length)**2)

    # If current distance is smaller, update the nearest neighbour
    if distance < knn:
        knn = distance
        pre_type = record[2]  # index 2 is the 'type' field

print(f"Based on width = {x1width} and length = {y1length}")
print(f"The predicted type is: {pre_type} (distance = {round(knn,3)})")

'''
Task 1.6 [3]
Extend the KNN algorithm to use width, length, and height 
as parameters to predict the device type.
'''
# Prompt the user for all three inputs
x1width = float(input("What is the width? "))
y1length = float(input("What is the length? "))
z1height = float(input("What is the height? "))

knn = 10000
pre_type = ''

# Loop through registered devices and calculate 3D distance
for mobdev in registered:
    record = registered[mobdev]
    width = float(record[3])
    length = float(record[4])
    height = float(record[5])

    # Euclidean distance in 3 dimensions
    distance = math.sqrt((width - x1width)**2 + 
                         (length - y1length)**2 + 
                         (height - z1height)**2)

    # Update prediction if this is the closest so far
    if distance < knn:
        knn = distance
        pre_type = record[2]

print(f"Based on width = {x1width}, length = {y1length}, and height = {z1height}")
print(f"The predicted type is: {pre_type} (distance = {round(knn,3)})")