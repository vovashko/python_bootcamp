alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift):
    result = ""
    for char in text:
        if char in alphabet:
            result += alphabet[(alphabet.index(char) + shift) % len(alphabet)]
        else:
            result += char

    return result

while True:
    option = input("Enter 'e' for encryption or 'd' for decryption: ").lower()
    if option == 'exit':
        break
    if option not in ['e', 'd', 'exit']:
        print("Invalid option")
        continue 
    text = input("Enter the text: ").lower()
    shift = int(input("Enter the shift: "))
    

    if option == 'e':
        print(f"Here is the result of the encryption: {encrypt(text, shift)}")
    else:
        print(f"Here is the result of the decryption:{encrypt(text, -shift)}")

