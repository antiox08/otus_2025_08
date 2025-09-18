from src.triangle import Triangle
import pytest


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area"),
                         [(3, 5, 4, 6.0),
                          (3.5, 5.5, 4.5, 7.854)],
                         ids=['integer', 'float'])
def test_triangle_area_positive(side_a, side_b, side_c, area):
    t = Triangle(side_a, side_b, side_c)
    assert t.area == area, f"Expected area should be {side_a + side_b + side_c}"

def test_triangle_invalid_value():
    with pytest.raises(ValueError):
        Triangle(1, 2, 10)
    assert f'neravenstvo triangle has broken'