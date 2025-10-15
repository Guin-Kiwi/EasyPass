#Trying to practice a bit at home

import os

files = os.listdir()
# how to make user_login_success a gloal variable?
valid_selection = ["1","2"]

welcome = "Welcome to EasyPass, a simple password manager."
print(welcome)  

login_menu = (
    "What would you like to do? \n"
    "1. Login \n"
    "2. Create new User \n"
    "Please enter a number from the above: "
)

login_selection = input(login_menu)
    
if login_selection == "1":
    valid_user = False
    user_login_success = False
    print("Logging In")
    while valid_user == False:
        login_name = input("Enter your username: ")
        if f"{login_name.lower()}.txt" in files:
            valid_user = True 
        elif f"{login_name.lower()}.txt" not in files:
            print("User not found, please create a new user")  
            login_selection = "2"
            break
    if valid_user == True:
        with open(f"{login_name.lower()}.txt", "r") as user_file:
            lines = user_file.readlines()
            attempt_counter = 0
            while len(lines) >= 1 and attempt_counter < 3:
                login_password = input("Enter your password: ")
                stored_password = lines[1].strip() 
                if stored_password == login_password:
                    user_login_success = True
                    print("Login successful!")
                    break
                elif stored_password != login_password:
                    attempt_counter += 1
                    print(f"Incorrect password, try again, you have {3 - (attempt_counter)} tries left")
            if attempt_counter == 3:
                print("Your account has been locked") #default text, of course doesnt lock anything 
            if len(lines) <= 1:
                print("No password set, Let's set one up now. ")
                new_password = input("Enter a new password:")
                with open(f"{login_name.lower()}.txt", "w") as user_file:
                    user_file.write(f"{login_name}\n{new_password}")                  
    elif login_selection not in valid_selection:
        print("Invalid selection, please try again.")   
        login_selection = input(login_menu)   
        
#            if len(lines) < 1:
#                print("User file is corrupted, please contact support.")


if login_selection == "2":
    new_user_setup = False
    new_login_name = ""
    username_accepted = False
    print("Creating a new User")
    while not username_accepted:
        new_login_name = input("Enter a new username: ")
        if f"{new_login_name.lower()}.txt" in files:
            print("Username not available, please choose another: ")
        elif f"{new_login_name.lower()}.txt" not in files:
            username_accepted = True
            print("Unique Username Accepted.")
    else:
        new_login_password = input("Enter a new password: ")
        with open(f"{new_login_name.lower()}.txt", "w") as user_file:
            user_file.write(f"{new_login_name}\n{new_login_password}")
            new_user_setup = True
            print("User created successfully!")
            if new_user_setup == True:
                login_new_user = input("Would you like to login y/n: ")
                if login_new_user == "y":
                    login_selection = "1"
        
        

                        
