import pytest
from part_04 import exponentiation

data_for_testing = (
    (1, 1, 1),
    (2, 2, 4),
    (3, 3, 27),
    (4, 4, 256),
    (5, 2, 25),
    (5, 1, 5)
)


@pytest.mark.parametrize('number, exponent, expected', data_for_testing)
def test_exponentiation(number, exponent, expected):
    result = exponentiation(number, exponent)

    assert result == expected


def test_exponentiation_with_invalid_exponent():
    with pytest.raises(ValueError) as err:
        exponentiation(1, 0)

    assert 'Exponent can\'t be less then 1, but 0 given.' in str(err.value)
