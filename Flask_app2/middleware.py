from flask import request, jsonify

# Define a valid token (you can replace this with your own logic for token validation)
TOKEN = "mysecrettoken"

# Middleware: Token authentication check
def authenticate_token():
    token = request.headers.get("Authorization")
    
    # Check if the token is present and valid
    if not token or token != f"Bearer {TOKEN}":
        return jsonify({"error": "Unauthorized"}), 401
