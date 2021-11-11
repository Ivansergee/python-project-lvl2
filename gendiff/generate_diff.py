from gendiff import parse, make_diff, to_string, plain


def generate_diff(file1, file2, format='str'):
    if format == 'str':
        return to_string(make_diff(parse(file1), parse(file2)))
    elif format == 'plain':
        return plain(make_diff(parse(file1), parse(file2)))
