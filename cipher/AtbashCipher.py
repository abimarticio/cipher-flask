from cipher import ALPHABET


class AtbashCipher():
    def __init__(self):
        self.alphabet = ALPHABET
   
    def __call__(self, text: str) -> str:
        return self.encrypt_decrypt_text(text)

    def encrypt_decrypt_text(self, text: str) -> str:
        """
        Returns the output of using Atbash cipher

        Parameters
        ----------
        text: str
            The input text.

        Returns
        -------
        str
            The Atbash cipher output.

        """
        alphabet_len = len(self.alphabet)
        text = text.upper()
        output_text = []
        for letter in text:
            letter_index = self.alphabet.index(letter) 
            output_index = ((alphabet_len - 1) * letter_index + (alphabet_len - 1)) % alphabet_len
            output_letter = self.alphabet[output_index]
            output_text.append(output_letter)
        return "".join(output_text)