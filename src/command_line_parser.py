import argparse
from unique_char_counter.src.unique_char_counter import count_unique_chars


def parser_uniq_chars():
    parser = argparse.ArgumentParser(description='Count the number of unique characters in a string or file')
    parser.add_argument('--string', type=str, help='Input string to count unique characters')
    parser.add_argument('--file', type=str, help='Input file to count unique characters')

    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r') as file:
            data = file.read()
    else:
        data = args.string

    return count_unique_chars(data)
