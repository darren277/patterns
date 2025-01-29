""""""
from flask import Flask, request, jsonify

from my_app.src.auth import TokenAuthStrategy, BasicAuthStrategy, AuthContext
from my_app.src.db import DatabaseConnection
from my_app.src.events import user_registered_subject
from my_app.src.service import CachingDecorator, DataService
from my_app.src.users import UserFactory

app = Flask(__name__)

PORT = 5010

# The single instance
db_connection = DatabaseConnection()

# Wrap our data service with the caching decorator
data_service = CachingDecorator(DataService())


@app.route("/")
def home():
    return "Welcome to the Combined Patterns Demo!"

@app.route("/register", methods=["GET", "POST"])
def register_user():
    if request.method == "GET":
        page = """
<h1>Register User</h1>
<form method="POST">
    <label for="user_type">User Type:</label>
    <select name="user_type" id="user_type">
        <option value="normal">Normal</option>
        <option value="admin">Admin</option>
    </select>
    <br>
    <label for="username">Username:</label>
    <input type="text" name="username" id="username">
    <br>
    <button type="submit">Register</button>
</form>
        """
        return page

    #data = request.json
    data = request.form
    user_type = data.get("user_type", "normal")
    username = data.get("username", "guest")

    # Factory: create a new user of the given type
    user = UserFactory.create_user(user_type, username)

    # Observer: notify all observers about new registration
    user_registered_subject.notify_observers(user)

    return jsonify({"message": f"User {username} of type {user_type} registered successfully."})

@app.route("/login", methods=["POST"])
def login_user():
    data = request.json
    auth_type = data.get("auth_type", "basic")
    username = data.get("username")
    credential = data.get("credential")

    # Strategy: pick an authentication strategy
    if auth_type == "token": strategy = TokenAuthStrategy()
    else: strategy = BasicAuthStrategy()

    auth_context = AuthContext(strategy)
    success = auth_context.login(username, credential)

    return jsonify({"success": success, "message": "Logged in" if success else "Invalid credentials"})

@app.route("/data", methods=["GET"])
def get_data():
    query = request.args.get("query", "default")

    # Decorator (caching)
    result = data_service.get_data(query)
    return jsonify({"data": result})

if __name__ == "__main__":
    app.run(debug=True, port=PORT)
