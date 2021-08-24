file = open('part_01.txt', 'w')

while True:
    write_data = input('Please enter text for write to file (empty string - end):')

    if write_data == '':
        break

    file.write(write_data + "\n")

file.close()
