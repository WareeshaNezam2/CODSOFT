print("~~~~~~~~~~~~~~~~~~~~~~~~PASSWORD GENERATOR~~~~~~~~~~~~~~~~~~~")
import random
import string

def generate_password(length=12, uppercase=True, digits=True, special_chars=True):
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    digits = input("Include digits? (yes/no): ").lower() == 'yes'
    special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    generated_password = generate_password(length, uppercase, digits, special_chars)
    print("Generated Password:", generated_password)

if __name__ == "__main__":
    main()


