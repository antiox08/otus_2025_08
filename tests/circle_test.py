from src.circle import Circle
from math import pi
import pytest

@pytest.mark.parametrize(('side_a', 'area'),
                        [(4, pi*4*4),
                         (2.5, pi * 2.5 * 2.5)],
                         ids=['integer', 'float'])
def test_circle_area_positive(side_a, area):
    c = Circle(side_a)
    assert c.area == area, f"Expected area should be {pi * side_a * side_a}"

def test_circle_negative_area():
    with pytest.raises(ValueError):
        Circle(-1)
        assert f"side_a should be greater than zero"

