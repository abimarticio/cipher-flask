from cipher import CaesarCipher, get_alphabet

def caesarMain():
    alphabet = get_alphabet()
    Caesar = CaesarCipher(alphabet=alphabet)
    mode = input("Do you want to encrypt or decrypt? ")
    mode = mode.lower()
    if mode == "encrypt":
        user_input = input("Enter text you want to encrypt: ")
        shift = int(input("Key: "))
        encrypted_text = Caesar.encrypt_decrypt_text(text=user_input, mode=mode, key=shift)
        print(encrypted_text)
    elif mode == "decrypt":
        user_input = input("Enter text you want to decrypt: ")
        shift = int(input("Key: "))
        decrypted_text = Caesar.encrypt_decrypt_text(text=user_input, mode=mode, key=shift)
        print(decrypted_text)
    else:
            raise ValueError

if __name__ == "__main__":
    caesarMain()