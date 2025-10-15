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

When the user enters a login name, the program checks for a .txt file with their username. If the account doesn't exist yet, the program will offer to generate a new password.

	`space for code`

### Password validation:
The program checks if the entered password corresponds to the requirements and if its not, an error occurs and the input is requested again.
The password must meet all the requirements in order to be valid as a password
1. minimum 4 characters
2. contain no spaces


	`space for code`


### Password strength requirements: 

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


	`space for code`
	


	



### 3. File Processing

The application writes and reads data using files:

- **Input and Output file:** `user_name.txt` — Contains the accounts and associated passwords for the user
		```
	- Google;strong;g7!R#x9VqP4sL@m2bZk8
  	- Reddit;medium;Blue-Planet-78
  	- Cara;weak;summer2024
		
		- The output file serves as a record for the user.
  
## ⚙️ Implementation

### Technology
- Python 3.x
- Environment: GitHub Codespaces
- No external libraries

### 📂 Repository Structure
```text
PizzaRP/
├── main.py             # main program logic (console application)
├── user_name.txt       # User password management info (input and output data file)
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

- Use this repository as a starting point by importing it into your own GitHub account.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.

## 📝 License

This project is provided for **educational use only** as part of the Programming Foundations module.  
[MIT License](LICENSE)
