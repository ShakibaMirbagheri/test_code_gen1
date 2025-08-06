import uuid
from typing import Any, Callable, Dict
class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
    @staticmethod
    def get_uuid():
        return uuid.uuid4()
    @classmethod
    def from_string(cls, string: str) -> "Person":
        try:
            return cls(**{
                'name': string,
                'surname': string
            })
        except ValueError as e:
            print(f"Error: {e}")