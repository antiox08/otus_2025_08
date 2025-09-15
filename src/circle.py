from src.figure import Figure
from math import pi

class Circle(Figure):

    def __init__(self, side_a: int):
        if side_a <= 0:
            raise ValueError(f'Circle side must be greater than zero {side_a}')
        self.side_a = side_a

    @property
    def perimeter(self):
        return  2 * pi * self.side_a

    @property
    def area(self):
        return pi * self.side_a ** 2
