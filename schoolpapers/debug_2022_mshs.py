word = input("Please enter your word: ")
word = word.lower() #word.islower() # 3.  should be word.lower()
begin_p = word.startswith("p")# 4. word.beginswith("p") # 4. startswith
end_h = word.endswith("h")
contain_e = word.find("e") # 5. word("e") # 5. missing .find()
word_length = len(word)#6. word.length() # should be len()

if not begin_p and not end_h and contain_e == -1: # 1. missing double =
    if word_length <= 3: # 9. should be <= to include 3
        print("The length of the word is short.")
    elif word_length <= 10: # 10 should be word_length
        print("The length of the word is medium.")
    else: # elif: # 2 should be else
        print("The length of the word is long.")
if begin_p:
    print("Invalid. You entered a word that begins with 'p'.")
elif end_h:
    print("Invalid. You entered a word that ends with 'h'.")
elif contain_e != -1: #7 elif not contain_e: # contain_e will return -1
    print("Invalid. You entered a word that contains 'e'.") # 8. should be e