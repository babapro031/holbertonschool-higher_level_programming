# task_04_flask.py
from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

# Users dictionary in memory
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Root endpoint
@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"

# /data endpoint: list of usernames
@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(list(users.keys()))

# /status endpoint
@app.route("/status", methods=["GET"])
def status():
    return "OK"

# /users/<username> endpoint
@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# /add_user endpoint for POST requests
@app.route("/add_user", methods=["POST"])
def add_user():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add user
    users[username] = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", 0),
        "city": data.get("city", "")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201

# Run the Flask app
if __name__ == "__main__":
    app.run()
