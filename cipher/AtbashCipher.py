class AtbashCipher():
    def __init__(self, alphabet: list):
        self.alphabet = alphabet

    def encrypt_decrypt_text(self, text: str) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        output_text = []
        for letter in text:
            letter_index = self.alphabet.index(letter) 
            output_index = ((alphabet_len - 1) * letter_index + (alphabet_len - 1)) % alphabet_len
            output_letter = self.alphabet[output_index]
            output_text.append(output_letter)
        return "".join(output_text)