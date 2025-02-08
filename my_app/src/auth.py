""""""
from abc import ABC, abstractmethod


class AuthStrategy(ABC):
    '''
    The `credential` parameter can be a password or a token, depending on the strategy.
    New strategies can be added by implementing this interface potentially using other types of credential.
    '''
    @abstractmethod
    def authenticate(self, username: str, credential: str):
        pass

class BasicAuthStrategy(AuthStrategy):
    def authenticate(self, username: str, credential: str) -> bool:
        print("Authenticating with BasicAuthStrategy...")
        return username == "admin" and credential == "secret"

class TokenAuthStrategy(AuthStrategy):
    def authenticate(self, username: str, credential: str) -> bool:
        print("Authenticating with TokenAuthStrategy...")
        return credential == "valid_api_token"


class AuthContext:
    def __init__(self, strategy: AuthStrategy):
        self._strategy = strategy

    def login(self, username: str, credential: str) -> bool:
        return self._strategy.authenticate(username, credential)
