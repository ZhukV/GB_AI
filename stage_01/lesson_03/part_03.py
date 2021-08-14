def my_func(a, b, c):
    data = (a, b, c)
    data = sorted(data, reverse=True)

    return data[0] + data[1]


if __name__ == '__main__':
    result = my_func(20, 10, 30)

    print(f'Result: {result}')
