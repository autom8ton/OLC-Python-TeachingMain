# open the file to read

# read all the lines from the file and display it
# task 1.1
with open("product.csv", "r") as fobj:
    content = fobj.read()
print(content)

# task 1.2
name = input("Enter a new product name: ")
price = input("Enter a new product price: ")

# task 1 c
# add a new product and price to the csv file
with open("product.csv", "a") as fobj:
    fobj.write(f"\n{name},{price}")
    print("New product added.")