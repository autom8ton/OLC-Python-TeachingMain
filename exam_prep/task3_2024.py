# The program: 
# takes as the length (longest side), width (second longest side) 
#  and depth (shortest side) of the parcel 
# calculates whether the parcel is large, medium, or small 
# outputs the size of the parcel. 

# The parcel is: 
# large – if the length, width and depth are all greater than 50. 
# medium – if the length and width are greater than 50, 
#  but the depth is 50 or less. 
# small – if either the length or the width is 50 or less. 

flag = False

# parcel_size = ""
while flag == False: # 10. flag == False so loop can start
    length = float(input("What is the length of the parcel?"))
    width = float(input("What is the width of the parcel?"))
    depth = float(input("What is the depth of the parcel?"))
    if length > 50 and width > 50 and depth > 50: # 7. width instead of length
        parcel_size = "large"
    
    elif length > 50 and width > 50 and depth <= 50: #8. depth less than equal 50 #9. and conditions
        parcel_size = "medium"
    else: # 1. change elif to else
        parcel_size = "small"
    
    # 6. Code moved here so parcel size is reported first.
    print("The size of your parcel is", parcel_size) # 3. should be parcel_size

    more_parcels = input("Do you want to enter another parcel? Y or N ").upper() # 5. change to upper case to match "N" below
    if more_parcels == "N": # 2. should be double equal, #4. "N" should be string
        flag = True
