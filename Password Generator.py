import string
import random

def generate_password(length, complexity):
    # Define the character sets for each complexity level
    complexity_sets = {
        1: string.ascii_letters,
        2: string.ascii_letters + string.digits,
        3: string.ascii_letters + string.digits + string.punctuation
    }

    # Generate the password using a random sample from the appropriate character set
    password = ''.join(random.choice(complexity_sets[complexity]) for _ in range(length))

    # Ensure the password contains at least one character from each complexity level
    for level in range(1, complexity):
        if not any(char in complexity_sets[level] for char in password):
            password = password[:level-1] + random.choice(complexity_sets[level]) + password[level-1:]

    return password

# Get user input for password length and complexity
length = int(input("Enter the desired password length: "))
complexity = int(input("Enter the desired password complexity (1-3): "))

# Generate and display the password
password = generate_password(length, complexity)
print("Generated password:", password)