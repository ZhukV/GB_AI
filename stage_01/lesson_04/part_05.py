from functools import reduce

out_list = range(100, 1001, 2)
total = reduce(lambda a, b: int(a) * int(b), out_list)

print(f'Total: {total}')
