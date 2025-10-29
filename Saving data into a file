def input_username():
    username = input("Username: ")
    while username == "":
        print("Error: Enter your username.")
        username = input("Username: ")
    return username

def input_password():
    password = input("Password: ")
    while password == "":
        print("Error: Enter your password.")
        password = input("Password: ")
    return password

def print_user(username):
    print(f"Username: {username}")

def main():
    file_path = "accounts.txt"
    print("Welcome to EasyPass!")
    
    new_account = input("Would you like to create a new account? (y/n): ").strip().lower()
    while new_account not in ["y", "n"]:
        print("Error: Enter y or n")
        new_account = input("Would you like to create a new account? (y/n): ").strip().lower()

    if new_account == "y":
        while True:
            username = input_username()
            password = input_password()
            with open(file_path, "a") as file:
                file.write(f"{username} {password}\n")
            again = input("Add another account? (y/n): ").strip().lower()
            if again != "y":
                break

    print("\nSaved accounts:")
    with open(file_path) as file:
        for line in file:
            username, password = line.rstrip("\n").split(" ")
            print_user(username)

if __name__ == "__main__":
    main()
 
