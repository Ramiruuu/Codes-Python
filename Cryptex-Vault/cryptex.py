from cryptography.fernet import Fernet
import sys

# Generate a key and save it to a file (only needed once)
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved to secret.key")

# Load the encryption key from a file
def load_key():
    try:
        with open("secret.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("Key file not found. Please generate a key first.")
        sys.exit(1)

# Encrypt text
def encrypt_text(text):
    key = load_key()
    fernet = Fernet(key)
    encrypted_text = fernet.encrypt(text.encode())
    return encrypted_text

# Decrypt text
def decrypt_text(encrypted_text):
    key = load_key()
    fernet = Fernet(key)
    decrypted_text = fernet.decrypt(encrypted_text).decode()
    return decrypted_text

# Encrypt a file
def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)
    print(f"{filename} has been encrypted.")

# Decrypt a file
def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    print(f"{filename} has been decrypted.")

# Menu
def main():
    print("Encryption/Decryption Program")
    print("1. Generate Key")
    print("2. Encrypt Text")
    print("3. Decrypt Text")
    print("4. Encrypt File")
    print("5. Decrypt File")
    choice = input("Choose an option: ")

    if choice == "1":
        generate_key()
    elif choice == "2":
        text = input("Enter text to encrypt: ")
        encrypted = encrypt_text(text)
        print(f"Encrypted text: {encrypted}")
    elif choice == "3":
        encrypted_text = input("Enter text to decrypt: ").encode()
        try:
            decrypted = decrypt_text(encrypted_text)
            print(f"Decrypted text: {decrypted}")
        except Exception as e:
            print(f"Decryption failed: {e}")
    elif choice == "4":
        filename = input("Enter the filename to encrypt: ")
        encrypt_file(filename)
    elif choice == "5":
        filename = input("Enter the filename to decrypt: ")
        decrypt_file(filename)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main
