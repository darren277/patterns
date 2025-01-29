""""""

class DataService:
    def get_data(self, query: str) -> str:
        print(f"Fetching data with query: {query}")
        return f"Result for {query}"

class CachingDecorator:
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
