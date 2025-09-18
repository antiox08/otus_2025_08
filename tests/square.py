from src.square import Square
import pytest


@pytest.mark.parametrize(("side_a", "area"),
                         [(3, 9),
                          (3.5, 12.25)],
                         ids=['integer', 'float'])
def test_square_area_positive(side_a, area):
    s = Square(side_a)
    assert s.area == area, f"Expected area should be {side_a * side_a}"
