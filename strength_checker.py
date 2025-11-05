import string

def strength_checker(password:str):
    if len(password) < 4:
        return "The password should be at least 4 charakters long"
    
    if " " in password:
        return "Your password must not contain spaces"

    has_lower = False
    has_upper = False
    has_special = False
    long_enough = len(password) >= 8

    for ch in password:
        if ch.islower():
            has_lower = True
        elif ch.isupper():
            has_upper = True
        elif ch in string.punctuation:
            has_special = True

    # Count how many requirements are met
    score = 0
    if has_lower:
        score += 1
    if has_upper:
        score += 1
    if has_special:
        score += 1
    if long_enough:
        score += 1

    # Decide strength
    if score == 1:
        return "Weak password"
    elif score in (2, 3):
        return "Medium password"
    elif score == 4:
        return "Strong password"
    else:
        return "Very weak password"


# Example use
pw = input("Enter your password: ")
print(strength_checker(pw))
