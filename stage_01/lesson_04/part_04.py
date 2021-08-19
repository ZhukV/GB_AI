from typing import List, Generator


def list_unique(input_list: List[int]) -> Generator:
    already_exist = []

    for el in input_list:
        if el in already_exist:
            continue

        already_exist.append(el)

        yield el


def main():
    our_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    result = list_unique(our_list)

    print(f'Input list: {our_list}')
    print(f'Result list: {list(result)}')


if __name__ == '__main__':
    main()
