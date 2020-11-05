from cipher import AtbashCipher, get_alphabet

def AtbashMain():
    alphabet = get_alphabet()
    Atbash = AtbashCipher(alphabet=alphabet)
    while True:
        user_input = input("Enter text you want to encrypt or decrypt: ")
        if user_input != "":
            break
        elif user_input == "":
            continue
    encrypted_decrypted_text = Atbash.encrypt_decrypt_text(text=user_input)
    print(encrypted_decrypted_text)

if __name__ == "__main__":
    AtbashMain()