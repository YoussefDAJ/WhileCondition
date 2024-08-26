correct_password = "a1b2c3"
entered_password = input("Enter password: ")
while entered_password != correct_password:
    print("Incorrect password. Try again.")
    entered_password = input("Enter password again: ")

print("Access Granted!")
