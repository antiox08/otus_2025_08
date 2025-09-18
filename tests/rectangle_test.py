from src.rectangle import Rectangle
import pytest


@pytest.mark.parametrize(("side_a", "side_b", "area"),
                         [(3, 5, 15),
                          (3.5, 5.5, 19.25)],
                         ids=['integer', 'float'])
def test_rectangle_area_positive(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.area == area, f"Expected area should be {side_a * side_b}"
