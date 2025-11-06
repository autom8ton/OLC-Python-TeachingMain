# shapes_no = 5
# for i in range(shapes_no):
#     no_of_sides = int(input("Please enter the number of sides the shape has: "))
#     angles_sum = (no_of_sides - 2) * 180
#     print("Sum of angles with", no_of_sides, "sides = ", angles_sum, "degrees")


#Task 2

# student_scores is a global variable
student_scores = {
    'susan123':85,
    'randy329':92,
    'mike671':78
    }

# # retrieve value from dictionary
# val_susan = student_scores['susan123']
# print(val_susan)

# # add to dictionary
# student_scores["manuel"] = 68
# print(student_scores)

# # change the value of a key
# student_scores["manuel"] = 88
# print(student_scores)

# # check if a key exist in dictionary
# if "mike671" in student_scores:
#     print("student exists")
# else:
#     print("student does not exist")

def add_student(username, score):
    if username in student_scores:
        print("Username already exists")
    else:
        student_scores[username] = score
        print('Added {} with score {}'.format(username, score))

add_student("mike671", 98)
print(student_scores)

def display_all():
    for username in student_scores:
        print(username,student_scores[username])

def edit_score(username, newscore): 
    if username in student_scores:
        student_scores[username] = newscore




###################### Ask the user for 

def prime(number):
    #n = int(input("Enter a number"))
    # divide_count = 0
    isprime = True
    for i in range(2, number):
        if number % i == 0:
            # divide_count += 1
            isprime = False

    return isprime

def mersenne_prime(number):
    isprime = prime(number)
    ismersenne = False

    # loop through from 
    for i in range(2, number):
        if prime(i):
            if number == 2**i - 1:
                ismersenne = True
                break

    if isprime and ismersenne:
        return True
    else:
        return False

print(mersenne_prime(3))
print(mersenne_prime(5))
print(mersenne_prime(7))