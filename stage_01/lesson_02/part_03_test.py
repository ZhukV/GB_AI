from part_03 import convert_month_from_list, convert_month_from_dict
import pytest

data_for_testing = [
    [1, 'January'],
    [6, 'June'],
    [12, 'December']
]


@pytest.mark.parametrize('month, expected_name', data_for_testing)
def test_correct_convert_month_name_from_list(month, expected_name):
    result = convert_month_from_list(month)

    assert result == expected_name, 'Wrong result month name from list.'


@pytest.mark.parametrize('month, expected_name', data_for_testing)
def test_correct_convert_month_name_from_dict(month, expected_name):
    result = convert_month_from_dict(month)

    assert result == expected_name, 'Wrong result month name from dict.'
