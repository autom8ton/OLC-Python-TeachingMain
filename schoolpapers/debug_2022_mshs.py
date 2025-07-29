word = input("Please enter your word: ")
word = word.islower()
begin_p = word.beginswith("p")
end_h = word.endswith("h")
contain_e = word("e")
word_length = word.length()
if not begin_p and not end_h and contain_e = -1:
    if word_length < 3:
        print("The length of the word is short.")
    elif word <= 10:
        print("The length of the word is medium.")
    elif:
        print("The length of the word is long.")
if begin_p:
    print("Invalid. You entered a word that begins with 'p'.")
elif end_h:
    print("Invalid. You entered a word that ends with 'h'.")
elif not contain_e:
    print("Invalid. You entered a word that contains 'a'.")