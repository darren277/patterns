""""""
from abc import ABC, abstractmethod

class IDataService(ABC):
    @abstractmethod
    def get_data(self, query: str) -> str:
        pass

class DataService(IDataService):
    def get_data(self, query: str) -> str:
        print(f"Fetching data with query: {query}")
        return f"Result for {query}"

class CachingDecorator(IDataService):
    def __init__(self, service: DataService):
        self._service = service
        self._cache = {}

    def get_data(self, query: str) -> str:
        if query not in self._cache:
            print("Cache miss!")
            self._cache[query] = self._service.get_data(query)
        else:
            print("Cache hit!")
        return self._cache[query]


# Some alternative decorators might include:
# - LoggingDecorator: For dedicated logging for the service.
# - TimingDecorator: For timing the service calls.
# - RateLimitingDecorator: For rate limiting the service calls.
# - RetryDecorator: For retrying the service calls in case of failures.
# - CircuitBreakerDecorator: For implementing a circuit breaker pattern for fault tolerance.

class LoggingDecorator(IDataService):
    def __init__(self, service: DataService):
        self._service = service

    def get_data(self, query: str) -> str:
        print(f"Logging: Fetching data with query: {query}")
        return self._service.get_data(query)
