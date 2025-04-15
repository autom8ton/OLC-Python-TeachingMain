countries = {"Singapore": "Singapore", "China":"Beijing","Malaysia":"Kuala Lumpur"}

option = input("Enter a country: ")
if option in countries: # key
    print(f"The Capital of {option} is {countries[option]}")