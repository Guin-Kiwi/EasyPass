import random
import string

def password_generator(length):

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""
    for i in range(length):
        password += random.choice(characters)

    return password



length = int(input("Enter password length: "))
print("Generated password:", password_generator(length))
