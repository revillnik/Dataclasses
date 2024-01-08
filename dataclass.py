from dataclasses import dataclass, field


@dataclass
class Data:
    name: str
    price: int
    area: list = field(default_factory=list)


a = Data("a", 25000)
a.area.append(10)
b = Data('b', 14000)
print(a)
print(b)

