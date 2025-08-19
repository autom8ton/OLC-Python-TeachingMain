# Task 4.1 [3] 

# Save your program as ENTERDATA_class>_<index number>_<your name>.py  
# In the same program, write a function enter_data() 
# which asks the user to enter a binary data packet. 
# Output a suitable error message if the binary 
# data packet is not made up of only '0's or '1's. 
# 
# Repeatedly ask the user to re-enter until it does. 
# Return the valid binary number. [3]  

# Sample executions: 
# >>> print(enter_data())
# Enter a binary data packet: 0020110  
# Data packet should consists of only '0's or '1's.  
# Enter a binary data packet: #bn0110  
# Data packet should consists of only '0's or '1's.  
# Enter a binary data packet: 0011011  
# 0011011  

# Save your program. 
def enter_data():
    
    while True:
        validbin = True
        testbin = input("Enter a binary data packet: ")

        for num in testbin:
            if num not in "01":
                print("Data packet should consists of only '0's or '1's.")
                validbin = False
                break
        
        if validbin:
            # print(testbin)
            return testbin

# enter_data()


# Task 4.2 [3] 

# In the next code cell, write a function count_ones(d), 
# which counts the number of '1's in the d argument. 
# Return the count of 1s from the function. [3] 

# Sample executions:  
# >>> count_ones('0011101')  
# 4  
# >>> count_ones('00000000')  
# 0  

# Save your program. 
def count_ones(d):
    count1 = 0

    for char in d:
        if char == "1":
            count1 += 1

    # print(count1)
    return count1

# count_ones('0011101')

############
# Task 4.3 [4] 

# In the next code cell.
# Use the count_ones(d) function to write a 
# function add_bit(d,oddeven), which decides 
# whether to append a '1' or a '0' to the d argument 
# depending on whether the oddeven argument 
# is 'odd' or 'even' using the following criteria: 

# Number of 1s in the d argument | oddeven argument | Character to append
# odd                            | 'odd'            | '0'
# even                           | 'odd'            | '1'
# odd                            | 'even'           | '1'
# even                           | 'even'           | '0'
# [4] 

# Sample executions:  
# >>> add_bit('0011101','odd')  
# 00111011  
# >>> add_bit('0011101','even')  
# 00111010  
# >>> add_bit('0000000','odd')  
# 00000001  
# >>> add_bit('0000000','even')  
# 00000000 

def add_bit(d, oddeven):
    num1s = count_ones(d)

    if oddeven == 'odd':
        if num1s % 2 == 0:
            d+="1"          
        else:
            d+="0"
    else:
        if num1s % 2 == 0:
            d+= "0"
        else:
            d+="1"
    
    # print(d)
    return d

add_bit('0011101','odd') 
add_bit('0011101','even')
add_bit('0000000','odd')
add_bit('0000000','even') 