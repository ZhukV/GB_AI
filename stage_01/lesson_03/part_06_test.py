import pytest
from part_06 import uppercase_first_char

data_for_testing = (
    ('some', 'Some'),
    ('foo Bar', 'Foo Bar'),
    ('SOME TEXT', 'SOME TEXT')
)


@pytest.mark.parametrize('string, expected', data_for_testing)
def test_uppercase_first_char(string, expected):
    result = uppercase_first_char(string)

    assert result == expected
    
