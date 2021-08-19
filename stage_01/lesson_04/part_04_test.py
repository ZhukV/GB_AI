import pytest
from part_04 import list_unique

data_for_testing = [
    (
        (1, 2, 3, 4, 3, 4),
        (1, 2, 3, 4)
    ),

    (
        (100, 90, 50, 40),
        (100, 90, 50, 40)
    ),

    (
        (100, 200, 100, 200, 100, 200),
        (100, 200)
    )
]


@pytest.mark.parametrize('input_list, expected_list', data_for_testing)
def test_list_unique(input_list, expected_list):
    result = list_unique(input_list)

    assert tuple(result) == expected_list
