def is_adult(age: int) -> bool:
    return age >= 18


class User:
    def __init__(self, age):
        self.age = age

    def get_age(self):
        return self.age
