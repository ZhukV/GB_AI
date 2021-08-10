from part_02 import swap_items

import pytest

data_for_testing_swap = [
    [
        [],
        []
    ],
    [
        [1, 2],
        [2, 1]
    ],
    [
        ['foo', 'bar', 'some', 'element', 'fifth'],
        ['bar', 'foo', 'element', 'some', 'fifth']
    ],
    [
        [1, 'bar', 2, 'foo', True],
        ['bar', 1, 'foo', 2, True]
    ]
]


@pytest.mark.parametrize('input_list, expected_list', data_for_testing_swap)
def test_swap_items(input_list, expected_list):
    result_list = swap_items(input_list)

    assert result_list == expected_list, 'Receive wrong swapped items'


def test_swap_items_with_invalid_type():
    with pytest.raises(TypeError) as err:
        swap_items(123)

    assert 'Only list or tuple supported, but <class \'int\'> given.' in str(err.value)
