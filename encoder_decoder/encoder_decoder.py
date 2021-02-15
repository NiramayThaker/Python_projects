alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt :- \n").lower()
text = input("Type your message :- \n").lower()
shift = int(input("Type the shift number :- \n"))


def encrypt(normal_text, number_of_shift):
    print("Encrypting user input")
    cipher_text = ""
    for letter in normal_text:
        position = alphabet.index(letter)   # will find the index(first) value of the given number
        new_position = position + number_of_shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encrypted cipher text is :- {cipher_text}")


def decrypt(ciper_text, shift_amount):
    plain_text = ""
    for letter in ciper_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"The decrypted form of text is :- {plain_text}")


if direction == 'encode':
    encrypt(normal_text=text, number_of_shift=shift)
elif direction == 'decode':
    decrypt(ciper_text=text, shift_amount=shift)
else:
    print("Invalid input")
