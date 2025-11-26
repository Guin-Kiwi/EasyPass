# EasyPass - Password Generator and Checker Reference Project (Console)

This project is intended to:

- Practice the complete process from **problem analysis to implementation**
- Apply basic **Python** programming concepts learned in the Programming Foundations module
- Demonstrate the use of **console interaction, data validation, and file processing**
- Produce clean, well-structured, and documented code
- Prepare students for **teamwork and documentation** in later modules
- Use this repository as a starting point by importing it into your own GitHub account.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.

## 📝 Analysis

### Problem
As a user, it is difficult to come up with new passwords regularly. It's also hard to determine if their passwords are good enough to protect their valuable information. It happens often that the users forget their platform passwords. Those problems create an unnecessary mental load and cause frustration. 

### Scenario
Generate and store a password for a new account in a secure way.

input - account
output - file

### User stories: stakeholder (for whom?), functionality (what do they want?), benefit (why is it useful?)

	1. As a user, I want to create a strong password by using the password generator in order to have a strong and safe password without dpending too much timme coming up with it on my own.
	2. As a user, I want to be able to read my passwords and store them in one file so that I don't have to remember them at all times. 
	3. As a user, I want to update my passwords so that they stay secure and I minimize the risks of hacking. 
	4. As a user, I want to be able to delete my passwords when I no longer need them.
	5. As a user, I want my password secret so that no body else can access it. -> libraries

### Use cases: 
- Enter Login (gain access to the EasyPass user specific file)
- Generate or check validity of a new password before storage
- Save password/s from platform accounts in (user_name.txt)
- Remove password/s from platform accounts in (user_name.txt)
- Show passwords from platform accounts in (user_name.txt)

---

## ✅ Project Requirements

Each app must meet the following three criteria in order to be accepted (see also the official project guidelines PDF on Moodle):

1. Interactive app (console input)
2. Data validation (input checking)
3. File processing (read/write)

---

### 1. Interactive App (Console Input)
 
---
The application interacts with the user via the console. Users can perform the following steps:

1. User Login
   1. with each username a file is created with the purpose of saving passwords 
   2. it can be either saved or deleted by the user 

2. Check a password
	1. Judge password strength 
   

3. Generate a password
	1. Define password requirements 

4. Manage User Specific account passwords
	1. Create a password for a platform account 
	2. Read passwords for different platform accounts
	3. Update passwords for platform accounts 
	4. Delete a platform account password entry 

---


### 2. Data Validation

The application validates all user input to ensure data integrity and a smooth user experience. 

### Account Check

When the user enters a login name, the program checks within the users.json for their username as the a key. If the account doesn't exist yet, the user is prompted to create a user and is returned to the previous menu.

	`def login(accounts):
    while True:
        nickname = input("Enter your nickname: ").strip().lower()
        if not nickname:
            print("Please enter a nickname.")
            continue

        if nickname not in accounts:
            print("User not found. Please create a new EasyPass nickname.")
            return None

        print("Login success.")
        return nickname`
### Create a User

	´def create_user(accounts):
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
        return nickname´

### User Data Management

	´def manage_accounts(accounts, user):
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
            print("Choose a valid option.")´

### Password creation: manual or generated

Need to write how it works.

	´def choose_password():
    """Loop until user accepts a password (generated or own)."""
    while True:
        choice = input("Do you want a generated password? (Y/N): ").strip().upper()

        if choice == "Y":
            try:
                length = int(input("Enter password length: "))
                if length <= 0:
                    print("Length must be positive.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
                continue

            password = password_generator(length)
            print("Generated password:", password)
        else:
            password = input("Enter your password: ")

        strength = strength_checker(password)
        print("Password strength:", strength)

        keep = input("Do you want to keep this password? (Y/N): ").strip().upper()
        if keep == "Y":
            return password

        print("Okay, let's try again.\n")´

### Password generation

The program asks the user the character length of the password to be generated.  A random string is generated and returned to the password creation function.

	`def password_generator(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))`


### Password validation and strength assessment: 

The program checks if the entered password corresponds to the requirements and if it doesn't, an error occurs and the input is requested again.
The password must meet all the requirements in order to be valid as a password

Depending on how many of the requirements the password is fulfilling, we deem it weak, medium or strong.
  
  Requirements:
1. At least one lowercase letter
2. At least one uppercase letter
3. At least one special character 
4. The password must be at least 8 characters long

**Criteria**

If 1 requirement is met -> weak password

If 2 or 3 are met -> medium password

If all 4 are met -> strong password


	`def strength_checker(password):
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
        return "Very weak password"`


### 3. File Processing

The application writes and reads data using a json file with a nested dictionary structure :

- **Input and Output file:** `users.json` — Contains the accounts and associated passwords for the users

	`def create_user(accounts):
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
        return nickname`
  
## ⚙️ Implementation

### Technology
- Python 3.x
- Environment: GitHub Codespaces
- No external libraries

### 📂 Repository Structure
```text
PizzaRP/
├── main.py             # main program logic (console application)
├── users.json       # Users password management info (input and output data file)
├── docs/               # optional screenshots or project documentation
└── README.md           # project description and milestones
```

### How to Run

1. Open the repository in **GitHub Codespaces**
2. Open the **Terminal**
3. Run:
	```bash
	python3 main.py
	```

### Libraries Used

- `os`: Used for file and path operations, such as checking if the menu file exists and creating new files.
- `glob`: Used to find all invoice files matching a pattern (e.g., `user_name.txt`) to determine the next invoice number.

These libraries are part of the Python standard library, so no external installation is required. They were chosen for their simplicity and effectiveness in handling file management tasks in a console application.


## 👥 Team & Contributions


| Name                  | Contribution                                 |
|-----------------------|----------------------------------------------|
| Marta Greschuk        |                                              |
| Polina Yemelianenkova |                                              |
| Ayla Allen            |                                              |


## 🤝 Contributing

- Use this repository as a starting point by importing it into your own GitHub account or VScode on Desktop.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.

## 📝 License

This project is provided for **educational use only** as part of the Programming Foundations module.  
[MIT License](LICENSE)
