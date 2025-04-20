from abc import ABC, abstractmethod

class BaseHandler(ABC):
    def __init__(self, id: str):
        self.id = id

    @abstractmethod
    def get_url(self) -> str:
        """Return the URL for the API request."""
        pass

    @abstractmethod
    def parse(self, data: dict) -> tuple[list[list], list[str]]:
        """Parse raw API data and return (rows, headers) for table display."""
        pass