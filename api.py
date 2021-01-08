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
from flask import Flask, request
from cipher import AtbashCipher, CaesarCipher


app = Flask(__name__)


@app.route("/atbash/encrypt", methods=["GET"])
def atbash_encrypt():
    """
    GET request for Atbash Encrypt.

    Request Parameters
    ----------
    text: str
        The input text.

    Returns
    -------
    str
        The Atbash cipher output.
    """
    text = request.args.get("text", default=None)
    encrypted_text = AtbashCipher()
    return f"text: {text} - encrypted text: {encrypted_text(text)}"


@app.route("/atbash/decrypt", methods=["GET"])
def atbash_decrypt():
    """
    GET request for Atbash Decrypt.

    Request Parameters
    ----------
    text: str
        The input text.

    Returns
    -------
    str
        The Atbash cipher output.
    """
    text = request.args.get("text", default=None)
    decrypted_text = AtbashCipher()
    return f"text: {text} - decrypted text: {decrypted_text(text)}"


@app.route("/caesar/encrypt", methods=["GET"])
def caesar_encrypt():
    """
    GET request for Caesar Encrypt.

    Request Parameters
    ----------
    text: str
        The input text.

    Returns
    -------
    str
        The Caesar cipher output.
    """
    text = request.args.get("text", default=None)
    key = request.args.get("key", default=None, type=int)
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text} - encrypted text: {encrypted_text}"


@app.route("/caesar/decrypt", methods=["GET"])
def caesar_decrypt():
    """
    GET request for Caesar Decrypt.

    Request Parameters
    ----------
    text: str
        The input text.

    Returns
    -------
    str
        The Caesar cipher output.
    """
    text = request.args.get("text", default=None)
    key = request.args.get("key", default=None, type=int)
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text} - decrypted text: {decrypted_text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
