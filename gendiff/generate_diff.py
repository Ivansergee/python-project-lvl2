from gendiff import parse
from gendiff import make_diff
from gendiff import to_string


def generate_diff(file1, file2):
    return to_string(make_diff(parse(file1), parse(file2)))
