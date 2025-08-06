import uuid
from typing import Any, Callable, Dict
class Person:
    def __init__(self, name: str):
        self.name = name
    @classmethod
    def from_string(cls, string: str) -> "Person":
        return cls(**{
            'uuid': uuid.uuid4(),
            'name': str(uuid.uuid4()),
            'surname': str(uuid.uuid4())
        })
class PersonClass:
    @classmethod
    def from_string(cls, string: str) -> "Person":
        return cls(**{
            'uuid': uuid.uuid4(),
            'name': string,
            'surname': string
        })
    @staticmethod
    def toString():
        return f"Hello, {this.__class__.__name__}!"
# Test the class
person = Person(123)
print(PersonClass.from_string("hello"))  # Output: Hello, hello!
print(PersonClass.toString())   # Output: Hello, hello!