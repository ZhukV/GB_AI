import pytest
from part_01 import divide_two_numbers

data_for_testing = [
    (10, 2, 5),
    (15, 2, 7.5),
    (2, 1, 2),
]


@pytest.mark.parametrize('number, divider, expected', data_for_testing)
def test_divide(number, divider, expected):
    result = divide_two_numbers(number, divider)

    assert result == expected, 'Return wrong result after divide'
