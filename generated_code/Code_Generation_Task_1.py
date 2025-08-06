import uuid
from typing import Any, Callable, Dict
class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
    @classmethod
    def from_json(cls, json_data: dict) -> "Person":
        uuid = uuid.uuid4()  # Create a random UUID for the object
        if not isinstance(json_data["person"], dict):
            raise ValueError("Invalid JSON data")
        name = json_data["name"]
        surname = json_data["surname"]
        age = json_data["age"]
        return cls(uuid=uuid, name=name, surname=surname, age=age)