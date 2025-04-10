###########################################################
# Scenario 6: Processing Customer Data from a CRM System

# You are working on a Customer Relationship Management (CRM) system 
# that stores customer records as a single raw string.

# Each record contains:
# - Customer Name followed by a semicolon (;).
# - Phone Number (8-digit number) immediately after the semicolon.
# - Records are separated by a comma (,).

# Your task is to:
# - Part 1: Extract individual customer records from the raw string 
#           and store them in a list.

# expected output
# ["Alice Johnson;98653263", "Catherine Lee;89653215", "Johnson Lam;95321453",
#     "Brandon Tan;81234567", "Emily Wong;92345678", "Hafiz Zaid;85678912",
#     "Isabelle Ng;96541234", "Ken Lim;97865432", "Noraini Ahmad;88776655",
#     "Samuel Chan;90123456"]


# - Part 2: Convert the list in part 1 into a dictionary, where:
# -   Customer names are the keys.
# -   Phone numbers are stored as integer values.

# expected output
# {"Alice Johnson": 98653263, "Catherine Lee": 89653215, "Johnson Lam": 95321453,
#     "Brandon Tan": 81234567, "Emily Wong": 92345678, "Hafiz Zaid": 85678912,
#     "Isabelle Ng": 96541234, "Ken Lim": 97865432, "Noraini Ahmad": 88776655,
#     "Samuel Chan": 90123456 }

customers = "Alice Johnson;98653263,Catherine Lee;89653215,Johnson Lam;95321453,Brandon Tan;81234567,Emily Wong;92345678,Hafiz Zaid;85678912,Isabelle Ng;96541234,Ken Lim;97865432,Noraini Ahmad;88776655,Samuel Chan;90123456"


# write your code for part 1 here
custlist = []
delimiter = ","

currentpos = 0

while True:
    # find the position of the delimiter
    delimpos = customers.find(delimiter, currentpos)

    if delimpos == -1:
        cust = customers[currentpos:] # retrieve the last value
        custlist.append(cust)
        break

    # slice out the word from the string using slicing
    cust = customers[currentpos:delimpos]
    print(cust)

    # add this customer to the list
    custlist.append(cust)

    # change currentpos to prepare for the customer
    currentpos = delimpos + len(delimiter)

# print(custlist)


# write your code for part 2 here
custdict = {}

for thiscust in custlist:
    print(thiscust)

    separatorpos = thiscust.find(";") # return me the position of the semicolon

    # name
    name = thiscust[:separatorpos] # from start until separator

    # phone number
    phone = thiscust[separatorpos+1:] # from separator +1 until the end

    # add to the dictionary
    custdict[name] = int(phone)

print(custdict)