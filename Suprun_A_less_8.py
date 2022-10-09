import time

import math

print("***Task 1. Auto***")


class Auto:
    """Это родительский класс"""
    brand = ""
    mark = ""
    move = ""
    stop = ""
    age = 0

    def __init__(self, brand: str = None, mark: str = None, age: int = 0):
        """метод инициализирует атрибуты"""
        self.brand = brand
        self.mark = mark
        self.age = age

    def birthday(self):
        """метод увеличивает возраст на 1"""
        self.__init__(self.brand, self.mark, self.age)
        print("Birthday: ", int(self.age) + 1)

    def show(self) -> str:
        """метод выводит обязательные атрибуты"""
        return f"Brand: {self.brand} \nMark: {self.mark} \nAge: {self.age}"

    def move(self):
        """метод выводит move на экран"""
        print("move")

    def stop(self):
        """метод выводит stop на экран"""
        print("stop")


auto = Auto("BMW AG", "BMW", 9)
auto.move()
print("Auto 1")
print(auto.show())
auto.birthday()

auto2 = Auto("VAG", "Audi", 10)
print("Auto 2")
print(auto2.show())
auto2.birthday()
auto.stop()
print(Auto.__mro__)


print("***Task 2. Truck***")


class Truck(Auto):
    """Это наследник класса Auto"""
    max_load = 0

    def __init__(self, company: str = None, country: str = None):
        """метод инициализирует атрибуты"""
        super().__init__()
        self.company = company
        self.country = country

    def move(self):
        """метод выводит attention, move на экран"""
        print("attention")
        super().move()

    def show(self) -> str:
        """метод выводит данные на экран"""
        return f"Truck: {self.company} \nCountry: {self.country}"

    def load(self, max_load: int = 0):
        """метод выводит максимальный груз"""
        self.max_load = max_load
        time.sleep(1)
        print(f"max_load is {max_load} lbs")
        time.sleep(1)


truck = Truck("Caterpillar Inc.", "USA")
truck.move()
print(truck.show())
truck.load(120000)

truck2 = Truck("John Deere", "USA")
print(truck2.show())
truck2.load(140000)
print(Truck.__mro__)

print("***Task 2. Car***")


class Car(Auto):
    """Это наследник класса Auto"""
    max_speed = 0

    def __init__(self, mark: str = None, model: str = None):
        """метод инициализирует атрибуты"""
        super().__init__()
        self.mark = mark
        self.model = model

    def show(self) -> str:
        """метод выводит данные на экран"""
        return f"Mark: {self.mark} \nModel: {self.model}"

    def move(self, max_speed: int = 0):
        """метод выводит максимальную скорость"""
        self.max_speed = max_speed
        super().move()
        print(f"max_speed is {max_speed} km/h")


car = Car("BMW", "M5")
print(car.show())
car.move(305)

car2 = Car("Lamborgini", "Urus")
print(car2.show())
car2.move(310)
print(Car.__mro__)


print("***Task 3***")


class Circle:

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def __abs__(self, radius):
        return abs(self.radius)

    def __eq__(self, other):
        if isinstance(other, Circle):
            if abs(self.radius) == abs(other.radius):
                print(
                    circle_a.x + circle_b.x,
                    circle_a.y + circle_b.y
                )

            else:
                print(
                    circle_a.x + circle_b.x,
                    circle_a.y + circle_b.y,
                    abs(circle_a.radius + circle_b.radius)
                )


circle_a = Circle(-3, -5, -8)
circle_b = Circle(7, 8, 8)
print(circle_a == circle_b)


# обратный метод
#    def __ne__(self, other):
#        if isinstance(other, Circle):
#            if abs(self.radius) != abs(other.radius):
#                return True
#            else:
#                return False

# class New:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def birthday(self):
#         self.__init__(self.name, self.age)
#         print(self.age + 1)


# new = New("Nastya", 23)
# print(new)
# new.birthday()

