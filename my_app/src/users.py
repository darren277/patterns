""""""
from typing import Literal
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
    @staticmethod
    def create_user(user_type: Literal["admin", "normal"], username: str):
        if user_type == "admin":
            return AdminUser(username)
        elif user_type == "normal":
            return NormalUser(username)
        else:
            raise ValueError(f"Unknown user type: {user_type}")
