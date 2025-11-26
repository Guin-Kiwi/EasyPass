def password_generator(length):       # Defines a function that generates a random password of a given length.
    chars = string.ascii_letters + string.digits + string.punctuation  
    # chars: all lowercase and uppercase letters, digits, and punctuation characters.

    return "".join(random.choice(chars) for _ in range(length))  
    # Builds a string by randomly picking 'length' characters from chars, then returns that string.


def strength_checker(password):       # Defines a function that evaluates the strength of a password.
    if len(password) < 4:             # If the password is shorter than 4 characters:
        return "The password should be at least 4 characters long"  # Returns a message about minimum length.
    if " " in password:               # If the password includes a space character:
        return "Your password must not contain spaces"              # Returns a message prohibiting spaces.

    has_lower = any(c.islower() for c in password)  # True if any character is lowercase.
    has_upper = any(c.isupper() for c in password)  # True if any character is uppercase.
    has_special = any(c in string.punctuation for c in password)  # True if any char is a punctuation symbol.
    long_enough = len(password) >= 8                # True if password length is at least 8.

    score = sum([has_lower, has_upper, has_special, long_enough])  
    # Converts each boolean to int (True=1, False=0) and sums them up to compute a score.

    if score == 4:                   # If all four criteria are met:
        return "Strong password"     # Returns strong.
    elif score in (2, 3):            # If 2 or 3 criteria are met:
        return "Medium password"     # Returns medium.
    elif score == 1:                 # If only 1 criterion is met:
        return "Weak password"       # Returns weak.
    else:                            # If score is 0 (no criteria met):
        return "Very weak password"  # Returns very weak.


def choose_password():               # Defines a function that lets the user choose or generate a password.
    """Loop until user accepts a password (generated or own)."""  # Docstring explaining the function.
    while True:                      # Infinite loop until the user confirms a password.
        choice = input("Do you want a generated password? (Y/N): ").strip().upper()
        # Asks if user wants a generated password, strips spaces, converts to uppercase.

        if choice == "Y":            # If user chooses generated password:
            try:                     # Try converting the length input to int.
                length = int(input("Enter password length: "))  # Asks for desired password length.
                if length <= 0:      # If length is zero or negative:
                    print("Length must be positive.")  # Warns user.
                    continue         # Asks again.
            except ValueError:       # If user does not enter a valid number:
                print("Please enter a valid number.")  # Error message.
                continue             # Repeats loop.

            password = password_generator(length)  # Generates a password of given length.
            print("Generated password:", password) # Shows generated password to user.
        else:                        # If user does not choose "Y" (anything else is treated as no):
            password = input("Enter your password: ")  # Asks the user to enter their own password.

        strength = strength_checker(password)  # Evaluates the password strength.
        print("Password strength:", strength)  # Displays the strength result.

        keep = input("Do you want to keep this password? (Y/N): ").strip().upper()
        # Asks if user wants to keep the current password.

        if keep == "Y":              # If user confirms:
            return password          # Returns the chosen password.

        print("Okay, let's try again.\n")  # Otherwise, informs user and restarts the loop.
