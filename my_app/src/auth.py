""""""
from abc import ABC, abstractmethod


class AuthStrategy(ABC):
    @abstractmethod
    def authenticate(self, username: str, password_or_token: str):
        pass

class BasicAuthStrategy(AuthStrategy):
    def authenticate(self, username: str, password: str) -> bool:
        print("Authenticating with BasicAuthStrategy...")
        return username == "admin" and password == "secret"

class TokenAuthStrategy(AuthStrategy):
    def authenticate(self, username: str, token: str) -> bool:
        print("Authenticating with TokenAuthStrategy...")
        return token == "valid_api_token"

class AuthContext:
    def __init__(self, strategy: AuthStrategy):
        self._strategy = strategy

    def login(self, username: str, credential: str) -> bool:
        return self._strategy.authenticate(username, credential)
