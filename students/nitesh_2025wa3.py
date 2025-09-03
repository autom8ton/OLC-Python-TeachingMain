"""
A program reads inputs from user in an application form
There are three inputs in the application form with the following requirements.

Name: Must have a first name and last name
Age: Must be 16 Years or older
Email: Must not be registered before/ Must resemble a valid email

Write a program to validate the above application form
- User will be prompted to enter a valid input before proceeding to the next input
- Meaningful error messages must be displayed accordingly
- If the validation passes all the checks:
    - print the registration details
    - add the email to the list of registered emails
"""
registered_emails = []

# check if there is a space for name
while True:
    fname = input("Enter your full name (First Name Last Name): ")

    if " " in fname:
        break
    else:
        print("You must enter a First Name Last Name e.g. Andrew Chong")
    
# validate if 16 years or older
while True:
    age = int(input("Enter your age (must be 16 or older): "))
    if age.isdigit():
        age = int(age) # make sure they input a valid integer

        if age >= 16:
            break
        else:
            print("Age must be 16 or above.")
    else:
        print("Age must be a valid number.")


# valid email and does not exist in list
while True:
    email = input("Enter your email: ").lower()

    if "@" in email and "." in email

        # valid email, and not registered before
        if email not in registered_emails:
            break
        else:
            # registered before
            print(f"{email} was registered before, try again. ")
    else:
        print(f"{email} is not a valid email. A valid email must contain @ and domain")

print(f"Name: {fname}"
print(f"Age: {age}")
print(f"Email: {email}")

registered_emails.append(email)
print(registered_emails) # testing only for list added correctly