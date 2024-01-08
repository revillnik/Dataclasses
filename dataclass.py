from dataclasses import dataclass, field, InitVar


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
    



a = Data("a", 14000)
a.area.append(10)
print(a.sell)
print(a)
