# Note: I'm not use russian language, because first - it's vary bad in code
# and second - it's can confusion between any os systems.

replace_parts = {
    'One': 'One translated',
    'Two': 'Two translated',
    'Three': 'Three translated',
    'Four': 'Four translated'
}

with open('part_04.txt', 'r') as input_file:
    with open('part_04_output.txt', 'w') as output_file:
        for line in input_file:
            parts = line.split('-')
            parts = list(map(lambda el: str(el).strip(), parts))

            for key in replace_parts.keys():
                parts[0] = str(parts[0]).replace(key, replace_parts[key])

            output_file.write(f'{parts[0]} - {parts[1]}\n')

