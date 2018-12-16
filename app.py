from flask import Flask, jsonify
import random

from quotes import funny_quotes

app = Flask(__name__)

@app.route("/api/funny")
def serve_funny_qotes():
	quotes = funny_quotes()
	no_of_quotes = len(quotes)
	selected_quote = quotes[random.randint(0, no_of_quotes -1)]
	return jsonify(selected_quote)

if __name__ == "__main__":
	app.run(debug=True)