import re

def check_password_strength(password):
    length = len(password) >= 8
    uppercase = re.search(r"[A-Z]", password)
    lowercase = re.search(r"[a-z]", password)
    digit = re.search(r"[0-9]", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    if length and uppercase and lowercase and digit and special:
        return "Strong Password"
    elif length and (digit or special):
        return "Medium Password"
    else:
        return "Weak Password"

password = input("Enter your password: ")
result = check_password_strength(password)
print("Password Strength:", result)
