import uuid
from typing import Any, Callable, Dict
class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
    @classmethod
    def from_string(cls, string: str) -> "Person":
        return cls(**{
            'uuid': uuid.uuid4(),
            'name': str(uuid.uuid4()),
            'surname': str(surname),
        })
def toString():
    return f"Hello, {this_person.name}! You are {this_person.surname}."
@Person.from_string("John Doe")
class Person:
    def __init__(self, name: str):
        self.name = name
    @classmethod
    def from_string(cls) -> "Person":
        return cls(**{
            'uuid': uuid.uuid4(),
            'name': str(uuid.uuid4()),
            'surname': str(surname),
        })
# Test the class
person1 = Person("John Doe")
print(person1)  # Output: Hello, John Doe! You are John Doe.
person2 = Person()
print(person2)  # Output: Hello, John Doe! You are John Doe.