import os
from Crypto.Cipher import AES
import base64

def pad(plaintext, block_size):
    padding_size = block_size - (len(plaintext) % block_size)
    padding = bytes([padding_size] * padding_size)
    return plaintext + padding

def encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)
    padded_plaintext = pad(plaintext.encode("utf-8"), AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return base64.b64encode(ciphertext).decode("utf-8")

def unpad(plaintext, block_size):
    padding = plaintext[-1]
    return plaintext[:-padding]

def decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_CBC)
    decoded_ciphertext = base64.b64decode(ciphertext)
    decrypted = cipher.decrypt(decoded_ciphertext)
    decrypted = unpad(decrypted, AES.block_size)

    return decrypted.rstrip(b"\x00").decode("utf-8")

# Generate a random 32-byte key for AES encryption
key = os.urandom(32)

# User input for plaintext and choice between encryption and decryption

choice = input("Choose (E)ncrypt or (D)ecrypt: ").upper()

if choice == "E":
    plaintext = input("Enter plaintext: ")
    encrypted = encrypt(plaintext, key)
    print("Plaintext:", plaintext)
    print("Encrypted:", encrypted)

elif choice == "D":
    ciphertext = input("Enter ciphertext: ")
    decrypted = decrypt(ciphertext, key)
    print("Ciphertext:", ciphertext)
    print("Decrypted:", decrypted)

else:
    print("Invalid choice.")
