import random
import string

# Function to generate a secure password
def generate_password(strength):
    if strength == "normal":
        length = 8
        characters = string.ascii_letters + string.digits  
    elif strength == "medium":
        length = 12
        characters = string.ascii_letters + string.digits + string.punctuation  
    elif strength == "hard":
        length = 16
        characters = string.ascii_letters + string.digits + string.punctuation
    elif strength == "veryhard":
        length = 20
        characters = string.ascii_letters + string.digits + string.punctuation + "!@#$%^&*()_+-=[]{}|;:',.<>?/`~"  
    else:
        return "Invalid strength level!"

    password = ''.join(random.SystemRandom().choice(characters) for _ in range(length))
    return password

# Function to generate a random email
def generate_email():
    domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]
    name_length = random.randint(6, 12)  
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=name_length))
    domain = random.choice(domains)
    return f"{username}@{domain}"

# Main loop
while True:
    print("\nOptions:")
    print("1 - Generate Password")
    print("2 - Generate Email")
    print("3 - Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        strength = input("Enter password strength (normal, medium, hard, veryhard): ").strip().lower()
        print("Generated Password:", generate_password(strength))
    elif choice == "2":
        print("Generated Email:", generate_email())
    elif choice == "3" or choice.lower() == "exit":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")