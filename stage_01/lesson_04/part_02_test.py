import pytest
from part_02 import search_large_elements

data_for_testing = [
    (
        (1, 2, 3, 4, 3, 4),
        (2, 3, 4, 4)
    ),

    (
        (100, 90, 50, 40),
        ()
    ),

    (
        (100, 200, 100, 200, 100, 200),
        (200, 200, 200)
    )
]


@pytest.mark.parametrize('input_list, expected_list', data_for_testing)
def test_search_large_elements(input_list, expected_list):
    result = search_large_elements(input_list)

    assert tuple(result) == expected_list
