import pytest
from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from math import pi


@pytest.mark.parametrize(("circle", "other_figure", "summ_area"),
                         [(Circle(5), Rectangle(2, 3), 25 * pi + 6),
                          (Circle(2), Square(4), 4 * pi + 16)],
                         ids=['circle + rectangle',
                              'circle + square'])
def test_figure_area_positive(circle, other_figure, summ_area):
    f = circle.add_area(other_figure)
    assert f == summ_area, f"Expected area {summ_area}, got: {f}"
