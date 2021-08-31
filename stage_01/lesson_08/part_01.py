import re
from typing import List


class Data:
    def __init__(self, data: str):
        self.data = data

    @classmethod
    def parse(cls, data: str) -> List[int]:
        if not re.match(r'\d{1,2}-\d{1,2}-\d{4}', data):
            raise ValueError(f'Pass wrong data {data}. Must be in format d-m-Y')

        parts = data.split('-')

        return list(map(lambda e: int(e), parts))

    @staticmethod
    def validate(data: str) -> bool:
        return bool(re.match(r'\d{1,2}-\d{1,2}-\d{4}', data))


data_1 = Data('01-01-2021')
print(f'Make a data object with data {data_1.data}')

data_list_for_parses = (
    '01-01-2021',
    '31-01-2021',
    '15-02-2021'
)

for el in data_list_for_parses:
    data_parts = Data.parse(el)

    print(f'The data {el} was been parsed to {data_parts}')


data_list_for_validate = (
    '01-01-2021',
    '02-2021',
    '2021'
)

for el in data_list_for_validate:
    valid = Data.validate(el)

    print(f'The data {el} is {"valid" if valid else "not valid"}')
