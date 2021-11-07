def to_string(diff):
    def dict_to_str(items):
        res = '{\n'
        for key in items:
            if isinstance(items[key], dict):
                res += dict_to_str(items[key])
                return res
            res += '    {}: {}\n'.format(key, items[key])
        return res + '}'

    res = '{\n'
    for node in diff:
        if 'children' in node:
            res += '  {} {}: {}\n'.format(
                node['prefix'] if node ['prefix'] else ' ',
                node['name'],
                to_string(node['children'])
                )
        elif isinstance(node['value'], dict):
            for item in node['value']:
                res += '  {} {}: {}\n'.format(
                    node['prefix'] if node ['prefix'] else ' ',
                    node['name'],
                    dict_to_str(node['value'])
                )
        else:
            res += '  {} {}: {}\n'.format(
                node['prefix'] if node['prefix'] else ' ',
                node['name'],
                node['value'])
    return res + '}'


def printer(prefix, name, value, level):
    res = '{}  {} {}: {}\n'.format(
        '    ' * level,
        prefix if prefix else ' ',
        name,
        value)
    return res