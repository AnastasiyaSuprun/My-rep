from dataclasses import dataclass


@dataclass
class Profile:
    """This class sets profile data"""

    first_name: str
    last_name: str
    age: int
    country: str
    profession: str
    children: int
    hobby: str


profile = Profile("Petr", "Strelchov", 35, "Russia", "dentist", 2, "swimming")
print(
    f"My name is {profile.first_name} {profile.last_name}."
    f"I am {profile.age} years old."
    f"I live in {profile.country}."
    f"I am a {profile.profession}."
    f"I have {profile.children} children."
    f"My hobby is {profile.hobby}."
)


class Summa:
    """This class uses staticmethod"""

    @staticmethod
    def my_stat_method(x, y):
        return x**2 + y**3


print(Summa.my_stat_method(5, 7))


class Breakfast:
    """This class uses classmethod"""

    def __init__(self, dishes):
        self.dishes = dishes

    def __repr__ (self):
        return f"Choose your favourite breakfast: {self.dishes}"

    @classmethod
    def variants(cls):
        return cls(("cereals", "oatmeal", "sandwiches", "cup of coffee"))


print(Breakfast.variants())


# Variant 1 of using metaclasses
class Meta1(type):
    def __new__(cls, name, bases, dict):
        method = super().__new__(cls, name, bases, dict)
        return method


class User(metaclass=Meta1):
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Olga", 30)
print(User.__dict__)


# Variant 2 of using metaclasses
class Granddad(type):
    def __new__(cls, class_name, super_classes, attributes):
        print("class_name: ", class_name)
        print("super_classes: ", super_classes)
        print("attributes: ", attributes)
        return type.__new__(cls, class_name, super_classes, attributes)


class Child:
    pass


class Grandchild(Child, metaclass=Granddad):
    pass


grandchild = Grandchild()


