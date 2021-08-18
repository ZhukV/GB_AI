def uppercase_first_char(string):
    """
    :param string:
    :return: Returns the new string where each word start with uppercase char
    :rtype str
    """
    words = str(string).split(' ')

    words = filter(lambda w: bool(w), words)
    words = map(lambda w: str(w[0]).upper() + str(w[1::]), words)

    return ' '.join(words)


if __name__ == '__main__':
    input_string = input('Please enter a few words separated by space: ')
    modified_string = uppercase_first_char(input_string)

    print(f'Result: {modified_string}')
