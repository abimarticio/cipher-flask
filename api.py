from flask import Flask, request
from cipher import AtbashCipher, CaesarCipher


app = Flask(__name__)

@app.route("/atbash/encrypt", methods=["GET"])
def atbash_encrypt():
    text = request.args.get("text", default=None)
    encrypted_text = AtbashCipher()
    return f"text: {text} - encrypted text: {encrypted_text(text)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)