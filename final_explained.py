import json                  # Imports JSON module to read/write JSON files
import random                # Imports random module for generating passwords
import string                # Imports string constants (letters, digits, punctuation)

ACCOUNTS_FILE = "users.json" # Name of the JSON file where account data is stored


# ---------- File handling ----------

def load_accounts():         # Function to load all accounts from file
    try:                     # Try to open and read the file
        with open(ACCOUNTS_FILE, "r") as f:  # Opens JSON file in read mode
            data = json.load(f)              # Loads JSON content into Python data
        if not isinstance(data, dict):       # Ensures the data is a dictionary
            return {}                        # If not, return an empty dict
        return data                          # Return the loaded account data
    except (FileNotFoundError, json.JSONDecodeError):  # If file missing or corrupted
        return {}                            # Return empty dict safely


def save_accounts(accounts): # Saves accounts dictionary into JSON file
    with open(ACCOUNTS_FILE, "w") as f:      # Opens file in write mode
        json.dump(accounts, f, indent=2)     # Writes formatted JSON to the file


# ---------- Auth / users ----------

def login(accounts):         # Function to log a user into the system
    while True:              # Loop until valid login or exit
        nickname = input("Enter your nickname: ").strip().lower()  # Get name, clean spacing, lowercase
        if not nickname:     # If empty input
            print("Please enter a nickname.") # Ask again
            continue

        if nickname not in accounts:         # Check if nickname exists
            print("User not found. Please create a new EasyPass nickname.")
            return None                      # Login failed

        print("Login success.")              # Login worked
        return nickname                      # Return logged-in username


def create_user(accounts):   # Function to create a new user account
    while True:              # Loop until a valid unique nickname is made
        nickname = input("Create your nickname: ").strip().lower()  # New nickname
        if not nickname:     # Must not be empty
            print("Please enter a nickname.")
            continue

        if nickname in accounts:             # Nickname already exists?
            print("That nickname already exists. Try another.")
            continue

        accounts[nickname] = {}              # Creates empty service list for user
        save_accounts(accounts)              # Saves new user to the file
        print(f"Created account '{nickname}'.")
        return nickname                      # Return created username


# ---------- Password tools ----------

def password_generator(length):              # Creates a random password
    chars = string.ascii_letters + string.digits + string.punctuation  # Pool of characters
    return "".join(random.choice(chars) for _ in range(length))        # Randomly pick characters


def strength_checker(password):              # Checks how strong a password is
    if len(password) < 4:                    # Too short?
        return "The password should be at least 4 characters long"
    if " " in password:                      # Contains spaces?
        return "Your password must not contain spaces"

    has_lower = any(c.islower() for c in password)     # Contains lowercase?
    has_upper = any(c.isupper() for c in password)     # Contains uppercase?
    has_special = any(c in string.punctuation for c in password)  # Contains symbol?
    long_enough = len(password) >= 8                   # Length at least 8?

    score = sum([has_lower, has_upper, has_special, long_enough]) # Total score

    if score == 4:                      # All rules matched
        return "Strong password"
    elif score in (2, 3):              # Some rules matched
        return "Medium password"
    elif score == 1:                    # Only one rule matched
        return "Weak password"
    else:                               # No rules matched
        return "Very weak password"


def choose_password():                  # Lets user generate or enter a password
    """Loop until user accepts a password (generated or own)."""
    while True:                         # Keep asking until password approved
        choice = input("Do you want a generated password? (Y/N): ").strip().upper()

        if choice == "Y":               # User wants generated password
            try:
                length = int(input("Enter password length: "))  # Get length as number
                if length <= 0:         # Must be positive
                    print("Length must be positive.")
                    continue
            except ValueError:          # Not a valid number
                print("Please enter a valid number.")
                continue

            password = password_generator(length)   # Generate password
            print("Generated password:", password)
        else:
            password = input("Enter your password: ")  # User types their own password

        strength = strength_checker(password)          # Check password strength
        print("Password strength:", strength)

        keep = input("Do you want to keep this password? (Y/N): ").strip().upper()
        if keep == "Y":                 # If user accepts password
            return password             # Return chosen password

        print("Okay, let's try again.\n")  # Otherwise restart


# ---------- Account operations ----------

def show_services(accounts, user):      # Displays list of saved services
    services = accounts.get(user, {})   # Get user’s services or empty dict
    print("\nYour current services:")
    if not services:                    # No services stored
        print("  (none yet)")
    else:
        for name in services:           # Print each service name
            print(" -", name)


