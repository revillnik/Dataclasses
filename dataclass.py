from dataclasses import dataclass, field

@dataclass
class Data:
    name: str
    price: int
    area: list = field(default_factory=list)
    def __eq__(self, other):
        return self.price == other.price


a = Data("a", 14000)
a.area.append(10)
b = Data('b', 14000)
print(a)
print(b)
print(a == b)

