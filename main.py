def encrypt_caesar(plaintext, shift):
    plaintext = plaintext.lower()  # Convert to lowercase
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            shift_base = ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_caesar(ciphertext, shift):
    ciphertext = ciphertext.lower()  # Convert to lowercase
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shift_base = ord('a')
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    while True:
        choice = input("Enter 'e' to encrypt or 'd' to decrypt: ").lower()
        
        if choice == 'e':
            plaintext = input("Enter the plaintext: ").lower()  # Convert to lowercase
            shift = int(input("Enter the shift value: "))
            encrypted_text = encrypt_caesar(plaintext, shift)
            print(f"Encrypted text: {encrypted_text}")
        
        elif choice == 'd':
            ciphertext = input("Enter the ciphertext: ").lower()  # Convert to lowercase
            shift = int(input("Enter the shift value: "))
            decrypted_text = decrypt_caesar(ciphertext, shift)
            print(f"Decrypted text: {decrypted_text}")
        
        else:
            print("Invalid choice. Please enter 'e' or 'd'.")

if __name__ == "__main__":
    main()
