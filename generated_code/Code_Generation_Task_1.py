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
            "first_name": cls.name[0],
            "last_name": cls.name[-1]
        }
class Email:
    def __init__(self, email: str):
        self.email = email
    @classmethod
    def get_email(cls) -> str:
        return cls._get_uuid() + ".com"
def main():
    uuid_obj = Person("John Doe")
    name_obj = Person("Jane Doe", "Smith")
    surname_obj = Person("Bob Smith", "Johnson")
    user1, user2 = User(uuid_obj)
    user3 = User(name_obj.get_user_info(), surname_obj.get_email())
    print("\nUser Information:")
    print(f"Person: {user1}")
    print(f"Email: {user3.get_email()}")
if __name__ == "__main__":
    main()