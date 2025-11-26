import json          # Imports the json module to read/write JSON-formatted data.
ACCOUNTS_FILE = "users.json"   # Defines the filename where account data will be stored in JSON format.

def load_accounts():                    # Defines a function to load accounts from the JSON file.
    try:                                # Starts a try block to catch errors when reading/parsing the file.
        with open(ACCOUNTS_FILE, "r") as f:   # Opens the accounts file in read mode as variable f.
            data = json.load(f)        # Reads JSON content from the file and converts it to a Python object.
        if not isinstance(data, dict): # Checks that the loaded data is a dictionary (expected structure).
            return {}                  # If it's not a dict, returns an empty dict as a safe fallback.
        return data                    # If everything is fine, returns the loaded dictionary.
    except (FileNotFoundError, json.JSONDecodeError):   # Catches errors if file is missing or JSON is invalid.
        return {}                      # In case of error, returns an empty dict as default.


def save_accounts(accounts):           # Defines a function to save the accounts dictionary to file.
    with open(ACCOUNTS_FILE, "w") as f:   # Opens the accounts file in write mode (overwrites it).
        json.dump(accounts, f, indent=2)  # Writes the accounts dict as JSON into the file, nicely formatted.


def login(accounts):                   # Defines a function for logging in an existing user.
    while True:                        # Infinite loop until the user logs in or function returns.
        nickname = input("Enter your nickname: ").strip().lower()  # Asks user for nickname, trims spaces, lowers.
        if not nickname:              # If nickname is an empty string:
            print("Please enter a nickname.")  # Warns the user.
            continue                  # Restarts the loop to ask again.

        if nickname not in accounts:  # Checks if entered nickname does NOT exist in the accounts dict.
            print("User not found. Please create a new EasyPass nickname.")  # Error message.
            return None               # Returns None to indicate login failed.

        print("Login success.")       # Confirms successful login.
        return nickname               # Returns the nickname of the logged-in user.


def create_user(accounts):            # Defines a function to create a new user.
    while True:                       # Infinite loop until a valid unique nickname is created.
        nickname = input("Create your nickname: ").strip().lower()  # Asks for a new nickname, trims & lowercases.
        if not nickname:              # If the nickname is empty:
            print("Please enter a nickname.")  # Warns the user.
            continue                  # Repeats the loop.

        if nickname in accounts:      # Checks if nickname already exists in accounts.
            print("That nickname already exists. Try another.")  # Warns about duplicate nickname.
            continue                  # Ask again.

        accounts[nickname] = {}       # Creates a new empty dict for this user (services will be stored here).
        save_accounts(accounts)       # Saves the updated accounts to the JSON file.
        print(f"Created account '{nickname}'.")  # Confirms the account creation.
        return nickname               # Returns the new nickname.
