from collections import Counter


def plain(diff, route=''):  # noqa
    diff.sort(key=lambda x: (x['name'], x['prefix']))
    count = Counter(i['name'] for i in diff)
    res = ''
    for index, node in enumerate(diff):
        name = node['name']
        prefix = node['prefix']
        if 'children' in node:
            new_route = route + name + '.'
            res += plain(node['children'], new_route)
        elif prefix == '+':
            if count[name] == 2:
                res += "Property '{}' was updated. From {} to {}\n".format(
                    route + name,
                    check_value(diff[index + 1]['value']),
                    check_value(node['value'])
                )
            else:
                res += "Property '{}' was added with value: {}\n".format(
                    route + name,
                    check_value(node['value'])
                )
        elif prefix == '-':
            if count[name] == 2:
                continue
            else:
                res += "Property '{}' was removed\n".format(
                    route + name
                )
    return res


def check_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return f"'{value}'"
    return value
