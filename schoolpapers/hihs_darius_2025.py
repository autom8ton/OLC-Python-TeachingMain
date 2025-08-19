from random import randint as x # alias
# x is an alias for random.randint

# a = x(27,100)

unik_val = []

ppl = ["Tom", "Yada", "Avaneesh", "Darius", " Eason", "Edward",
       "ZhiNing", "Amanda", "Sabina", "Ace", "Dean", "Dylan",
       "Gabriel","ZhenEn", "Justin"]

# function no_repeat
def no_repeat(alist):
    # 15 unique random numbers from 27, 100

    while len(alist) < 15:

        rannum = x(27,100) # gen a random number

        if rannum not in alist: # check is this rannum not in the list?
            alist.append(rannum) # add to the list
    
    return alist

output = no_repeat(unik_val)

# task 3.2
def key_finder(numa, dicta):
    # LOOP THROUGH each key/ value pair
    for key, value in dicta.items():
        # check whether value match given integer
        if numa == value:

            # if match found, return key
            return key
    
    # else finish checking entire dictionary return None
    return None

testdict = {"a":27,"b":33,"c":45}
testnum = 99

output = key_finder(testnum, testdict)
print(output)

# task 3.3

#        [47, 97, 67, 82, 83, 98, 72, 75, 91, 63, 56, 68, 38, 80, 45]
# ppl = ["Tom", "Yada", "Avaneesh", "Darius", " Eason", "Edward",
#        "ZhiNing", "Amanda", "Sabina", "Ace", "Dean", "Dylan",
#        "Gabriel","ZhenEn", "Justin"]
unik_val = no_repeat(unik_val)

combi = {} # empty dictionary

# loop through both unik_val and ppl list.
for i in range(len(ppl)):
    currentstudent = ppl[i]
    currentscore = unik_val[i]

    combi[currentstudent] = currentscore # how you create a dictinoary entry

print(combi)

# combine into a dictionary

###########################
# task 3.4

sort_unik_val = sorted(unik_val) 
# [33, 38, 42, 51, 54, 56, 57, 64, 68, 78, 84, 85, 86, 88, 96]
combi_sorted = {}
# {'Tom': 30, 'Yada': 71, 'Avaneesh': 100, 'Darius': 86, ' Eason': 64, 'Edward': 76, 'ZhiNing': 81, 'Amanda': 75, 'Sabina': 45, 'Ace': 67, 'Dean': 38, 'Dylan': 27, 'Gabriel': 77, 'ZhenEn': 74, 'Justin': 57}

# loop through sort_unik_val



menu = {"hamburger": 5, "fries":3}

# add a new food item
menu["spaghetti"] = 7