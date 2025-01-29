""""""
from my_app.src.users import User


class UserRegisteredSubject:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, user):
        for observer in self._observers:
            observer.update(user)

class WelcomeEmailObserver:
    def update(self, user: User):
        print(f"Sending welcome email to {user.username}")

class LoggingObserver:
    def update(self, user: User):
        print(f"Logging: New user registered -> {user.username}")

# Set up the subject and attach some observers
user_registered_subject = UserRegisteredSubject()
user_registered_subject.register_observer(WelcomeEmailObserver())
user_registered_subject.register_observer(LoggingObserver())
