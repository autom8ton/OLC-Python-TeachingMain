#  The task is to write a program that calculates a worker's 
# daily wages based on their working hours.
#  Time is entered in 24-hour format "HH•MM" Wages are calculated 
# in complete 1-hour blocks only - 
# workers must work the full hour to earn wages for that block. 
# The rate is $20 per #  complete hour for the first 8 hours worked, 
# and $30 per complete hour for any hours beyond 8 hours

#  Task 5.1 # [2]
#  Write a calculate_minutes ( ) function that accepts a 24-hour time parameter in the
#  format "HH:MM". The function must calculate and return the number of minutes elapsed
#  since start of day (00:00)

# "06:35"
def calculate_minutes(time):
    # variable type? string

    # how to take out the hour and minute??
    hour = time[:2]
    minute = time[3:]

    # with hour and minute, how to convert all to minutes?
    total_minutes = (int(hour) * 60 ) + int(minute)

    return total_minutes

print(calculate_minutes("06:35"))


## Task 5.2

# 09:00 to 14:00
# 08:00 to 18:00
def calculate_wage(clock_in, clock_out):
    # convert the params to minutes use calculate_minutes
    clock_in_mins = calculate_minutes(clock_in)
    clock_out_mins = calculate_minutes(clock_out)

    # calculate difference between out and in
    mins_worked = clock_out_mins - clock_in_mins

    # calculate time in 1 hour block / divide and round down
    hours_worked = mins_worked // 60

    # ot more than 8 hours
    if hours_worked > 8:
        normal = 8 * 20 # calculate normal wage
        hours_worked -= 8 # calculate overtime hours

        overtime = hours_worked * 30 # calculate overtime wage
        total_wage = normal + overtime
    # for 8 or less than
    else:
        normal = hours_worked * 20
        total_wage = normal 
    
    return total_wage

print(calculate_wage("09:00","14:00"))
print(calculate_wage("08:00","18:00"))

#########################
#Task 5.3
# check for clock_time

# Task 5.3
while True:

    while True:
        clock_in_input = input("Enter a clock in time in HH:MM format: ")

        # retrieve the hour and minute
        hour = clock_in_input[:2]
        minute = clock_in_input[3:]

        if not hour.isdigit() or not minute.isdigit():
            print("Invalid time. ")
        elif ":" not in clock_in_input:
            print("Invalid. Missing colon in time format. ")
        else:
            hour_num = int(hour)
            minute_num = int(minute)
            if  hour_num < 00 or hour_num > 23:
                print("Invalid hour. Hour must be a number between 0 and 23")
            elif minute_num < 00 or minute_num > 59:
                print("Invalid minute. minute must be a number between 0 and 59")
            else:
                # at this point, it is a correct time format
                break
            
            # check hour valid range here

    while True:
        clock_out_input = input("Enter a clock out time in HH:MM format: ")

        # retrieve the hour and minute
        hour = clock_out_input[:2]
        minute = clock_out_input[3:]

        if not hour.isdigit() or not minute.isdigit():
            print("Invalid time. ")
        elif ":" not in clock_out_input:
            print("Invalid. Missing colon in time format. ")
        else:
            hour_num = int(hour)
            minute_num = int(minute)
            if  hour_num < 00 or hour_num > 23:
                print("Invalid hour. Hour must be a number between 0 and 23")
            elif minute_num < 00 or minute_num > 59:
                print("Invalid minute. minute must be a number between 0 and 59")
            else:
                # at this point, it is a correct time format
                break

    # verify clock out is later than clock in    
    clock_out_time = calculate_minutes(clock_out_input)
    clock_in_time = calculate_minutes(clock_in_input)

    if clock_out_time < clock_in_time:
        print("clock out time must be later than clock in time")
    else:
        wage = calculate_wage(clock_in_input, clock_out_input)
        print(f"The wage for this worker is ${wage}")

        