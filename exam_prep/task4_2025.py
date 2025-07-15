'''
Task 5
Open a new JupyterLab notebook and save it as: 
TASK5_<your name>_<centre number>_<index number>.ipynb

The task is to write a program that encrypts and decrypts messages.
A cipher is an algorithm that encodes a message so that only the 
intended recipient is able to read it.
The Caesar Shift Cipher is a type of cipher where each letter 
in the original message is shifted down
the alphabet sequence by a fixed number of positions.

The table below shows an example where the letters have been shifted 
down the alphabet sequence by 3 positions. The letters 'wrap-around' 
at the end. Using the table, the message 'happy' would be encoded as 'kdssb'.
Original            >>  a b c d e f g h i j k l m n o p q r s t u v w x y z
Shifted down by 3   >>  d e f g h i j k l m n o p q r s t u v w x y z a b c

The process of encoding the message is called encryption and 
the encoded message is called the ciphertext. In order to 
read it, the recipients need to perform an opposite process 
called decryption to change the ciphertext back to the original message.
'''
# All code should have appropriate comments and all 
# identifiers should be appropriately named. [4]


'''
Task 5.1 [4]
Write a shift() function that has the parameter char passed to it. 
The function must shift a lower-case letter down the alphabet sequence 
by one position (a → b ... → y → z → a) and do nothing to other characters.                                                                                                                                         
'''
#-----------------------------------
# Task 5.1 [4]
#-----------------------------------

# Write and test your code here
def shift(char): #z
    # or use chr()/ ord() for ascii, but this way easier.
    alphas = 'abcdefghijklmnopqrstuvwxyz' 

    # check if char is lower case or in alphas string
    if char in alphas: 
        idx = alphas.find(char) # find the index

        # shift 1 and handle wrap around cos 26 alphabets
        shifted_idx = (idx + 1 ) % 26  

        return alphas[shifted_idx]
    else:
        return char

# shift('z',1)

# finding the start and end range
# print(ord('a')) #97
# print(ord('z')) #122

def shift(char):
    startrange = ord('a') # 97 # find the start position of lowercase letters in ascii
    endrange = ord('z') # 122 # find the end position of lowercase letters in ascii

    idx = ord(char) # find the ordinal number (index) of the character

    if idx >= startrange and idx <= endrange:

        # offset to zero and modulus 26 to handle wraparound, then add startrange back
        shifted_idx = (idx - startrange + 1) % 26 + startrange

        return chr(shifted_idx) # z -> a. a -> b
    else:
        # if not lowercase, just return back as per question
        return char
    
print(shift2('y'))


'''
Task 5.2 [7]
Write a function encrypt() that has the parameters message and 
positions passed to it. The function must use the shift() function 
to encrypt the message argument by shifting all the lower-case 
letters in the message down the alphabet sequence by the number 
of positions given in the positions argument. The function 
should ignore all other characters. 
'''
#-----------------------------------
# Task 5.2 [7]
#-----------------------------------
# Write and test your code here
# a a a , 3 > d d d
def encrypt(message, positions):
    encrypted = ''

    # loop through message to shift 
    for c in message:
        tempchar = c # current character
        # loop x many times to shift 1 character
        for i in range(positions):
            tempchar = shift(tempchar)

        # concatenate back the final shifter character    
        encrypted = encrypted + tempchar

    return encrypted

print(encrypt("aaa", 1))

'''
Task 5.3 [2]
Write a function shift_up() that has the parameter char passed to it. 
The function must shift a lower-case letter up the alphabet sequence by 
one position (a ← b ... ← y ← z ← a) and do nothing to other characters.                                                                                                                                         
'''
#-----------------------------------
# Task 5.3 [2]
#-----------------------------------
# Write and test your code here
def shift_up(char):
    # or use chr()/ ord() for ascii, but this way easier.
    alphas = 'abcdefghijklmnopqrstuvwxyz' 

    # check if char is lower case or in alphas string
    if char in alphas: 
        idx = alphas.find(char) # find the index

        # shift 1 and handle wrap around cos 26 alphabets
        shifted_idx = (idx - 1 ) % 26  
        
        return alphas[shifted_idx]
    else:
        return char

# print(shift_up('z', 1))

'''
Task 5.4 [1]
Write a function decrypt() that has the parameters ciphertext 
and positions passed to it. The function must use the shift_up() 
function to decrypt the ciphertext argument by shifting all the 
letters up the alphabet sequence by the number of positions given 
in the positions argument. 
The function should ignore all other characters. 
'''
#-----------------------------------
# Task 5.4 [1]
#-----------------------------------
# Write and test your code here
def decrypt(message, positions):
    decrypted = ''

    # loop through message to shift 
    for c in message:
        tempchar = c # current character
        # loop x many times to shift 1 character
        for i in range(positions):
            tempchar = shift_up(tempchar)

        # concatenate back the final shifter character    
        decrypted = decrypted + tempchar

    return decrypted
# print(encrypt("A B C", 1))

'''
Task 5.5 [7]
Create a simple text-based user interface to:
• request the user to enter 'E' to encrypt a message or 'D' to 
decrypt a ciphertext (case insensitive) and to re-enter if the 
input is not 'E', 'D', 'e' or 'd'

• request the user to enter the message or the ciphertext

• request the user to enter the number of positions to shift 
the letters and the user to re-enter the number if the input is 
not a positive integer

• output the encrypted message and write the encrypted message 
to the file encrypted.txt, if the user requested to encrypt a message

• output the decrypted ciphertext if the user requested to decrypt a message.
Your program should use the encrypt() and decrypt() functions.
Test your program with the following input:
a, E, This is the seCret me55age!, -1, 12 
'''
#-----------------------------------
# Task 5.5 [7]
#-----------------------------------
# Write and test your code here

while True:
    command = input("Type E/e to encrypt, or D/d to decrypt: ").lower()

    # check if command input is correct
    if command not in "de":
        print("Invalid input. Only E/e or D/d.")
    else:
        break

# getting message for encryption/ decryption
if command == "e":
    content = input("Input message for encryption: ")
elif command == 'd':
    content = input("Input ciphertext for decryption: ")

while True:
    shiftnum = input("Enter positions to shift: ")

    # ensure valid number and more than 0
    if shiftnum.isdigit() and int(shiftnum) > 0:
        shiftnum = int(shiftnum)
        break
    else:
        print("Shift position must be a positive integer.")

if command == 'e':
    encrypted = encrypt(content, shiftnum)
    print(f"Encrypted Text is: {encrypted}")
    with open('encrypted.txt','w') as fobj:
        fobj.write(encrypted)

if command == 'd':
    decrypted = decrypt(content, shiftnum)
    print(f"Decrypted Text is: {decrypted}")

# a, E, This is the seCret me55age!, −1, 12