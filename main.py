import json
import random
import string

ACCOUNTS_FILE = "users.json"


# ---------- File handling ----------

def load_accounts():
    try:
        with open(ACCOUNTS_FILE, "r") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            return {}
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_accounts(accounts):
    with open(ACCOUNTS_FILE, "w") as f:
        json.dump(accounts, f, indent=2)


# ---------- Auth / users ----------

def login(accounts):
    while True:
        nickname = input("Enter your nickname: ").strip().lower()
        if not nickname:
            print("Please enter a nickname.")
            continue

        if nickname not in accounts:
            print("User not found. Please create a new EasyPass nickname.")
            return None

        print("Login success.")
        return nickname


def create_user(accounts):
    while True:
        nickname = input("Create your nickname: ").strip().lower()
        if not nickname:
            print("Please enter a nickname.")
            continue

        if nickname in accounts:
            print("That nickname already exists. Try another.")
            continue

        accounts[nickname] = {}   # services will go here later
        save_accounts(accounts)
        print(f"Created account '{nickname}'.")
        return nickname


# ---------- Password tools ----------

def password_generator(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))


def strength_checker(password):
    if len(password) < 4:
        return "The password should be at least 4 characters long"
    if " " in password:
        return "Your password must not contain spaces"

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_special = any(c in string.punctuation for c in password)
    long_enough = len(password) >= 8

    score = sum([has_lower, has_upper, has_special, long_enough])

    if score == 4:
        return "Strong password"
    elif score in (2, 3):
        return "Medium password"
    elif score == 1:
        return "Weak password"
    else:
        return "Very weak password"


def choose_password():
    """Loop until user accepts a password (generated or own)."""
    while True:
        choice = input(
            "Do you want a generated password? (Y/N): ").strip().upper()

        if choice == "Y":
            try:
                length = int(input("Enter password length: "))
                if 4 <= length <= 50: 
                    break
                else:
                    print("Length must be between 4 and 50.")
            except ValueError:
                print("Please enter a valid number.")
                continue

            password = password_generator(length)
            print("Generated password:", password)
        else:
            password = input("Enter your password: ")

        strength = strength_checker(password)
        print("Password strength:", strength)

        keep = input(
            "Do you want to keep this password? (Y/N): ").strip().upper()
        if keep == "Y":
            return password

        print("Okay, let's try again.\n")


# ---------- Account operations ----------

def show_services(accounts, user):
    services = accounts.get(user, {})
    print("\nYour current services:")
    if not services:
        print("  (none yet)")
    else:
        for name in services:
            print(" -", name)


def account_add_or_save(accounts, user):
    service = input("Service name (e.g. Google, Twitter): ").strip()
    if not service:
        print("Service name cannot be empty.")
        return

    user_id = input("Service username/email: ").strip()
    if not user_id:
        print("User ID cannot be empty.")
        return

    print("\nNow choose a password for this service:")
    password = choose_password()

    if user not in accounts:
        accounts[user] = {}
    accounts[user][service] = {"user_id": user_id, "password": password}
    save_accounts(accounts)
    print(f"Saved credentials for '{service}'.")


def account_read(accounts, user):
    services = accounts.get(user, {})
    if not services:
        print("No saved services.")
        return

    print(f"\nStored credentials for '{user}':")
    for service, creds in services.items():
        print(f"- {service}:")
        print(f"    user_id : {creds['user_id']}")
        print(f"    password: {creds['password']}")


def account_update(accounts, user):
    services = accounts.get(user, {})
    if not services:
        print("No saved services.")
        return

    show_services(accounts, user)
    service = input("Which service do you want to update? ").strip()
    if service not in services:
        print("Service not found.")
        return

    current = services[service]

    new_user_id = input("New user ID (leave blank to keep current): ").strip()
    if new_user_id:
        current["user_id"] = new_user_id

    change_pwd = input("Change password? (Y/N): ").strip().upper()
    if change_pwd == "Y":
        current["password"] = choose_password()

    services[service] = current
    accounts[user] = services
    save_accounts(accounts)
    print(f"Updated credentials for '{service}'.")


def account_delete(accounts, user):
    services = accounts.get(user, {})
    if not services:
        print("No services to delete.")
        return

    show_services(accounts, user)
    service = input("Which service do you want to delete? ").strip()
    if service not in services:
        print("Service not found.")
        return

    confirm = input(f"Delete '{service}'? (Y/N): ").strip().upper()
    if confirm == "Y":
        del services[service]
        accounts[user] = services
        save_accounts(accounts)
        print("Deleted.")


def manage_accounts(accounts, user):
    """Main submenu for managing services of the logged-in user."""
    while True:
        show_services(accounts, user)
        choice = input(
            "\nA) Add / Save service"
            "\nR) Read all details"
            "\nU) Update a service"
            "\nD) Delete a service"
            "\nB) Back\n> "
        ).strip().upper()

        if choice == "A":
            account_add_or_save(accounts, user)
        elif choice == "R":
            account_read(accounts, user)
        elif choice == "U":
            account_update(accounts, user)
        elif choice == "D":
            account_delete(accounts, user)
        elif choice == "B":
            break
        else:
            print("Choose a valid option.")


# ---------- Main loop ----------

def main():
    accounts = load_accounts()
    print("EasyPass")

    while True:
        menu = input(
            "\n1) Login"
            "\n2) Create user"
            "\nQ) Quit\n> "
        ).strip().upper()

        if menu == "1":
            user = login(accounts)
            if not user:
                continue

            # Logged-in menu
            while user in accounts:
                choice = input(
                    "\n1) Manage accounts"
                    "\nL) Logout\n> "
                ).strip().upper()

                if choice == "1":
                    manage_accounts(accounts, user)
                elif choice == "L":
                    print("Logged out.")
                    break
                else:
                    print("Choose a valid option.")

        elif menu == "2":
            create_user(accounts)

        elif menu == "Q":
            print("Goodbye.")
            break

        else:
            print("Choose 1, 2 or Q.")


if __name__ == "__main__":
    main()
