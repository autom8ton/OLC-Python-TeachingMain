#------------------------------------------------------------
# Exercise 14: Combined Checks (Password Policy)
# Requirements:
# - Non-empty
# - Length between 8 and 16
# - Must contain at least one digit 0-9
# - No spaces
# Keep prompting until valid, then print "Password set".
# Sample Inputs: "abc" (invalid), "abcd efgh1" (invalid), "GoodPass1" (valid)
#------------------------------------------------------------

while True:
    pw = input("Enter a password: ")

    hasdigit = False
    hasspace = False # flag
    hasspecial = False

    # check whether has number and has not space
    for c in pw:
        if c.isdigit():
            hasdigit = True
        if c.isspace():
            hasspace = True
        # if c in ["!","@","#","$","%","&","*"]:
        if c in "!@#$%&*":
            hasspecial = True

    # !@#$%&*
    if pw == "":
        print("Password cannot be empty")
    elif len(pw) < 8 or len(pw) > 16:
        print("Password length must be between 8 and 16.")
    elif hasdigit == False:
        print("Password must contain a number from 0 to 9")
    elif hasspace:
        print("Password cannot contain spaces.")
    else:
        print(f"Password {pw} has been set. ")
        break

    