def to_string(diff):
    r = '{\n  '
    for node in diff:
        if 'children' in node:
            pass
        else:
            res = '{} {}: {}\n'.format(
                node['prefix'] if node['prefix'] else ' ',
                node['name'],
                node['value'])
