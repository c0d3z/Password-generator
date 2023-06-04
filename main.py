import random

# Define the characters that can be used in the password
LOWER_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SYMBOLS = "!#$%&()*+,-./:;<=>?@[\\]^_`{|}~"

# Combine the characters into a single list
ALL_CHARACTERS = list(LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SYMBOLS)

# Define a list of common English words to avoid in passwords
COMMON_WORDS = [
    "password",
    "123456",
    "qwerty",
    "letmein",
    "monkey",
    "football",
    "iloveyou",
    "admin",
    "welcome",
    "abc123",
    "sunshine",
    "master",
    "hottie",
    "charlie",
    "solo",
    "princess",
    "dragon",
    "access",
    "flower",
]

# Define a list of banned characters to avoid in passwords
BANNED_CHARACTERS = ["'", '"', "\\"]


def generate_password() -> str:
    # Prompt the user for the desired length of the password
    while True:
        try:
            password_length = int(input("Enter password length (8-64): "))
            if not 8 <= password_length <= 64:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter an integer between 8 and 64.")

    # Generate a password with various rules and constraints
    while True:
        password = ""

        # Add at least one lowercase letter
        password += random.choice(LOWER_LETTERS)

        # Add at least one uppercase letter
        password += random.choice(UPPER_LETTERS)

        # Add at least one digit
        password += random.choice(NUMBERS)

        # Add at least one symbol
        password += random.choice(SYMBOLS)

        # Add additional characters up to the desired length
        for i in range(password_length - 4):
            password += random.choice(ALL_CHARACTERS)

        # Check if the password contains a common word or a banned character
        if any(word in password.lower() for word in COMMON_WORDS) or any(
            char in password for char in BANNED_CHARACTERS
        ):
            continue

        # Check if the password has unique characters
        if len(set(password)) < password_length:
            continue

        # Shuffle the characters of the password for added security
        password = "".join(random.sample(password, len(password)))

        # Return the generated password
        return password


# Generate and print a password
password = generate_password()
print("Your password is:", password)
