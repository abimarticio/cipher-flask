from flask import Flask, request
from cipher import AtbashCipher, CaesarCipher


app = Flask(__name__)


@app.route("/atbash/encrypt", methods=["GET"])
def atbash_encrypt():
    text = request.args.get("text", default=None)
    encrypted_text = AtbashCipher()
    return f"text: {text} - encrypted text: {encrypted_text(text)}"


@app.route("/atbash/decrypt", methods=["GET"])
def atbash_decrypt():
    text = request.args.get("text", default=None)
    decrypted_text = AtbashCipher()
    return f"text: {text} - decrypted text: {decrypted_text(text)}"


@app.route("/caesar/encrypt", methods=["GET"])
def caesar_encrypt():
    text = request.args.get("text", default=None)
    key = request.args.get("key", default=None, type=int)
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text} - encrypted text: {encrypted_text}"


@app.route("/caesar/decrypt", methods=["GET"])
def caesar_decrypt():
    text = request.args.get("text", default=None)
    key = request.args.get("key", default=None, type=int)
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text} - decrypted text: {decrypted_text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
