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

### Open/Closed Principle (OCP)

Principle: _Open for extension, but closed for modification._

### Liskov Substitution Principle (LSP)

Principle: _Subtypes must be substitutable for their base types._

### Interface Segregation Principle (ISP)

Principle: _Keep interfaces small and focused._

### Dependency Inversion Principle (DIP)

Principle: _High-level modules should not depend on low-level modules. Both should depend on abstractions._
