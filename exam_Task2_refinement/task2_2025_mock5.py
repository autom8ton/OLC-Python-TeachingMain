# num_members = 15
# for x in range(num_members):
#     sport = input("What is the member's preferred sport?")

# while True:
#     sport = input("What is the member’s preferred sport?")

# ----------------------------------
# Task 5.1 [3 marks]
# ----------------------------------
# Edit the program to repeatedly prompt the organizer to enter a 
# member's preferred sport. The loop should stop when the 
# organizer enters 'done'

# Task 5.1

# while True:
#     sport = input("What is the member's preferred sport? ")
#     if sport.lower() == "done":
#         print("All sports have been entered.")
#         break




# # ----------------------------------
# # Task 5.2  [2 marks]
# # ----------------------------------
# # Edit your program to convert each sport to lowercase and 
# # then store it into a list. The loop should stop when the 
# # organizer enters 'done'


# # Task 5.2
# sports = []

# while True:
#     sport = input("What is the member's preferred sport? ").lower()
#     if sport == "done":
#         print("All sports have been entered.")
#         break
#     else:
#         sports.append(sport)


# # ----------------------------------
# # Task 5.3 [5 marks]
# # ----------------------------------
# # Ask the organizer to input a sport to search for. 
# # The program must:
# # - Handle upper/lower case input.
# # - Print the number of members who prefer that sport.
# # - Display a message if nobody likes that sport.

sports = []

while True:
    sport = input("What is the member's preferred sport? ").lower()
    if sport == "done":
        print("All sports have been entered.")
        break
    else:
        sports.append(sport)

query = input("Enter a sport to search for: ").lower()
countmembers = 0
if query in sports:

    # alternatively >> sports.count(query)
    for s in sports:
        if s == query:
            countmembers += 1

    print(f"{countmembers} members like the sport {query}.")
else:
    print(f"Nobody likes to play {query}")

