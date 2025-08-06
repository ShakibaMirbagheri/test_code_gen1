import uuid
from typing import Any, Callable, Dict, List, Optional
class Person(dict):
    def __init__(self, name: str = None, surname: str = None) -> None:
        self._name = name
        self._surname = surname
    @classmethod
    def from_string(cls, string: str) -> "Person":
        return cls(**{
            'uuid': uuid.uuid4(),
            'name': string or '',
            'surname': string or ''
        })