def account_create(accounts, user):     # Add a new service to user
    service = input("Service name (e.g. Google, Twitter): ").strip()
    if not service:                     # Must not be empty
        print("Service name cannot be empty.")
        return

    user_id = input("Service username/email: ").strip()
    if not user_id:                     # Must not be empty
        print("User ID cannot be empty.")
        return

    print("\nNow choose a password for this service:")
    password = choose_password()        # Get password from user

    if user not in accounts:            # Ensure user exists
        accounts[user] = {}

    accounts[user][service] = {         # Save service credentials
        "user_id": user_id,
        "password": password
    }

    save_accounts(accounts)             # Write updates to file
    print(f"Saved credentials for '{service}'.")


def account_read(accounts, user):       # Show all stored services for user
    services = accounts.get(user, {})
    if not services:                    # No services to show
        print("No saved services.")
        return

    print(f"\nStored credentials for '{user}':")
    for service, creds in services.items():      # Loop through each service
        print(f"- {service}:")                   # Service name
        print(f"    user_id : {creds['user_id']}")  # Print username
        print(f"    password: {creds['password']}")  # Print password


def account_update(accounts, user):     # Update an existing service
    services = accounts.get(user, {})
    if not services:                    # None saved
        print("No saved services.")
        return

    show_services(accounts, user)       # Show services to choose from
    service = input("Which service do you want to update? ").strip()

    if service not in services:         # Must exist
        print("Service not found.")
        return

    current = services[service]         # Get existing credentials

    new_user_id = input("New user ID (leave blank to keep current): ").strip()
    if new_user_id:                     # Update username if provided
        current["user_id"] = new_user_id

    change_pwd = input("Change password? (Y/N): ").strip().upper()
    if change_pwd == "Y":               # Update password if chosen
        current["password"] = choose_password()

    services[service] = current         # Save updated data
    accounts[user] = services           # Write back to user
    save_accounts(accounts)             # Save to file
    print(f"Updated credentials for '{service}'.")


def account_delete(accounts, user):     # Delete a stored service
    services = accounts.get(user, {})
    if not services:
        print("No services to delete.")
        return

    show_services(accounts, user)       # Show list to pick from
    service = input("Which service do you want to delete? ").strip()

    if service not in services:         # Must exist
        print("Service not found.")
        return

    confirm = input(f"Delete '{service}'? (Y/N): ").strip().upper()
    if confirm == "Y":                  # Confirm delete
        del services[service]           # Remove service
        accounts[user] = services       # Update dictionary
        save_accounts(accounts)         # Save to file
        print("Deleted.")


def manage_accounts(accounts, user):    # Menu for managing services
    """Main submenu for managing services of the logged-in user."""
    while True:                         # Loop until user chooses Back
        show_services(accounts, user)   # Display services
        choice = input(
            "\nC) Create new account."
            "\nR) Read (display) accounts."
            "\nU) Update account."
            "\nD) Delete account."
            "\nB) Back\n> "
        ).strip().upper()

        if choice == "C":
            account_create(accounts, user)
        elif choice == "R":
            account_read(accounts, user)
        elif choice == "U":
            account_update(accounts, user)
        elif choice == "D":
            account_delete(accounts, user)
        elif choice == "B":
            break                       # Exit submenu
        else:
            print("Choose a valid option.")


# ---------- Main loop ----------

def main():                             # Starting point of the program
    accounts = load_accounts()          # Read data from JSON file
    print("EasyPass")                   # Title

    while True:                         # Main menu loop
        menu = input(
            "\n1) Login"
            "\n2) Create user"
            "\nQ) Quit\n> "
        ).strip().upper()

        if menu == "1":                 # Login option
            user = login(accounts)      # Attempt login
            if not user:                # Failed login?
                continue

            # Logged-in menu loop
            while user in accounts:     # While user remains logged in
                choice = input(
                    "\n1) Manage accounts"
                    "\nL) Logout\n> "
                ).strip().upper()

                if choice == "1":       # Manage stored services
                    manage_accounts(accounts, user)
                elif choice == "L":     # Logout
                    print("Logged out.")
                    break
                else:
                    print("Choose a valid option.")

        elif menu == "2":               # Create user option
            create_user(accounts)

        elif menu == "Q":               # Quit program
            print("Goodbye.")
            break

        else:
            print("Choose 1, 2 or Q.")  # Invalid menu choice


if __name__ == "__main__":             # Only run main() when file executed directly
    main()                              # Start the program
