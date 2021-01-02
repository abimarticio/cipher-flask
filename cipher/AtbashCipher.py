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


class AtbashCipher:
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
            output_index = (
                (alphabet_len - 1) * letter_index + (alphabet_len - 1)
            ) % alphabet_len
            output_letter = self.alphabet[output_index]
            output_text.append(output_letter)
        return "".join(output_text)
