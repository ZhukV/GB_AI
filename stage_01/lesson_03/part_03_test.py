import pytest
from part_03 import my_func

data_for_testing = [
    [(1, 2, 3), 5],
    [(2, 1, 3), 5],
    [(5, 2, 1), 7],
    [(0, 0, 0), 0]
]


@pytest.mark.parametrize('input_data, expected', data_for_testing)
def test_my_func(input_data, expected):
    result = my_func(*input_data)

    assert result == expected

