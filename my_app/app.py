""""""
from flask import Flask

from my_app.routes import register_routes
from my_app.src.db import DatabaseConnection, DatabaseConfig, PostgreSQLConnection
from my_app.src.service import CachingDecorator, DataService
from my_app.src.users import UserFactory, AdminUser, NormalUser


PORT = 5010

def create_app(config_filename="config.json"):
    app = Flask(__name__)
    #app.config.from_json(config_filename)

    # The single instance
    db_connection = DatabaseConnection(
        PostgreSQLConnection(),
        config=DatabaseConfig(
            host="localhost",
            port=5432,
            name="my_db",
            user="admin",
            password="admin"
        )
    )

    # Wrap our data service with the caching decorator
    data_service = CachingDecorator(DataService())

    UserFactory.register_user_type("admin", AdminUser)
    UserFactory.register_user_type("normal", NormalUser)

    app = register_routes(app, data_service)

    return db_connection, app

db_connection, app = create_app()


if __name__ == "__main__":
    app.run(debug=True, port=PORT)
