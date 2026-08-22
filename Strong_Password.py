password = input("Enter your password: ")

if len(password) < 8:
    print("Weak Password")

elif password.isalpha():
    print("Weak Password: Add numbers and special characters")

elif password.isdigit():
    print("Weak Password: Add letters and special characters")

elif password.isalnum():
    print("Medium Password: Add a special character")

else:
    print("Strong Password")