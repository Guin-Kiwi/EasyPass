import os
import json
import random
import string
from typing import Dict, Tuple, Optional
import pathlib

def main():
    accounts = load_json()
    print("EasyPass")
    while True:
        menu = input("\n1) Login"
                "\n2) Create user"
                "\nQ) Quit\n> ").strip().upper()
        if menu == "1":
            user = login(accounts)
            if user is None:
                continue
            while user is not None and user in accounts:
                choice = input("\n1) Generate and check"
                            "\n2) Save"
                            "\n3) update"
                            "\n4) read"
                            "\n5) delete")
                if choice == "1":
                    pass #generate()
                    pass #check()
                elif choice == "2":
                    pass #account_save()
                elif choice == "3":
                    pass #account_update()
                elif choice == "4":
                    pass #account_read()
                elif choice == "5":
                    pass #account_delete()
                elif choice == "L":
                    print("Logged out.")
                    user = None
                    break
                else:
                    print("Choose valid menuion.")
        elif menu == "2":
            new_account()
        elif menu == "Q":
            print("Goodbye.")
            break
        else:
            print("Choose 1, 2 or Q.")
            
#this was just so I could check if the login was working, it can be overwritten of course
def load_json(path: str = "users.json"):
    with open(path, "r") as accounts:
        return json.load(accounts)     

def login(accounts: Dict):
    nickname = input("Enter your Nickname: ").strip().lower()
    if not nickname:
        print("Please enter a Nickname")
        return None
    account = accounts.get(nickname)
    if not isinstance(account, Dict):
        print("User not found.  Please create a new EasyPass Nickname.")
        return None
    elif isinstance(account, Dict):
        user = nickname
        print("Login Success.")
        return user
    else:
        print("An error has occurred, please try again")
        return None
    
def new_account(accounts: Dict):
    while True:
        nickname = input("Enter your Nickname: ").strip().lower()
        if not nickname:
            print("Please enter a Nickname")
            continue
        if nickname in accounts:
            print("That username already exists. Try another")
            continue
        # create an empty dict for services
        if nickname not in accounts:
            accounts[nickname] = {{"Google": {"user_id": "password"},
            "Twitter": {"user_id": "password"},
            "Reddit": {"user_id": "password"},
            "Github": {"user_id": "password"},
            "Meta": {"user_id": "password"}}}
            # account_save(accounts)  Needs to be added.
            print(f"Created account '{nickname}'.")
            return nickname
        else:
            print("Something went wrong")
            break

if __name__ == "__main__":
    main()
