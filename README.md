# patterns

## Object Oriented Design Patterns

### Strategy Pattern (Auth)

Example of the strategy pattern used to implement different authorization mechanisms: `my_app/src/auth.py`.

### Singleton Pattern (Database)

Example of the singleton pattern used to implement a database connection class: `my_app/src/db.py`.

### Observer Pattern (Events)

Example of the observer pattern used to implement an event stream processor for both logging and notifications: `my_app/src/events.py`.

### Decorator Pattern (Service and Caching)

Example of the decorator pattern used to implement a service layer with caching: `my_app/src/service.py`.

### Factory Pattern (Users)

Example of the factory pattern used for instantiating different kinds of users: `my_app/src/users.py`.

## SOLID Principles

### Single Responsibility Principle (SRP)

Principle: _A class should have one and only one reason to change._

Examples:
1. `my_app/src/users.py`: Each `User` subclass has its own role-specific logic (`AdminUser`, `NormalUser`).
2. `my_app/src/db.py`: Our original `DatabaseConnection` class was responsible for both ensuring only one instance (using the `Singleton` pattern), as well as connecting to the database. We will create separate `DatabaseConfig` and `DatabaseConnection` classes.

### Open/Closed Principle (OCP)

Principle: _Open for extension, but closed for modification._

Examples:
1. `my_app/src/auth.py`: Our authentication strategies can be extended without modifying the main `Auth` class. For example, if we wanted to add an `OAuthStrategy`, we would not have to touch the original `Auth` class.
2. `my_app/src/users.py`: We can implement a registration based approach so that we can create new user types dynamically, and register them at run time, without modifying `UserFactory`.

### Liskov Substitution Principle (LSP)

Principle: _Subtypes must be substitutable for their base types._

Examples:
1. `my_app/src/users.py`: Anywhere a `User` is expected, you could pass in either an `AdminUser` or a `NormalUser`.
2. `my_app/src/auth.py`: Currently, `BasicAuthStrategy.authenticate` takes in a `username` and a `password` parameter, while `TokenAuthStrategy.authenticate` expects `username` and `token`. For better consistency in the method signature, we will change these arguments to `username` and `credential`.

### Interface Segregation Principle (ISP)

Principle: _Keep interfaces small and focused._

Examples:
1. `my_app/src/events.py`: The `Observer` classes only have the `update` method, meaning the client is not forced to implement unneeded methods.
2. `my_app/src/service.py`: Right now, the `DataService` class is specifically bound to a single data source. We will therefore implement an additional `IDataService` interface.

In order to adhere to this principle as this project expands, it will be important to keep methods both simple in logic and decoupled from one another.

### Dependency Inversion Principle (DIP)

Principle: _High-level modules should not depend on low-level modules. Both should depend on abstractions._

1. `my_app/src/auth.py`: The `AuthContext` is a higher level module that depends on the `AuthStrategy` abstraction.
