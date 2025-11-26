def main():                           # Defines the main function, the core entry point of the program.
    accounts = load_accounts()        # Loads account data from the JSON file into a dictionary.
    print("EasyPass")                 # Prints the name of the program.

    while True:                       # Infinite loop for the main menu until user quits.
        menu = input(
            "\n1) Login"
            "\n2) Create user"
            "\nQ) Quit\n> "
        ).strip().upper()             # Shows main options and gets user's choice.

        if menu == "1":               # If user chooses Login:
            user = login(accounts)    # Calls login() and stores the result in user.
            if not user:             # If login() returned None or empty (failed login):
                continue              # Skip rest of loop and show main menu again.

            # Logged-in menu          # Comment explaining that next part is the logged-in submenu.
            while user in accounts:   # Loop while that user still exists in accounts (i.e. logged in).
                choice = input(
                    "\n1) Manage accounts"
                    "\nL) Logout\n> "
                ).strip().upper()     # Shows logged-in options, gets choice.

                if choice == "1":     # If user selects "Manage accounts":
                    manage_accounts(accounts, user)  # Open the services submenu.
                elif choice == "L":   # If user chooses Logout:
                    print("Logged out.")  # Confirm logout.
                    break             # Exit the logged-in loop, go back to main menu.
                else:                 # If invalid option:
                    print("Choose a valid option.")  # Error message.

        elif menu == "2":             # If user chooses to create a new user:
            create_user(accounts)     # Calls the create_user() function.

        elif menu == "Q":             # If user chooses to quit:
            print("Goodbye.")         # Prints goodbye message.
            break                     # Breaks the main loop, ending the program.

        else:                         # If user input doesn't match 1, 2, or Q:
            print("Choose 1, 2 or Q.")# Tells user to pick a valid option.


if __name__ == "__main__":           # Checks if this file is being run directly (not imported as a module).
    main()                            # If so, calls the main() function to start the program.
