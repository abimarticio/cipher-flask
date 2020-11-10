from cipher import ALPHABET


class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(self, text: str, key: int) -> str:
        """
        Returns the encrypted text using Caesar cipher

        Parameters
        ----------
        text: str
            The input text to encrypt.
        key: int
            The cipher key to use.

        Returns
        -------
        str
            The encrypted text.

        """
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
