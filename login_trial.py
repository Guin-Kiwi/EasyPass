import os
import json
import random
import string
from typing import Dict, Tuple, Optional
#probably doesnt work properly with the new json

def load_users(path: str = "users.json") -> Dict:
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            users = json.load(f)
    except (json.JSONDecodeError, OSError):
        print("Warning: users.json missing or corrupt — starting empty.")
        return {}
    # normalize simple legacy cases: string -> {"EasyPass_pw": <string>}
    for name, record in list(users.items()):
        if isinstance(record, str):
            users[name] = {"EasyPass_pw": record}
        elif not isinstance(record, dict):
            users[name] = {"EasyPass_pw": ""}
        else:
            record.setdefault("EasyPass_pw", "")
    return users

def save_users(users: Dict, path: str = "users.json") -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=2)

def strength_checker(pw: str) -> Tuple[int, str]:
    s = 0
    s += len(pw) >= 8
    s += any(c.islower() for c in pw)
    s += any(c.isupper() for c in pw)
    s += any(c.isdigit() for c in pw)
    s += any(c in string.punctuation for c in pw)
    labels = {0:"Very weak",1:"Very weak",2:"Weak",3:"Medium",4:"Strong",5:"Very strong"}
    return s, labels[s]

def password_generator(length: int = 12) -> str:
    try:
        n = max(4, int(length))
    except (TypeError, ValueError):
        n = 12
    rng = random.SystemRandom()
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(rng.choice(chars) for _ in range(n))

def login(users: Dict) -> Optional[str]:
    username = input("Username: ").strip().lower()
    if not username:
        print("Empty username.")
        return None
    record = users.get(username)
    if not isinstance(record, dict):
        print("User not found.")
        return None
    for i in range(3):
        if input("Master password: ") == record.get("EasyPass_pw"):
            print("Login successful.")
            return username
        print(f"Incorrect password ({2 - i} attempts left).")
    print("Login failed.")
    return None

def new_user(users: Dict) -> Optional[str]:
    while True:
        username = input("Choose username: ").strip().lower()
        if not username or not username.isalnum():
            print("Alphanumeric username required.")
            continue
        if username in users:
            print("Taken.")
            continue
        pw = input("Choose master password: ")
        if pw != input("Confirm: "):
            print("No match.")
            continue
        users[username] = {"EasyPass_pw": pw}
        save_users(users)
        print("User created.")
        return username

def change_password(users: Dict, username: str) -> None:
    if username not in users:
        print("User not found.")
        return
    new_pw = input("New master password (or blank to cancel): ").strip()
    if not new_pw:
        print("Cancelled.")
        return
    if new_pw != input("Confirm new master password: "):
        print("Mismatch. Not changed.")
        return
    users[username]["EasyPass_pw"] = new_pw
    save_users(users)
    print("Master password updated.")

def manage_service(users: Dict, username: str) -> None:
    if username not in users:
        print("User not found.")
        return
    services = [k for k in users[username].keys() if k != "EasyPass_pw"]
    if services:
        print("Saved services:", ", ".join(services))
    else:
        print("No saved services.")
    service = input("Service to add/update (blank to cancel): ").strip().lower()
    if not service:
        print("Cancelled.")
        return
    pw = input("Password (or 'g' to generate): ").strip()
    if pw.lower() == "g":
        length = input("Length (default 12): ").strip()
        pw = password_generator(length if length.isdigit() else 12)
        print("Generated:", pw)
    if service in users[username]:
        if input(f"Overwrite {service}? (y/n): ").strip().lower() != "y":
            print("Not changed.")
            return
    users.setdefault(username, {})[service] = pw
    save_users(users)
    print(f"Saved {service}.")

if __name__ == "__main__":
    users = load_users()
    print("EasyPass")
    while True:
        opt = input("\n1) Login\n2) Create user\nQ) Quit\n> ").strip().upper()
        if opt == "1":
            user = login(users)
            if user is None:
                continue
            # post-login menu
            while user is not None and user in users:
                cmd = input("\n1) Generate"
                            "\n2) Check & Save"
                            "\n3) List services\n4) Add/Update service\n5) Change master pw\nL) Logout\n> ").strip().upper()
                if cmd == "1":
                    length = input("Length (12): ").strip()
                    print("Generated:", password_generator(length if length.isdigit() else 12))
                elif cmd == "2":
                    pw = input("Password to check: ")
                    score, label = strength_checker(pw)
                    print(f"Strength: {label} ({score}/5)")
                    if input("Save to service? (y/n): ").strip().lower() == "y":
                        service = input("Service name: ").strip().lower()
                        if service in users.get(user, {}):
                            if input("Overwrite? (y/n): ").strip().lower() == "y":
                                users[user][service] = pw
                                save_users(users)
                                print("Updated.")
                            else:
                                print("Not saved.")
                        else:
                            if input(f"Save under '{service}'? (y/n): ").strip().lower() == "y":
                                users.setdefault(user, {})[service] = pw
                                save_users(users)
                                print("Saved.")
                elif cmd == "3":
                    _ = [print(" -", s) for s in users.get(user, {}) if s != "EasyPass_pw"] #atm this doesnt show the passwords to us only the 
                elif cmd == "4":
                    manage_service(users, user)
                elif cmd == "5":
                    change_password(users, user)
                elif cmd == "L":
                    print("Logged out.")
                    user = None
                    break
                else:
                    print("Choose valid option.")
        elif opt == "2":
            new_user(users)
        elif opt == "Q":
            print("Goodbye.")
            break
        else:
            print("Choose 1, 2 or Q.")
