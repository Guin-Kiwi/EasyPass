import string

def strength_checker(password):

    score = 0  # counts how many requirements are met

    # Check for lowercase letter
    if any(c.islower() for c in password):
        score += 1

    # Check for uppercase letter
    if any(c.isupper() for c in password):
        score += 1

    # Check for special character
    if any(c in string.punctuation for c in password):
        score += 1

    # Check for length
    if len(password) >= 8:
        score += 1

    # Evaluate strength
    if score == 1:
        return "Weak password"
    elif score in [2, 3]:
        return "Medium password"
    elif score == 4:
        return "Strong password"
    else:
        return "Very weak password"


# Example usage:
user_password = input("Enter your password: ")
print(strength_checker(user_password))
