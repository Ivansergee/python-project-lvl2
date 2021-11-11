def plain(diff, route=''):
    diff.sort(key=lambda i: i['name'])
    res = 'Property '
    for i, node in enumerate(diff):
        if 'children' in node:
            route += node['name'] + '.'
            plain(node['children'], route)
        elif diff[i+1]['name'] == node['name']:
            res += '{} was updated. From {} to {}'.format(
                route + node['name'],
                check_value(node['value']),
                check_value(diff[i+1]['value'])
            )
            diff[i+1].pop()
        elif node['prefix'] == '+':
            res += '{} was added with value: {}'.format(
                route + node['name'],
                check_value(node['value'])
            )
        elif node['prefix'] == '-':
            res += route + node['name'] + 'was removed'
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
    return value