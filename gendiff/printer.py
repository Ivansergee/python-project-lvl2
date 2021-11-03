def to_string(diff):
    res = [f"{ch} {key}: {val}" for ch, key, val in diff]
    res_str = ''
    for item in res:
        res_str += item + '\n'
    return '{\n' + res_str + '}'