import uuid
class Person:
    """
    A class representing a person with name, surname, age, and UUID.
    """
    def __init__(self, name, surname, age):
        """
        Initializes the person object with the given name, surname, and age.
        Args:
            name (str): The person's name.
            surname (str): The person's surname.
            age (int): The person's age.
        """
        self.uuid = str(uuid.uuid4())
        self.name = name
        self.surname = surname
        self.age = age
    def __str__(self):
        """
        Returns a string representation of the person object.
        Returns:
            str: A string representation of the person object.
        """
        return f"{self.name} {self.surname}, age {self.age}"
if __name__ == "__main__":
    # Test the Person class
    person = Person("John", "Doe", 30)
    print(person)