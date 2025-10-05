# Password Generator and Checker Reference Project (Console)

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

**Problem**

Different websites require "strong" passwords, which are hard to generate and difficult to remember, 
users need an easy and quick solution for password generation and storage.

**Scenario**

When users want to register or signup on a new platform requiring a complicated password 
(e.g. numbers, special characters, Capitals, etc) they can use the application to generate one that works, 
and store it for later.

**User stories:**
1. As a user, I want my password to be legitimate.
2. As a user, I want to store my generated passwords.
3. As a user, I want to simplify the password generation process.
4. As a user, I want the generated password to be unique.

**Use cases:**
- User Login (choose user)
- Generate or check a new password before storage
- Store password/s from accounts in (user_passwords.csv)
- Remove password/s from accounts in (user_passwords.csv)
- Show passwords (user specific)

---

## ✅ Project Requirements

Each app must meet the following three criteria in order to be accepted (see also the official project guidelines PDF on Moodle):

1. Interactive app (console input)
2. Data validation (input checking)
3. File processing (read/write)

---

### 1. Interactive App (Console Input)
 
---
The application interacts with the user via the console. Users can:

- Login to their account
 		- create or delete
- Generate a password
 		- Define password requirements
- Check a password
 		- Judge password strength
- Manage User Specific account passwords
 		- Check passwords
 		- Change passwords
  		- Generate a new password
  		- Delete a password

---


### 2. Data Validation

The application validates all user input to ensure data integrity and a smooth user experience. 

When the user chooses a difficulty of the generated password, the program checks if the entered password corresponds to the requirements and if its not, an error occurs and the input is requested again.

- **User Login Check** When the user enters a login name, the program checks for a .txt file with their username, if there is no file the system creates an error that there is no account with that name and prompts them to create a new login
	```

- **Password check:** When the user enters a password, the program checks if the input corresponds to the chosen requirements level:
	```python
	
	```
	This ensures only valid password generation.

- **Account check:** When entering an account credentials the program checks if the account (including password) already exists, and if so suggests an update of the password: 
	```python
	
	```

- **Password strength requirements:** Depending on how many of the requirements the password is fulfilling, we deem it weak, medium or strong.
  
  Requirements:
1. At least one lowercase letter
2. At least one uppercase letter
3. At least one special character
4. The password must not contain spaces 
5. The password must be at least 8 characters long

**Criteria**

If 1 requirement is met -> weak password

If 2 or 3 are met -> medium password

If more than 3 are met -> strong password


`space for code`
	




### 3. File Processing

The application writes and reads data using files:

- **Input and Output file:** `user_name.txt` — Contains the accounts and associated passwords for the user
		```
		Google;strong;g7!R#x9VqP4sL@m2bZk8
  		Reddit;medium;Blue-Planet-78
  		Cara;weak;summer2024
		
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
- `glob`: Used to find all invoice files matching a pattern (e.g., `invoice_*.txt`) to determine the next invoice number.

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
