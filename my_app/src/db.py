""""""
from abc import ABC, abstractmethod

class IDatabaseConnection(ABC):
    @abstractmethod
    def connect(self) -> str:
        pass

class MySQLConnection(IDatabaseConnection):
    def connect(self) -> str:
        print("Connecting to MySQL...")
        return "MYSQL_CONNECTION_OBJECT"

class PostgreSQLConnection(IDatabaseConnection):
    def connect(self) -> str:
        print("Connecting to PostgreSQL...")
        return "POSTGRESQL_CONNECTION_OBJECT"


class DatabaseConnection:
    _instance = None

    def __new__(cls, connection_impl: IDatabaseConnection, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = connection_impl.connect()
        return cls._instance

    @classmethod
    def _connect_to_db(cls):
        # Pseudo code for DB connection
        print("Establishing new database connection...")
        return "DB_CONNECTION_OBJECT"


class DatabaseConfig:
    def __init__(self, host, port, name, user, password):
        self.host = host
        self.port = port
        self.name = name
        self.user = user
        self.password = password

    def __str__(self):
        return f"DatabaseConfig:URIString={self._uri_string()}"

    def _uri_string(self):
        return f"{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"

