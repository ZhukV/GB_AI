from typing import Generator


def factorial(f: int) -> Generator:
    result = 1

    for i in range(1, f + 1):
        result = result * i
        yield result


def main():
    for i, el in enumerate(factorial(5)):
        print(f'Element #{i + 1}: {el}')


if __name__ == '__main__':
    main()
