def make_diff(data1, data2):

    keys = {*data1, *data2}
    diff_list = []

    for key in keys:
        if key in data1 and key in data2:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                diff_list.append({
                    'name': key,
                    'prefix': None,
                    'children': make_diff(data1[key], data2[key])
                    })
            elif data1[key] == data2[key]:
                diff_list.append({
                    'name': key,
                    'value': data1[key],
                    'prefix': None
                    })
            else:
                diff_list.extend([
                    {
                        'name': key,
                        'value': data1[key],
                        'prefix': '-'
                    },
                    {
                        'name': key,
                        'value': data2[key],
                        'prefix': '+'
                    }
                    ])
        elif key in data1:
            diff_list.append({
                'name': key,
                'value': data1[key],
                'prefix': '-'
            })
        else:
            diff_list.append({
                'name': key,
                'value': data2[key],
                'prefix': '-'
            })
    return diff_list