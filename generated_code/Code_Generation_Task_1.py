import uuid
from typing import Any, Callable, Dict
class Person:
    def __init__(self, uuid_str: str):
        self.uuid = uuid_str
    @classmethod
    def from_string(cls, string: str) -> "Person":
        return cls(*[f"{s} {c}" for s, c in string.split(",")])