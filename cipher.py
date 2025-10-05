import string

def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts text using the Caesar cipher.
    :param text: The string to be processed.
    :param shift: The integer key for shifting letters.
    :param mode: 'encrypt' or 'decrypt'.
    :return: The processed string.
    """
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    
    if mode.lower() == 'decrypt':
        # Swap alphabets for decryption
        table = str.maketrans(shifted_alphabet, alphabet)
    else: # Default to encrypt
        table = str.maketrans(alphabet, shifted_alphabet)

    # Preserve case by processing lower and upper case separately
    # All non-alphabetic characters are left unchanged
    return text.translate(table)

# --- Main execution block ---
if __name__ == "__main__":
    print("🔒 Caesar Cipher Encryptor/Decryptor 🔒")
    
    message = input("Enter your message: ")
    
    while True:
        try:
            shift_key = int(input("Enter the shift key (a number from 1 to 25): "))
            if 1 <= shift_key <= 25:
                break
            else:
                print("Invalid key. Please enter a number between 1 and 25.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    while True:
        choice = input("Choose an option: (e)ncrypt or (d)ecrypt: ").lower()
        if choice in ['e', 'encrypt', 'd', 'decrypt']:
            mode = 'encrypt' if choice.startswith('e') else 'decrypt'
            break
        else:
            print("Invalid choice. Please enter 'e' or 'd'.")

    result = caesar_cipher(message, shift_key, mode)

    print("\n" + "="*30)
    print(f"  Original message:  {message}")
    print(f"  Processed message: {result}")
    print("="*30 + "\n")
