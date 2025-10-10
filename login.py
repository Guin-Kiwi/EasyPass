#Trying out some coding


import os

files = os.listdir()

welcome = "Welcome to EasyPass, a simple password manager."
print(welcome)  

login_menu = (
    "What would you like to do? \n"
    "1. Login \n"
    "2. Create new User \n"
    "Please enter a number from the above: "
)

login_selection = input(login_menu)

while login_selection not in ["1", "2"]:
    print("Invalid selection, please try again.")   
    login_selection = input(login_menu)
while login_selection == "1":
    print("You selected Login")
    login_name = input("Enter your username: ")
    if f"{login_name.lower()}.txt" not in files:
        print("User not found, please create a new user.")
        login_selection = input(login_menu)
        continue
    else:
        login_password = input("Enter your password: ")
        with open(f"{login_name.lower()}.txt", "r") as user_file:
            lines = user_file.readlines()
            if  len(lines) >= 1:
                stored_password = lines[1].strip() 
                while stored_password == login_password:
                    print("Login successful!")
                    break   
            if len(lines) == 0:
                print("No password set, Let's set one up now. ")
                new_password = input("Enter a new password:")
                with open(f"{login_name.lower()}.txt", "w") as user_file:
                    user_file.write(f"{login_name}\n{new_password}")  
                    continue
                  
while login_selection == "2":
    print("You selected Create new User")
    new_login_name = input("Enter a new username: ")
    while f"{new_login_name.lower()}.txt" in files:
        print("Username already exists, please try a different one.")
        new_login_name = input("Enter a new username: ")
    else:
        new_login_password = input("Enter a new password: ")
        with open(f"{new_login_name.lower()}.txt", "w") as user_file:
            user_file.write(f"{new_login_name}\n{new_login_password}")
        print("User created successfully!")
    break
