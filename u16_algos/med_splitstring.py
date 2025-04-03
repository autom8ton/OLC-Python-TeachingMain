# Practice on how to split strings based on delimiter
s = "Aisha;Benny;Chloe;David;Eva"

delim = ";"

slist = []

currentpos = 0



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



### string slicing
word = "SINGAPORE"

print(word[0]) # pulls out letter

#[start:stop:step] # 

print(word[3:6])


s = "Aisha;Benny;Chloe;David;Eva" # comma seperated value

delim = ";"

wordlist = [] # empty list

currentpos = 0

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



ipadds = "192.168.1.1,10.0.0.2,172.16.5.10,192.168.1.45,10.0.0.18,172.16.5.20,192.168.2.15,10.0.0.5,172.16.5.30,192.168.3.5,10.0.0.12,172.16.6.25,192.168.1.100,10.0.0.9,172.16.5.55,192.168.4.8,10.0.1.1,172.16.7.8,192.168.5.2,10.0.2.3,172.16.8.45,192.168.6.7,10.0.3.5,172.16.9.20,192.168.7.11,10.0.4.9,172.16.10.10,192.168.8.4,10.0.5.2,172.16.11.14,192.168.9.6,10.0.6.3,172.16.12.17,192.168.10.9,10.0.7.8,172.16.13.22,192.168.11.10,10.0.8.15,172.16.14.30,192.168.12.5,10.0.9.20,172.16.15.8,192.168.13.3,10.0.10.11,172.16.16.40,192.168.14.2,10.0.11.4,172.16.17.18,192.168.15.1,10.0.12.5"
delim = 0
delimiter = ","
currentpos = 0
sus_ips = []
delim = ipadds.find(delimiter, currentpos)
while True:
    if delim == -1:
        sus_ips.append(ipadds[currentpos:])
        break
    else:
        sus_ips.append(ipadds[currentpos:delim])
        currentpos = delim + len(delimiter)
print(sus_ips) 