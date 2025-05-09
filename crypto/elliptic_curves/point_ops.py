from dataclasses import dataclass
from typing import Optional, Self, TypeVar

inf = float("inf")

T = TypeVar('T')

def unwrap_optional(opt: Optional[T]) -> T:
    if opt is None:
        raise ValueError("Optional value is None")
    return opt

@dataclass
class Point:
    x: Optional[int]
    y: Optional[int]

    # p must be prime
    p: int

    # coefficient of the curve
    a: int

    # use Point(None, None) to represent O

    def __post_init__(self):
        if (self.x is None and self.y is not None) or (self.x is not None and self.y is None):
            raise ValueError

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.p == other.p and self.a == other.a

    def isO(self):
        return self.x is None and self.y is None

    def isInverse(self, other):
        return self.x == other.x and self.y == (-1 * other.y) % self.p

    def __add__(self, other: Self):
        if(self.p != other.p): raise ValueError

        if self.isO(): return other
        if other.isO(): return self

        if self.isInverse(other): return Point(None, None, self.p, self.a)

        x1 = unwrap_optional(self.x)
        y1 = unwrap_optional(self.y)
        x2 = unwrap_optional(other.x)
        y2 = unwrap_optional(other.y)
        p = self.p
        l = None

        if self != other:
            l = ((y2 - y1) * pow(x2 - x1, p-2, p)) % p
        else:
            l = ((3 * pow(x1, 2, p) + self.a) * pow(2 * y1, p-2, p)) % p
        
        x3 = (pow(l, 2, p) - x1 - x2) % p
        y3 = (l * (x1 - x3) - y1) % p

        return Point(x3, y3, self.p, self.a)

    def scale(self, scalar: int):
        Q = self
        R = Point(None, None, Q.p, Q.a)

        while scalar > 0:
            if scalar % 2 == 1:
                R = R + Q
            Q = Q + Q
            scalar = scalar // 2
            if scalar <= 0: break
        return R

X = Point(5274, 2841, 9739, 497)
Y = Point(8669,740,9739, 497)

P=Point(493,5564, 9739, 497)
Q=Point(1539,4742,9739, 497)
R=Point(4403,5202,9739, 497)

X=Point(5323,5438, 9739, 497)
assert(X.scale(1337) == Point(1089, 6931, X.p, X.a))

P=Point(2339,2213, 9739, 497)
Q=P.scale(7863)
print(Q)
