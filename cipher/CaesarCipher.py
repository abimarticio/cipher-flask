from cipher import ALPHABET


class CaesarCipher():
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_decrypt_text(self, text: str, mode: str = "encrypt", key: int = 1) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        output_text = []
        for letter in text:
            letter_index = self.alphabet.index(letter)
            if mode == "encrypt":
                output_index = (letter_index + key) % alphabet_len
            elif mode == "decrypt":
                output_index = (letter_index - key) % alphabet_len
            output_letter = self.alphabet[output_index]
            output_text.append(output_letter)
        return "".join(output_text)