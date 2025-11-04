# Task 4.1

visitors = [145,209,198,175,223,310,285]

# total visitors? 
total_visitors = sum(visitors)

# average ?
avgnum = total_visitors / len(visitors)

# max ?
max_visitors = max(visitors)

# min ?
min_visitors = min(visitors)

stats_dic = {"total":total_visitors,
             "average": avgnum,
             "max":max_visitors,
             "min":min_visitors}

# Task 4.2
def find_busy_days(visitors):
    # visitors is the list
    busy = []

    for days in visitors:
        if days > stats_dic["average"]:
            busy.append(days)   
    
    return busy

print(find_busy_days(visitors))

a = stats_dic["total"]
# Task 4.3
print("=== Weekly Website Analysis ===")
print(f"Total Visitors: {stats_dic['total']}")
print(f"Daily Average: {stats_dic['average']}")
print(f"Highest daily traffic: {stats_dic['max']}")
print(f"Lowest daily traffic: {stats_dic['min']}")

print(f"Busy days (above average): {find_busy_days(visitors)}")