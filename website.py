from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Some dummy data stored right in the Python memory (no database needed yet!)
my_profile = {
    "name": "Ren",
    "role": "Aspiring Full-Stack Developer",
    "current_status": "Coding my first API! 🚀"
}

quotes = [
    "Simplicity is the soul of efficiency. — Austin Freeman",
    "Make it work, make it right, make it fast. — Kent Beck",
    "Before software can be reusable it first has to be usable. — Ralph Johnson"
]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/profile', methods=['GET'])
def get_profile():
    # Send the profile info and a random quote
    return jsonify({
        "name": my_profile["name"],
        "role": my_profile["role"],
        "status": my_profile["current_status"],
        "quote": random.choice(quotes)
    })


@app.route('/api/status', methods=['POST'])
def update_status():
    # Let the frontend update the status
    data = request.json
    if "new_status" in data:
        my_profile["current_status"] = data["new_status"]
        return jsonify({"message": "Status updated successfully!", "status": my_profile["current_status"]})
    return jsonify({"error": "Invalid data"}, 400)


if __name__ == '__main__':
    app.run(port=5000)
