import uuid
from typing import Any, Callable, Dict
class Person:
    def __init__(self, uuid: str, name: str, surname: str):
        self.uuid = uuid
        self.name = name
        self.surname = surname
    @classmethod
    def from_dict(cls, dict_obj) -> "Person":
        return cls(**{
            'uuid': uuid,
            'name': dict_obj['uuid'],
            'surname': dict_obj['surname']
        })
class User:
    def __init__(self, name: str):
        self.name = name
    @classmethod
    def from_dict(cls, dict_obj) -> "User":
        return cls(**{
            'uuid': uuid.uuid4(),
            'name': dict_obj['name'],
            'surname': dict_obj['surname']
        })
class Program:
    def __init__(self):
        self.person = Person("123")
    @staticmethod
    def get_user(username) -> User:
        return User(**{
                'uuid': uuid.uuid4(),
                'name': username
            }).from_dict()
    @staticmethod
    def create_new_user():
        user = Person("John Doe")
        print(f"User created with ID {user['id']}")
if __name__ == "__main__":
    program = Program()
    program.create_new_user()
    program.get_user("Alice")