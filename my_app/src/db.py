""""""

class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = cls._connect_to_db()
        return cls._instance

    @classmethod
    def _connect_to_db(cls):
        # Pseudo code for DB connection
        print("Establishing new database connection...")
        return "DB_CONNECTION_OBJECT"
