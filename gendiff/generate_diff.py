import json


def generate_diff(file1, file2):
    data1 = json.load(open(file1))
    data2 = json.load(open(file2))

    data = {*data1, *data2}
    diff_log = []

    for key in data:
        if key in data1:
            if key in data2:
                if data1[key] == data2[key]:
                    res = [(' ', key, data1[key])]
                else:
                    res = [('-', key, data1[key]), ('+', key, data2[key])]
            else:
                res = [('+', key, data1[key])]
        else:
            res = [('+', key, data2[key])]
        diff_log.extend(res)

    diff_log.sort(key=lambda i: i[1])
    res = [f"{ch} {key}: {val}" for ch, key, val in diff_log]
    res_str = ''
    for item in res:
        res_str += item + '\n'
    return '{\n' + res_str + '}'
