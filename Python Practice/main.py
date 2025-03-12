import hashlib
import re

# Function to validate email
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

# Function to encrypt password using SHA-256
def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to register a user
def register_user():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if not is_valid_email(email):
        return "Invalid email format!"

    encrypted_password = encrypt_password(password)
    confirmation_message = "Registration successful! A confirmation email has been sent."

    return {
        "email": email,
        "encrypted_password": encrypted_password,
        "message": confirmation_message
    }

# Run the registration process
registration_result = register_user()
print(registration_result)