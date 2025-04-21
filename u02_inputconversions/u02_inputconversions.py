#####
# variable types
# numbers - integers (whole numbers), floats (floating point numbers)
# string - words, anything with quotation mark is a string
# boolean - True/ False
# list - list of values (numbers, string, boolean, dictionary ..... )
# dictionary - key/ value pairs

# var1 = "dog" # string
# var2 = "cat" # string
# var3 = var1 + var2 # + on 2 strings, will join (string concatenation)
# print(var3)

# var4 = 10 # integer
# var5 = 20 # integer
# var6 = var4 + var5 # + on 2 integers will add them
# print(var6)

# # type conversion int() str()
# var7 = str(var4) + var1
# # var8 = var4 * var1
# print(var7)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
answer = num1 + num2

# option 1 - basic but painful
# print(str(num1) + " + " + str(num2) + " = " + str(answer))

# option 2 - a bit better, but only works for print()
# print(num1, " + ", num2, " = ", answer)

# option 3 - more powerful, correct
# sentence = "{} + {} = {}".format(num1, num2, answer)
# print(sentence)

# option 4 - f string
sentence = f"{num1} + {num2} = {answer}"
print(sentence)