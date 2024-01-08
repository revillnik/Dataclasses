from dataclasses import dataclass, field, InitVar, make_dataclass


@dataclass(eq=True, order=True)
class Data:
    name: str = field(compare=False)
    price: int
    area: list = field(default_factory=list, compare=False)
    sell: bool = field(default=True)
    allprice: float = field(init=False)

    def __eq__(self, other):
        return self.price == other.price

    def __post_init__(self):
        if self.sell:
            self.allprice = self.price * 0.9


@dataclass
class Child(Data):
    price: int = 50000
    photo: str = 'no'


Human = make_dataclass(
    "Human", [("age", int, 20)], bases=(Data,), namespace={"get_age": lambda self: self.age}
)

a = Data("a", 14000)
a.area.append(10)
print(a.sell)
print(a)
c = Human('Nikita', 50000)
print(c)
print(c.get_age())
f = Child('Egor', 12000)
print(f)

