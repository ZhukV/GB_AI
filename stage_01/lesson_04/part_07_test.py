import pytest
from part_07 import factorial

data_for_testing = [
    (1, [1]),
    (2, [1, 2]),
    (3, [1, 2, 6]),
    (4, [1, 2, 6, 24]),
    (5, [1, 2, 6, 24, 120])
]


@pytest.mark.parametrize('fact, expected_list', data_for_testing)
def test_factorial(fact, expected_list):
    result = factorial(fact)

    assert list(result) == expected_list
