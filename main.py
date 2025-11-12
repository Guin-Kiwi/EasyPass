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
        menu = input("\n1) Login\n2) Create user\nQ) Quit\n> ").strip().upper()
        if menu == "1":
            user = login(users)
            if user is None:
                continue
            while user is not None and user in accounts:
                choice = input("\n1) Generate and check"
                            "\n2) Save"
                            "\n3) update"
                            "\n4) read"
                            "\n5) delete")
                if choice == "1":
                    generate()
                    check()
                elif choice == "2":
                    account_save()
                elif choice == "3":
                    account_update()
                elif choice == "4":
                    account_read()
                elif choice == "5":
                    account_delete()
                elif choice == "L":
                    print("Logged out.")
                    user = None
                    break
                else:
                    print("Choose valid option.")
        elif opt == "2":
            new_account()
        elif opt == "Q":
            print("Goodbye.")
            break
        else:
            print("Choose 1, 2 or Q.")


if __name__ == "__main__":
    main()
