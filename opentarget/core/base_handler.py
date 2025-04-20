import os
import json
import requests
from abc import ABC, abstractmethod

class BaseHandler(ABC):
    def __init__(self, entity_id: str):
        self.id = entity_id

    @abstractmethod
    def get_url(self) -> str:
        """Return the URL for the API request."""
        pass

    @abstractmethod
    def parse(self, data: dict) -> tuple[list[list], list[str]]:
        """Parse raw API data and return (rows, headers) for table display."""
        pass

    def fetch_or_load(self) -> dict:
        cache_file = f"data/{self.id}.json"
        if os.path.exists(cache_file):
            with open(cache_file, "r") as f:
                return json.load(f)
        else:
            response = requests.post(self.get_url()["url"], json=self.get_url()["json"])
            if response.status_code != 200:
                raise ValueError(f"Failed to fetch data: {response.text}")
            data = response.json()
            os.makedirs("data", exist_ok=True)
            with open(cache_file, "w") as f:
                json.dump(data, f)
            return data