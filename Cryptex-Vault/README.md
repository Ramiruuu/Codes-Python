## Encryption and Decryption Program

This Python program allows you to encrypt and decrypt text and files using the Fernet encryption algorithm from the cryptography library. The program supports generating a key, encrypting text, decrypting text, encrypting files, and decrypting files.

Features
<ul>
  <li>Generate an encryption key and save it to a file (secret.key).</li>
  <li>Encrypt and decrypt text using the generated key.</li>
  <li>Encrypt and decrypt files in binary format.</li>
  <li> Simple command-line interface for easy usage.</li>
</ul>

## Requirements
Python 3.6 or higher

cryptography library


## Installation

1. Install Python: https://www.python.org/downloads/

2. Install the cryptography library using pip:

pip install cryptography



## How to Use

1. Generate an Encryption Key

Run the program and select Option 1. This will create a secret.key file in your current directory.

2. Encrypt Text

Choose Option 2 and enter the text you want to encrypt. The program will output the encrypted text.

3. Decrypt Text

Choose Option 3 and provide the encrypted text. The program will return the decrypted text if the correct key is available.

4. Encrypt a File

Choose Option 4 and specify the file you want to encrypt. This will replace the original file with its encrypted version.

5. Decrypt a File

Choose Option 5 and provide the encrypted file. The program will decrypt the file and replace the encrypted content with the original data.

## Example Usage

Encrypting and Decrypting Text:

Enter text to encrypt: HelloWorld123
Encrypted text: gAAAAABf1Hb... (truncated)

Encrypting and Decrypting a File:

Enter the filename to encrypt: sample.txt  
sample.txt has been encrypted.

Important Notes

Keep the secret.key file safe. Without it, you won’t be able to decrypt your data.

Always back up your files before encrypting them.

This program encrypts files in place, meaning the original file will be replaced with the encrypted/decrypted version.


## License

This project is licensed under the MIT License.
