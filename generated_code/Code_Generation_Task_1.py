import uuid
from typing import Any, Callable, Dict
class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
    @classmethod
    def get_uuid(cls) -> str:
        return uuid.uuid4().hex
    @staticmethod
    def toString():
        return f"Person({str(datetime.now())})"
class User:
    def __init__(self, name: str):
        self.name = name
    @classmethod
    def get_user_info(cls) -> dict:
        return {
            "id": cls._get_uuid(),
            "first_name": cls.name[:10],
            "last_name": cls.name[10:]
        }
def generate_java_class():
    uuid = uuid.uuid4()
    name = uuid.uuid4().hex
    return Person(name)
    # Add toString method for proper error handling and documentation generation