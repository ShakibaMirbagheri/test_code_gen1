import uuid
from typing import Any, Callable, Dict, List, Optional
class Person(object):
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname
    @classmethod
    def from_string(cls, string: str) -> "Person":
        uuid = str(uuid.uuid4())  # Generate a random UUID for the class
        return cls(**{
            'name': str(uuid),
            'surname': str(uuid),
        })