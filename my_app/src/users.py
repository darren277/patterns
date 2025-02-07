""""""
from typing import Literal, Dict, Type
from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, username: str):
        self.username = username

    @abstractmethod
    def get_role_permissions(self):
        pass

class AdminUser(User):
    def get_role_permissions(self) -> list:
        return ["read", "write", "delete"]

class NormalUser(User):
    def get_role_permissions(self) -> list:
        return ["read"]


class UserFactory:
    _user_types: Dict[str, Type[User]] = {}

    @staticmethod
    def register_user_type(user_type: str, user_class: Type[User]) -> None:
        UserFactory._user_types[user_type] = user_class

    @staticmethod
    def create_user(user_type: str, username: str) -> User:
        user_class = UserFactory._user_types.get(user_type)
        if user_class is None:
            raise ValueError(f"Unknown user type: {user_type}")
        return user_class(username)
