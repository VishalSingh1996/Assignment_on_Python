import re #This import is for regular function

def check_password_strength(password):# Checking minimum length of password
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password):# Checking for uppercase and lowercase letters
        return False
    if not re.search(r'\d', password): # Checking for digits entered by user
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password): # Checking for special characters by user input
        return False
    return True

def prompt_for_strong_password():
    while True:
        user_password = input("Enter a password: ")
        if check_password_strength(user_password):
            print("Password is strong.")
            break
        else:#for understanding user what's the criteria of password
            print("Password is weak. Please ensure it meets the criteria:")
            print("   - Is at least 8 characters long")
            print("   - Has both uppercase and lowercase letters")
            print("   - Contains at least one number")
            print("   - Includes at least one special character like : !@#$%^&*(),.?:{}|<>")
            print("Try again.\n")

if __name__ == "__main__":
    prompt_for_strong_password()