from string import ascii_uppercase 
from typing import List
from .CaesarCipher import CaesarCipher
from .AtbashCipher import AtbashCipher


def get_alphabet() -> List:
    letters= list(ascii_uppercase)
    return letters