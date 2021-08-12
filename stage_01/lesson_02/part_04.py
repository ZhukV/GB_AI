string = input('Please enter a random string with space as separator: ')

parts = string.split(' ')

for i in range(len(parts[:10])):
    print(f'{i + 1}: {parts[i]}')

