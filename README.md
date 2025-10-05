# 🍕 PizzaRP – Pizzeria Reference Project (Console)

> 🚧 This is a template repository for student project in the course Programming Foundations at FHNW, BSc BIT.  
> 🚧 Do not keep this section in your final submission.

This project is intended to:

- Practice the complete process from **problem analysis to implementation**
- Apply basic **Python** programming concepts learned in the Programming Foundations module
- Demonstrate the use of **console interaction, data validation, and file processing**
- Produce clean, well-structured, and documented code
- Prepare students for **teamwork and documentation** in later modules
- Use this repository as a starting point by importing it into your own GitHub account.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.

# 🍕 TEMPLATE for documentation

## 📝 Analysis

**Problem**
> 🚧 Describe the real-world problem your application solves. (Not HOW, but WHAT)

💡 Different websites require "strong" passwords, which are hard to generate and difficult to remember, 
users need an easy and quick solution for password generation and storage.

**Scenario**
> 🚧 Describe when and how a user will use your application

💡 When users want to register or signup on a new platform requiring a complicated password 
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

> 🚧 In this section, document how your project fulfills each criterion.  
---
The application interacts with the user via the console. Users can:
- Define password requirements, check or Generate password
- Manage User Specific account passwords
- Regenerate a new password, Copy the password

---


### 2. Data Validation

The application validates all user input to ensure data integrity and a smooth user experience. 

When the user chooses a difficulty of the generated password, the program checks if the entered password corresponds to the requirements and if its not, an error occurs and the input is requested again.

- **Password check:** When the user enters a password, the program checks if the input corresponds to the chosen requirements level:
	```python
	
	```
	This ensures only valid password generation.

- **Account check:** When entering an account credentials the program checks if the account (including password) already exists, and if so suggests an update of the password: 
	```python
	
	```

- **Password strength requirements:** Depending on how many of the requirements the password is fulfilling, we deem it weak, medium or strong.
- Requirements:

At least one lowercase letter

At least one uppercase letter

At least one special character

The password must not contain spaces 

The password must be at least 8 characters long

If 1 requirement is met -> weak password
If 2 or 3 are met -> medium password
If more than 3 are met -> strong password


	else:
			print("⚠️ Invalid choice.")
	```

These checks prevent crashes and guide the user to provide correct input, matching the validation requirements described in the project guidelines.

---

---


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
> 🚧 Adjust if needed.
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

> 🚧 Fill in the names of all team members and describe their individual contributions below. Each student should be responsible for at least one part of the project.

| Name       | Contribution                                 |
|------------|----------------------------------------------|
| Student A  |                                              |
| Student B  |                                              |
| Student C  |                                              |


## 🤝 Contributing

> 🚧 This is a template repository for student projects.  
> 🚧 Do not change this section in your final submission.

- Use this repository as a starting point by importing it into your own GitHub account.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.

## 📝 License

This project is provided for **educational use only** as part of the Programming Foundations module.  
[MIT License](LICENSE)
