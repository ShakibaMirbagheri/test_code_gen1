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
    return f"Name: {self.name}, Surname: {self.surname}"
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
print(person1)  # Output: Name: John Doe, Surname: John Doe
person2 = Person()
print(person2)  # Output: Name: John Doe, Surname: John Doe