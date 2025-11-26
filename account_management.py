def show_services(accounts, user):    # Defines a function to display all services for a given user.
    services = accounts.get(user, {}) # Gets the user's services dict; defaults to empty dict if user not found.
    print("\nYour current services:") # Prints a header with newline before it.
    if not services:                 # If services dict is empty:
        print("  (none yet)")        # Shows that there are no services yet.
    else:                            # Otherwise, if there are services:
        for name in services:        # Iterates over each service name.
            print(" -", name)        # Prints the service name with a dash.


def account_add_or_save(accounts, user):   # Defines a function to add or save credentials for a service.
    service = input("Service name (e.g. Google, Twitter): ").strip()
    # Asks for the service name, trims spaces.

    if not service:                   # If service name is empty:
        print("Service name cannot be empty.")  # Error message.
        return                        # Exits function.

    user_id = input("Service username/email: ").strip()
    # Asks for the username/email for the service and trims spaces.

    if not user_id:                   # If user_id is empty:
        print("User ID cannot be empty.")  # Error message.
        return                        # Exits function.

    print("\nNow choose a password for this service:")  # Prompts user that they will choose a password.
    password = choose_password()      # Calls choose_password() to get a password from the user.

    if user not in accounts:          # If the user doesn't exist in accounts (safety check):
        accounts[user] = {}           # Create an empty dict for them.

    accounts[user][service] = {"user_id": user_id, "password": password}
    # Stores the credentials for this service as a nested dictionary under this user.

    save_accounts(accounts)           # Saves updated accounts to the JSON file.
    print(f"Saved credentials for '{service}'.")  # Confirms that credentials were saved.


def account_read(accounts, user):     # Defines a function to print all credentials for a user's services.
    services = accounts.get(user, {}) # Gets services dict for user.
    if not services:                 # If no services exist:
        print("No saved services.")   # Informs user.
        return                        # Exits function.

    print(f"\nStored credentials for '{user}':")  # Prints header with username.
    for service, creds in services.items():       # Loops through each service and its credentials.
        print(f"- {service}:")                    # Prints service name.
        print(f"    user_id : {creds['user_id']}")# Prints the stored user_id, indented.
        print(f"    password: {creds['password']}") # Prints the stored password, indented.


def account_update(accounts, user):   # Defines a function to update credentials for a given service.
    services = accounts.get(user, {}) # Gets services for user.
    if not services:                 # If there are none:
        print("No saved services.")   # Notify user.
        return                        # Exit.

    show_services(accounts, user)     # Shows list of services to choose from.
    service = input("Which service do you want to update? ").strip()
    # Asks for the name of the service to update.

    if service not in services:       # If the named service doesn't exist:
        print("Service not found.")   # Error message.
        return                        # Exits function.

    current = services[service]       # Retrieves current credentials for that service.

    new_user_id = input("New user ID (leave blank to keep current): ").strip()
    # Asks user for a new user ID, allows keeping old one if blank.

    if new_user_id:                   # If user typed something (non-blank):
        current["user_id"] = new_user_id  # Updates the user_id with the new value.

    change_pwd = input("Change password? (Y/N): ").strip().upper()
    # Asks if they want to change the password.

    if change_pwd == "Y":             # If yes:
        current["password"] = choose_password()  # Calls choose_password to get a new password.

    services[service] = current       # Stores updated credentials back into services dict.
    accounts[user] = services         # Writes services dict back under this user in accounts.
    save_accounts(accounts)           # Saves updated accounts to file.
    print(f"Updated credentials for '{service}'.")  # Confirms update.


def account_delete(accounts, user):   # Defines a function to delete a service for a given user.
    services = accounts.get(user, {}) # Gets services dict for this user.
    if not services:                 # If it's empty:
        print("No services to delete.") # Tell user there is nothing to delete.
        return                        # Exit.

    show_services(accounts, user)     # Shows current services to choose from.
    service = input("Which service do you want to delete? ").strip()
    # Asks for the service name to delete.

    if service not in services:       # If that service doesn't exist:
        print("Service not found.")   # Error message.
        return                        # Exit.

    confirm = input(f"Delete '{service}'? (Y/N): ").strip().upper()
    # Asks for confirmation before deleting.

    if confirm == "Y":                # If user confirms:
        del services[service]         # Removes the service entry from services dict.
        accounts[user] = services     # Updates accounts with modified services dict.
        save_accounts(accounts)       # Saves updated accounts.
        print("Deleted.")             # Confirms deletion.


def manage_accounts(accounts, user):  # Defines the submenu to manage all services for a logged-in user.
    """Main submenu for managing services of the logged-in user."""  # Docstring explaining this function.
    while True:                      # Infinite loop for the submenu until user chooses to go back.
        show_services(accounts, user) # Shows current list of services.
        choice = input(
            "\nA) Add / Save service"
            "\nR) Read all details"
            "\nU) Update a service"
            "\nD) Delete a service"
            "\nB) Back\n> "
        ).strip().upper()            # Displays options and gets user's choice, stripped & uppercased.

        if choice == "A":            # If user chooses to add/save a service:
            account_add_or_save(accounts, user)  # Calls add/save function.
        elif choice == "R":          # If user chooses to read all details:
            account_read(accounts, user)  # Calls read function.
        elif choice == "U":          # If user chooses to update a service:
            account_update(accounts, user)  # Calls update function.
        elif choice == "D":          # If user chooses to delete a service:
            account_delete(accounts, user)  # Calls delete function.
        elif choice == "B":          # If user chooses to go back:
            break                    # Breaks out of the submenu loop, returning to main menu.
        else:                        # If input doesn't match any option:
            print("Choose a valid option.")  # Prints an error message.
