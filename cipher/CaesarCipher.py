# Atbash and Caesar cipher Flask app
# Copyright (C) 2020  Abigail Marticio

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
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
        encrypted_text = []
        for letter in text:
            letter_index = self.alphabet.index(letter)
            output_index = (letter_index + key) % alphabet_len
            output_letter = self.alphabet[output_index]
            encrypted_text.append(output_letter)
        return "".join(encrypted_text)

    def decrypt_text(self, text: str, key: int) -> str:
        """
        Returns the decrypted text using Caesar cipher

        Parameters
        ----------
        text: str
            The encrypted text to decrypt.
        key: int
            The cipher key to use.

        Returns
        -------
        str
            The decrypted text.

        """
        alphabet_len = len(self.alphabet)
        text = text.upper()
        decrypted_text = []
        for letter in text:
            letter_index = self.alphabet.index(letter)
            output_index = (letter_index - key) % alphabet_len
            output_letter = self.alphabet[output_index]
            decrypted_text.append(output_letter)
        return "".join(decrypted_text)
