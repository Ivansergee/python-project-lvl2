#!/usr/bin/env python
import argparse

from gendiff import generate_diff, parse, to_sting


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set the format of output')

    args = parser.parse_args()

    print(to_sting(generate_diff(parse(args.first_file), parse(args.second_file))))


if __name__ == '__main__':
    main()
