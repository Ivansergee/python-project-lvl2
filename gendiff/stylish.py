def to_string(diff, level=0):
    diff.sort(key=lambda i: i['name'])
    res = '{\n'
    for node in diff:
        if 'children' in node:
            res += printer(
                node['prefix'],
                node['name'],
                to_string(node['children'], level + 1),
                level
            )
        elif isinstance(node['value'], dict):
            res += printer(
                node['prefix'],
                node['name'],
                dict_to_str(node['value'], level + 1),
                level
            )
        else:
            res += printer(
                node['prefix'],
                node['name'],
                node['value'],
                level
            )
    return res + '    ' * level + '}'


def dict_to_str(items, level):
    res = '{\n'
    for key in items:
        if isinstance(items[key], dict):
            res += '{}{}: {}\n'.format(
                '    ' * (level + 1),
                key,
                dict_to_str(items[key], level + 1)
            )
        else:
            res += '{}{}: {}\n'.format(
                '    ' * (level + 1),
                key,
                items[key]
            )
    return res + '    ' * level + '}'


def printer(prefix, name, value, level):
    res = '{}  {} {}: {}\n'.format(
        '    ' * level,
        prefix if prefix else ' ',
        name,
        check_value(value)
    )
    return res


def check_value(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    return value
