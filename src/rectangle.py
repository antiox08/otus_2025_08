from src.figure import Figure


class Rectangle(Figure):

    def __init__(self, side_a: int | float, side_b: int | float) -> None:
        if side_a <= 0 or side_b <= 0:
            raise ValueError(f'rectangle should have sides greater that 0, actual {side_a}, {side_b}')
        self.side_a = side_a
        self.side_b = side_b

    @property
    def perimeter(self):
        return (self.side_a + self.side_b) * 2

    @property
    def area(self):
        return self.side_a * self.side_b


