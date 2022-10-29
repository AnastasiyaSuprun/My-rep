import re

# Task 1 by using class

class GeoSequence:
    """This class shows how geometric sequence works"""

    def __init__(self):
        """This method initializes attributes of the sequence"""
        self.b_n: float = 0
        self.sum: float = 0
        self.b = int(input("Enter first member: "))
        self.n = int(input("Enter ordinal number: "))
        self.q = float(input("Enter denominator: "))

    def count(self):
        """This method counts desired member and sum of sequence members"""
        self.b_n = self.b * (self.q ** (self.n - 1))
        self.sum = self.b * (1 - self.q ** self.n) / (1 - self.q)

        while self.b < self.b_n:
            self.b *= self.q
            yield f"Member: {self.b_n}, sum: {self.sum}"


geo_seq = GeoSequence()
print(next(geo_seq.count()))


# Task 1 by using function

def geopr():
    b = int(input("Enter first member: "))
    n = int(input("Enter ordinal number: "))
    q = float(input("Enter denominator: "))
    while q != 0 and n > 1:
        b = b * (q ** (n - 1))
        yield b


print(next(geopr()))


# Task 2 with regular expressions

regex = (
    r'[A-Za-z0-9]+ '
    r'[.!#%&*+-=?^_`{|}~] '
    r'[A-Za-z0-9]+ '
    r'@[A-Za-z0-9] '
    r'[A-Za-z0-9.-]{,61} '
    r'[A-Za-z0-9] '
)

result = re.match(regex, "Pro9.Ivan@yand-var.com")

print(result)

# Помогите... почему на сайте regex101 срабатывает, а в пайчарм нет?
