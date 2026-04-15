def caesar_cipher(text, shift, mode):
    result = ""
    
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        # Encrypt/Decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt/Decrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Keep spaces and punctuation as they are
        else:
            result += char
            
    return result

def main():
    print("--- Caesar Cipher Program ---")
    
    # Get user input
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode! Please choose 'encrypt' or 'decrypt'.")
        return

    message = input("Enter your message: ")
    
    try:
        shift_value = int(input("Enter the shift value (a number): "))
    except ValueError:
        print("Invalid input! Shift value must be a number.")
        return

    # Perform the operation
    translated_text = caesar_cipher(message, shift_value, mode)
    
    print(f"\nResulting Text: {translated_text}")

if __name__ == "__main__":
    main()