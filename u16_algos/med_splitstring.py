# Practice on how to split strings based on delimiter
namestrings = "Aisha;Benny;Chloe;David;Eva;John;Laura"

delim = ";" # stores the value of the delimiter

# create an empty list
namelist = []

# create a temp string, this will hold each name temporarily
tempstring = ""

# loop through each character from the name string
for c in namestrings:

    # check if this current character is a delimiter
    if c == delim:
        # means that this character is the delimiter 
        namelist.append(tempstring)

        tempstring = "" # erase the previous name
    else:
        # this is not a delimiter
        # builds each name character by character
        tempstring = tempstring + c 
        print(tempstring)

# add the last name manually
namelist.append(tempstring)

# print the list to confirm
print(namelist)





















#### for loop

# names = ['Aisha', 'Benny', 'Chloe', 'David', 'Eva', 'John', 'Laura']

# print(names[2]) # retrieve using index (number)

# names.append("Darius") # add to the list
# print(names)

# names.remove("Chloe") # remove
# print(names)


# # find the position of the delimiter, if cannot find, returns -1
# delimpos = s.find(delim, currentpos)

# # use string slicing to pull it out
# word = s[currentpos:delimpos]
# # word = s[0:5] # slicing
# print(word)

# # add to the list
# slist.append(word)

# # update the position of currentpos to find next word
# currentpos = delimpos + len(delim)





# # slicing - way to extract parts of a string/ list into antoher string
# word = "SINGAPORE"
# # [start: stop: step] slicing syntax 
# a = word[5:]
# print(a[::-1])



# slist = s.split(";")
# print(slist)


############################################# first word done



# # Loop until all parts are extracted
# while True:
#     # Find the next occurrence of the delimiter from the current position
#     delimiter_start = s.find(delimiter, currentpos)

#     # If no more delimiters are found, add the remaining part and exit the loop
#     if delimiter_start == -1:
#         thispiece = s[currentpos:]  # Get the last substring after the final delimiter
#         parts.append(thispiece)  # Add the last piece to the list
#         break  # Exit loop

#     # Extract substring from the current position to just before the delimiter
#     thispiece = s[currentpos:delimiter_start]  
#     parts.append(thispiece)  # Add the extracted part to the list

#     # Move current position past the delimiter for the next search
#     currentpos = delimiter_start + len(delimiter)  

# # Print the final list of split parts
# print(parts)  


# while True:
#     # find the position of the separator/ delimiter ;
#     delimpos = s.find(delim, currentpos) ### returns the index of the string you are looking for

#     if delimpos == -1:
#         word = s[currentpos:]
#         wordlist.append(word)
#         break

#     # pull out the word using string slicing
#     word = s[currentpos: delimpos]
#     print(word)

#     # add this word to the list
#     wordlist.append(word)

#     # prep to pull out the next word
#     currentpos = delimpos + len(delim)

# print(wordlist)



# ipadds = "192.168.1.1,10.0.0.2,172.16.5.10,192.168.1.45,10.0.0.18,172.16.5.20,192.168.2.15,10.0.0.5,172.16.5.30,192.168.3.5,10.0.0.12,172.16.6.25,192.168.1.100,10.0.0.9,172.16.5.55,192.168.4.8,10.0.1.1,172.16.7.8,192.168.5.2,10.0.2.3,172.16.8.45,192.168.6.7,10.0.3.5,172.16.9.20,192.168.7.11,10.0.4.9,172.16.10.10,192.168.8.4,10.0.5.2,172.16.11.14,192.168.9.6,10.0.6.3,172.16.12.17,192.168.10.9,10.0.7.8,172.16.13.22,192.168.11.10,10.0.8.15,172.16.14.30,192.168.12.5,10.0.9.20,172.16.15.8,192.168.13.3,10.0.10.11,172.16.16.40,192.168.14.2,10.0.11.4,172.16.17.18,192.168.15.1,10.0.12.5"
# delim = 0
# delimiter = ","
# currentpos = 0
# sus_ips = []
# delim = ipadds.find(delimiter, currentpos)
# while True:
#     if delim == -1:
#         sus_ips.append(ipadds[currentpos:])
#         break
#     else:
#         sus_ips.append(ipadds[currentpos:delim])
#         currentpos = delim + len(delimiter)
# print(sus_ips) 



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
clist = [] 

delimiter = ","

currentpos = 0


# look for position of delimiter
delimpos = customers.find(delimiter, currentpos)

# string slicing to slice the words
cust = customers[currentpos:delimpos]

# add to the list
clist.append(cust)

# update currentpos
currentpos = delimpos + len(delimiter)



# write your code for part 2 here





# word = "AISHA,BENNY,CHLONE"
# print(word[6:11])

# palindrome



#[start:stop:step]
