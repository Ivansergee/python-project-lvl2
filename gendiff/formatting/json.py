import json


def to_json(diff):

    def inner(diff, route=''):
        for node in diff:
            if 'children' in node:
                new_route = route + node['name'] + '.'
                inner(node['children'], new_route)
            elif node['prefix'] == '+':
                res['added'].update({route + node['name']: check_value(node['value'])})
            elif node['prefix'] == '-':
                res['removed'].update({route + node['name']: check_value(node['value'])})

    res = {
        'added': {},
        'removed': {},
        'updated': {}
    }

    inner(diff)
    return json.dumps(make_update(res))


def check_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    return value


def make_update(data):
    keys = {*data['added'], *data['removed']}
    for key in keys:
        if key in data['added'] and key in data['removed']:
            data['updated'].update({key: {
                'from': data['removed'].pop(key),
                'to': data['added'].pop(key)
            }})
    return data
