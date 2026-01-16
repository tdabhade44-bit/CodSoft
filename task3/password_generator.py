import random
import string

# get password length from user
length = int(input("Enter password length: "))

# combination of characters
characters = string.ascii_letters + string.digits + string.punctuation

# generate password
password = ""
for i in range(length):
    password += random.choice(characters)

# Output
print("Generated Password:", password)
