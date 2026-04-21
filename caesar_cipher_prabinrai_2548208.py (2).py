# Name: Prabin Rai
# Student ID: 2548208

import os

def welcome():
    """Displays the welcome message to the user."""
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.\n")

def enter_message():
    """
    Prompts user to enter a valid mode (encrypt/decrypt),
    message, and shift number. Returns mode, message (uppercase), and shift.
    """
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d)? ").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid Mode")

    while True:
        message = input(f"What message would you like to {'encrypt' if mode == 'e' else 'decrypt'}: ")
        shift = input("What is the shift number: ")
        if shift.isdigit():
            return mode, message.upper(), int(shift)
        else:
            print("Invalid Shift")

def encrypt(message, shift):
    """
    Encrypts a message using Caesar Cipher.
    Returns the encrypted message in uppercase.
    """
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shifted_char = chr((ord(char.upper()) - ord('A') + shift) % 26 + ord('A'))
            encrypted_message += shifted_char
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, shift):
    """
    Decrypts a message using Caesar Cipher by reversing the shift.
    Returns the decrypted message in uppercase.
    """
    return encrypt(message, -shift)

def process_file(filename, mode, shift):
    """
    Reads lines from the given filename and encrypts/decrypts
    based on the mode. Returns a list of processed messages.
    """
    messages = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                messages.append(line.strip())
    except FileNotFoundError:
        print("File not found.")
    return [encrypt(msg, shift) if mode == 'e' else decrypt(msg, shift) for msg in messages]

def is_file(filename):
    """
    Returns True if the file exists, otherwise False.
    """
    return os.path.isfile(filename)

def write_messages(messages):
    """
    Writes a list of messages to results.txt, one message per line.
    """
    with open('results.txt', 'w') as file:
        for message in messages:
            file.write(f"{message}\n")

def message_or_file():
    """
    Prompts the user for mode (e/d), input method (file/console),
    and returns mode, message (or None), filename (or None).
    """
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid Mode")

    while True:
        source = input("Would you like to read from a file (f) or the console (c)? ").lower()
        if source in ['f', 'c']:
            break
        else:
            print("Invalid Source")

    if source == 'c':
        message = input(f"What message would you like to {'encrypt' if mode == 'e' else 'decrypt'}: ")
        return mode, message.upper(), None
    else:
        while True:
            filename = input("Enter a filename: ")
            if is_file(filename):
                break
            else:
                print("Invalid Filename")
        return mode, None, filename

def main():
    """Main function to run the Caesar Cipher program."""
    welcome()

    while True:
        mode, message, filename = message_or_file()
        shift = int(input("What is the shift number: "))

        if filename:
            messages = process_file(filename, mode, shift)
            write_messages(messages)
            print("Output written to results.txt")
        elif message:
            result = encrypt(message, shift) if mode == 'e' else decrypt(message, shift)
            print(result)

        while True:
            another = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
            if another in ['y', 'n']:
                break
            else:
                print("Invalid input")
        if another != 'y':
            print("Thanks for using the program, goodbye!")
            break

if __name__ == "__main__":
    main()
