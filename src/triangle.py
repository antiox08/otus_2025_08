from src.figure import Figure


class Triangle(Figure):

    def __init__(self, side_a: int, side_b: int, side_c: int) -> None:
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError(f'Triangle side must be greater than zero {side_a}, {side_b}, {side_c}')
        elif side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError('Sum of any two sides must be greater than the third side')
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    @property
    def area(self):
        p = self.perimetr / 2
        return (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5