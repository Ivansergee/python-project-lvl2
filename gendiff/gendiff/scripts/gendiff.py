#!/usr/bin/env python
import argparse
import pathlib


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=pathlib.Path)
    parser.add_argument('second_file', type=pathlib.Path)
    parser.add_argument('-f', '--format', help='set the format of output')

    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
    main()