import random
import string

# input the length of the password from user
password_length = int(input("Enter password length : "))

#set of characters to choose from
letters = string.ascii_letters  # a-z and A-Z
digits = string.digits          # 0-9
symbols = string.punctuation    # Special characters

# Combine all characters into one string
all_characters = letters + digits + symbols

if password_length<=3 :
    print("Password length must be greater than 3")
else :
    # empty password string
    password = ""

    # random characters one by one and add to the password
    for i in range(password_length):
        password += random.choice(all_characters)

    print("Your password is:", password)